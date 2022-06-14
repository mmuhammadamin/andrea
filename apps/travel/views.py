from django.core.paginator import Paginator
from django.shortcuts import render
from validate_email import validate_email

from .forms import Contact_form, CommentForm, CommentForm_single,Contact_form_single
from .models import Post, Category, Tag


# Create your views here.


def travel_view(request):
    post = Post.objects.all().order_by('-id')
    last_posts = Post.objects.all().order_by('-id')[0:3]
    category = Category.objects.all()
    tag = Tag.objects.all()

    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()

    p = Paginator(Post.objects.all().order_by('-id')[:9], 2)
    page = request.GET.get('page')

    blog = p.get_page(page)
    list = []

    for page in range(1, blog.paginator.num_pages + 1):
        list.append(page)

    search_result = Post.objects.all().order_by('-id')
    result = request.GET.get('search')

    tags = request.GET.get('tag')

    categorys = request.GET.get('categorys')

    if tags:
        post = search_result.filter(tags__tag__exact=tags)
    if categorys:
        post = search_result.filter(category__category__exact=categorys)

    if result:
        post = search_result.filter(title__icontains=result)
    ctx = {
        'post': post,
        'category': category,
        'tag': tag,
        'last_posts': last_posts,
        'blog': blog,
        'list': list,
        'search_result': search_result,
        'form': form

    }

    return render(request, 'travel.html', ctx)


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    form = Contact_form(request.POST or None)
    if form.is_valid():
        form.save()

        # return redirect('/blog/')

    ctx = {
        'form': form
    }

    return render(request, 'contact.html', ctx)


def blog_single(request,pk):
    posts = Post.objects.all().order_by('-id')
    categories = Category.objects.all()
    post = Post.objects.get(id=pk)
    tags = Tag.objects.all()
    post1 = Post.objects.all().order_by('-id')[:3]

    form = CommentForm_single(request.POST or None)
    if form.is_valid():
        form.save()

    forms=Contact_form_single(request.POST or None)
    if forms.is_valid():
        obj = forms.save(commit=False)
        obj.post = post
        obj.save()

    # return redirect('/blog/')

    ctx = {
        'posts': posts,
        'categories': categories,
        'post': post,
        'tags': tags,
        'post1': post1,
        'form': form,
        'forms':forms

    }

    return render(request, 'single.html', ctx)
