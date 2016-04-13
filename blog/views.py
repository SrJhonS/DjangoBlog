from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from .forms import PostForm, CommentForm
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #import ipdb; ipdb.set_trace()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk) 
    comments = Comment.objects.filter(post=post).order_by('created_date')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                comment = form.save(commit=False)            
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
            else:
                return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form })

@login_required(login_url='login')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            #post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url='login')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post })

@login_required(login_url='login')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')