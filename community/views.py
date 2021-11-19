
from .forms import PostForm, CommunityCommentForm
from community.models import Post, CommunityComment
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


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
            post = form.save(commit=False)
            post.user = request.user
            post.save()
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
def community_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommunityCommentForm()
    comments = post.communitycomment_set.all()
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
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


@require_POST
def community_comment_create(request, post_pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_pk)
        comment_form = CommunityCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect('community:community_detail', post.pk)
    return redirect('accounts:login')


@login_required
def community_comment_update(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(CommunityComment, pk=comment_pk)
    if request.method == 'POST':
        comment_form = CommunityCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment.save()
            return redirect('community:community_detail', post_pk)
    else:
        comment_form = CommunityCommentForm(instance=comment)
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def community_comment_delete(request, post_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(CommunityComment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:community_detail', post_pk)