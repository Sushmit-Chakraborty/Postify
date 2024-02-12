from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import PostForm
from .models import Posts
# Create your views here.
def displayPosts(request):
    resultPost = Posts.objects.all()
    return render(request,"displayPost.html",{"result":resultPost})

def createPosts(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.save()
        return redirect("displayPosts")
    else:
        form = PostForm()
    return render(request,"addPost.html",{"form":form})

def updatePost(request,id):
    post = get_object_or_404(Posts,pk=id)
    form = PostForm(request.POST,instance=post)
    if form.is_valid():
        form.save()
        return redirect("displayPosts")
    else:
        form = PostForm()
    return render(request,"updatePost.html",{"form":form})

def deletePost(request,id):
    post = get_object_or_404(Posts,pk=id)
    post.delete()
    return redirect("displayPosts")