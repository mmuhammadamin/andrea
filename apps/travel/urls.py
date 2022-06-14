from django.urls import path

from .views import travel_view,about_view,contact_view,blog_single

urlpatterns = [
    path('', travel_view, name='travel'),
    path('about/', about_view, name='about'),
    path('contact/',contact_view,name='contact'),
    path('detail/<int:pk>/', blog_single, name='detail'),

]
