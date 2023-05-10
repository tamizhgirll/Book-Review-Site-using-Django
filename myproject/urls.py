"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app1.views import mainpage, aboutPage, recForm,signup,favBooks,myPage
from app1.views import viewRecommend, editRecommend, deleteRecommend
from django.contrib.auth.views import LoginView, LogoutView

from app1.views import AddBook, ViewBooks, UpdateBooks, DeleteBooks

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainpage,name='main'),
    path('about/',aboutPage,name='about'),
    path('favBooks/',favBooks,name='fav'),
    path('recform/',recForm,name='form1'),
    path('myPage/',myPage,name='mypage'),

    path('signup/',signup,name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),

    path('viewRec/',viewRecommend,name='viewrec'),
    path('edit/<id>/',editRecommend,name='editrec'),
    path('delete/<id>/',deleteRecommend, name='deleterec'),

    path('addBook/',AddBook.as_view(),name='add'),
    path('viewFav/',ViewBooks.as_view(),name='viewFav'),
    path('editFav/<id>/',UpdateBooks.as_view(),name='updateFav'),
    path('deleteFav/<id>/',DeleteBooks.as_view(),name='delFav'),

    path('reset_password/',PasswordResetView.as_view(template_name='reset1.html'),name='password_reset'),
    path('reset_password_done/',PasswordResetDoneView.as_view(template_name='reset2.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='reset3.html'),name='password_reset_confirm'),
    path('reset_complete/',PasswordResetCompleteView.as_view(template_name='reset4.html'),name='password_reset_complete')
]
