from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from app1.forms import RecommendForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from app1.models import Recommend
from app1.models import FavBooks
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


# Create your views here.
def mainpage(request):
    return render(request,'base.html')

def aboutPage(request):
    current_time = datetime.now()
    return render(request,'about.html',{'time':current_time,'name1':'sangavi',"name2":"RAJ"})

def recForm(request):
    form = RecommendForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main')

    return render(request,'form1.html',{'data':form})

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main')
    return render(request,'signup.html',{'form':form})
@login_required(login_url='login')
def favBooks(request):
    data = FavBooks.objects.all()
    return render(request,'favBooks.html',{'data':data})

@login_required(login_url='login')
def myPage(request):
    return render(request,'myPage.html')

def viewRecommend(request):
    data = Recommend.objects.all()
    return render(request,'recommends.html',{'data':data})

def editRecommend(request,id):
    obj = get_object_or_404(Recommend,pk=id)
    form = RecommendForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('viewrec')
    return render(request,'editRec.html',{'form':form})

def deleteRecommend(request,id):
    obj = get_object_or_404(Recommend, pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect('viewrec')
    return render(request,'deleteRec.html',{'data':obj})

class AddBook(CreateView):
    model = FavBooks
    fields = "__all__"
    template_name = 'addBook.html'
    success_url = reverse_lazy('mypage')

class ViewBooks(ListView):
    model = FavBooks
    template_name = 'viewFav.html'
    context_object_name = 'obj'
    queryset = FavBooks.objects.all()

class UpdateBooks(UpdateView):
    model = FavBooks
    template_name = 'updateFav.html'
    fields = "__all__"
    success_url = reverse_lazy('viewFav')

    def get_object(self, queryset=None):
        obj = get_object_or_404(FavBooks,pk=self.kwargs['id']);
        return obj

class DeleteBooks(DeleteView):
    model = FavBooks
    template_name = 'deleteFav.html'
    success_url = reverse_lazy('viewFav')

    def get_object(self, queryset=None):
        obj = get_object_or_404(FavBooks,pk=self.kwargs['id'])
        return obj