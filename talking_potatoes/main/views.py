from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
# 랜딩페이지
def index(request) : 
    return render(request, 'index.html')

#####################################
# 멋사 read 페이지 
def likelion(request) : 
    sort = request.GET.get('sort')
    if sort == 'like_users':
        likelion = Likelion.objects.order_by('-like_users')
    else:
        likelion = Likelion.objects.order_by('-created')
    context ={
        'likelion' : likelion,
        'request' : request,
        'sort' : sort
    }
    return render(request, 'likelion.html', context)

# 멋사 좋아요. 
def likelion_like(request, pk) : 
    user = request.user
    likelion = Likelion.objects.get(pk=pk)
    if user.is_authenticated :
        if request.user in likelion.like_users.all() : 
            likelion.like_users.remove(request.user) # 좋아요 취소
            return redirect('likelion')
        else :
            likelion.like_users.add(request.user)
            return redirect('likelion')
    else :
        return redirect('/login')


# 멋사 Create
def likelion_create(request) :
    user = request.user
    if user.is_authenticated : 
        if request.method == 'POST' : 
            post = Likelion()
            post.writer = User.objects.get(username = request.user) # 이게 문제 
            post.likelion_first = request.POST['likelion_first']
            post.likelion_second = request.POST['likelion_second']
            post.created = timezone.datetime.now()
            post.save()
            return redirect('likelion')
    else :
        return redirect('/login')

    context = {
        'user' : user,
    }
    return render(request, 'create.html', context)


#########################################################
# 어흥 Read 페이지  
def growl(request) : 
    sort = request.GET.get('sort')
    if sort == 'like_users':
        growl = Growl.objects.order_by('-like_users')
    else:
        growl = Growl.objects.order_by('-created')
    context ={
        'growl' : growl,
        'request' : request,
        'sort' : sort
    }
    return render(request, 'growl.html', context)

# 어흥 좋아요. 로그인을 해야지만 가능하게 해야함.
def growl_like(request, pk) : 
    user = request.user
    growl = Growl.objects.get(pk=pk)
    if user.is_authenticated :
        if request.user in growl.like_users.all() : 
            growl.like_users.remove(request.user) # 좋아요 취소
            return redirect('growl')
        else :
            growl.like_users.add(request.user)
            return redirect('growl')
    else :
        return redirect('/login')

# 어흥 Create
def growl_create(request) :
    user = request.user
    if user.is_authenticated : 
        if request.method == 'POST' : 
            post = Growl()
            post.writer = User.objects.get(username = request.user) # 이게 문제 
            post.growl_first = request.POST['growl_first']
            post.growl_second = request.POST['growl_second']
            post.created = timezone.datetime.now()
            post.save()
            return redirect('growl')
    else :
        return redirect('/login')

    context = {
        'user' : user,
    }
    return render(request, 'growl_create.html', context)