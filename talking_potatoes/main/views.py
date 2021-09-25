from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
# 랜딩페이지
def index(request) : 
    return render(request, 'index.html')

# read 페이지 
def likelion(request) : 
    likelion = Likelion.objects.all()
    context ={
        'likelion' : likelion,
    }
    return render(request, 'likelion.html', context)


# 좋아요. 로그인을 해야지만 가능하게 해야함. 아 ㅈ좆됐다 진짜... 어떡하지......................................
def likelion_like(request, pk) : 
    likelion = get_object_or_404(Likelion, pk = pk)
    if request.writer in likelion.like_users.all() : 
        likelion.like_users.remove(request.writer)
    else :
        likelion.like_users.add(request.writer)
        return redirect('likelion', likelion.pk)


# Create
def likelion_create(request) :
    user = request.user
    if user.is_authenticated : 
        if request.method == 'POST' : 
            post = Likelion()
            post.writer = User.objects.get(user = request.username) # 이게 문제 
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
