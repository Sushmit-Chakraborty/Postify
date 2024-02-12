from django.urls import path
from .views import displayPosts,createPosts,updatePost,deletePost
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',displayPosts,name='displayPosts'),
    path('add',createPosts,name='createPosts'),
    path('update/<int:id>',updatePost,name='updatePost'),
    path('delete/<int:id>',deletePost,name='deletePost'),
    path('contact',TemplateView.as_view(template_name='contact.html'), name='contact')
]