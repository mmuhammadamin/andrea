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
    image = models.ImageField(upload_to='travel/', null=True)
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


class ContactForm(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Comment_single(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
class Contact_Form_single(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    name=models.CharField(max_length=100)
    message=models.TextField(max_length=300)

    def __str__(self):
        return self.name




# Create your models here.
