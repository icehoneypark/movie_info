
from .forms import PostForm
from community.models import Post
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_safe
def community_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'community/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def community_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('community:community_detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
        'site_name': 'Create',
        'btn_name': 'create',
    }
    return render(request, 'community/form.html', context)

@require_safe
def community_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'community/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def community_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:community_detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form,
        'site_name': 'Update',
        'btn_name': 'update',
    }
    return render(request, 'community/form.html', context)

@login_required
@require_POST
def community_delete(request, pk):
    community = get_object_or_404(Post, pk=pk)
    community.delete()
    return redirect('community:community_index')
