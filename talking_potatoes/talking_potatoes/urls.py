"""talking_potatoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import main.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('account.urls')),
    path('admin/', admin.site.urls),
    path('', main.views.index, name = 'index'),
    path('likelion/', main.views.likelion, name = 'likelion'), # 멋사
    path('likelion/<int:pk>', main.views.likelion_like, name = 'likelion_like'),
    path('likelion/create/', main.views.likelion_create, name = 'likelion_create'),
    #path('likelion/rank', main.views.likelion_ranking, name = 'likelion_ranking'), # 랭킹 순위 매기기 


    path('growl/', main.views.growl, name = 'growl'), # 어흥
    path('growl/<int:pk>', main.views.growl_like, name = 'growl_like'), # 어흥 좋아요
    path('growl/create/', main.views.growl_create, name = 'growl_create'), 

]
