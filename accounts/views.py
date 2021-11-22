from django.http.response import JsonResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required

@require_http_methods(['GET', 'POST'])
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('community:community_index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    # 이미 로그인이 돼있으면 index로 redirect
    else:
        return redirect('community:community_index')


@require_http_methods(['GET', 'POST'])
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect(request.GET.get('next') or 'community:community_index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('community:community_index')


def logout(request):
    auth_logout(request)
    return redirect('movies:movie_index')


@login_required
def change(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user)
    else:
    	form = CustomUserChangeForm(instance=request.user)
    context = {
    	'form':form,
    }
    return render(request, 'accounts/change.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('accounts:login')


@require_safe
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = request.user
        another = get_object_or_404(get_user_model(), pk=user_pk)
        if another != person:
            if another.followers.filter(pk=person.pk).exists():
                another.followers.remove(person)
                isFollowed = False
            else:
                another.followers.add(person)
                isFollowed = True
            data = {
                'isFollowed': isFollowed,
                'followings_cnt': another.followings.count(),
                'followers_cnt': another.followers.count(),
            }
            return JsonResponse(data)
        return redirect('accounts:profile', another.username)
    return redirect('accounts:login')

@login_required
@require_http_methods(['GET', 'POST'])
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('community:community_index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)