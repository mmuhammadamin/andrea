from django.contrib import admin
from .models import Post,Tag,Category,Comment,ContactForm

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ContactForm)

# Register your models here.
