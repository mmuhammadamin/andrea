from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import CreateCommentForm
from .models import Post, Category, Tag


# Create your views here.
def index_view(request):
    post = Post.objects.all().order_by('-id')
    last_posts = Post.objects.all().order_by('-id')[0:3]
    category = Category.objects.all()
    tag = Tag.objects.all()

    p = Paginator(Post.objects.all().order_by('-id')[:9], 5)
    page = request.GET.get('page')

    blog = p.get_page(page)
    list = []

    for page in range(1, blog.paginator.num_pages + 1):
        list.append(page)
    search = request.GET.get('search')
    tags = request.GET.get('tag')
    date = request.GET.get('date')
    categories = request.GET.get('categories')
    if date:
        post = search.filter(category__post__created_at__exact=date)
    if tags:
        blog = Post.objects.filter(tags__tag__exact=tags)
    if categories:
        blog = Post.objects.filter(category__category__exact=categories)
    if search:
        blog = Post.objects.filter(title__icontains=search)
    ctx = {
        'post': post,
        'category': category,
        'tag': tag,
        'last_posts': last_posts,
        'forms': forms,
        'blog': blog,
        'list': list,

    }

    return render(request, 'index.html', ctx)


def fashion_view(request):
    post = Post.objects.all().order_by('-id')

    p = Paginator(Post.objects.all().order_by('-id')[:9], 4)
    page = request.GET.get('page')

    blog = p.get_page(page)
    list = []

    for page in range(1, blog.paginator.num_pages + 1):
        list.append(page)

    ctx = {
        'post': post,
        'blog': blog,
        'list': list

    }

    return render(request, 'fashion.html', ctx)


def blog_single(request, pk):
    categories = Category.objects.all()
    post = Post.objects.get(id=pk)
    tags = Tag.objects.all()
    post1 = Post.objects.all().order_by('-id')[:3]

    form = CreateCommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        return redirect(f'/detail/{post.id}#comments')
        # return redirect('/blog/')

    ctx = {
        'categories': categories,
        'post': post,
        'tags': tags,
        'post1': post1,
        'form': form,

    }

    return render(request, 'single.html', ctx)
