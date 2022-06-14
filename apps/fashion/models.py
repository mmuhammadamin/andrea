from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Post(models.Model):
    image = models.ImageField(upload_to='fashion/', null=True)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=500)

    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Comment1(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=222)
    message = models.TextField()

    def __str__(self):
        return self.full_name


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.name
