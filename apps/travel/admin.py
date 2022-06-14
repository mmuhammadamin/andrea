from django.contrib import admin
from .models import Post,Tag,Category,Comment,ContactForm,Comment_single,Contact_Form_single

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ContactForm)


admin.site.register(Comment_single)
admin.site.register(Contact_Form_single)


# Register your models here.
