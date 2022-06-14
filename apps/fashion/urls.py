from django.urls import path

from .views import index_view,fashion_view,blog_single
urlpatterns=[
    path('',index_view,name='index'),
    path('fashion/',fashion_view,name='fashion'),
    path('detail/<int:pk>/', blog_single, name='detail_fashion'),

]