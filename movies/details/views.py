from django.shortcuts import render
from django.urls import reverse_lazy
from details.models import Movie
from .forms import movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# def home(request):
#     m=Movie.objects.all
#     return render(request,'home.html',{'m':m})

class homeview(ListView):
    model=Movie
    template_name="home.html"
    context_object_name='m'


# def add(request):
#     if(request.method=="POST"):
#         n=request.POST['n']
#         y=request.POST['y']
#         d=request.POST['d']
#         i=request.FILES['i']
#         m=Movie.objects.create(name=n,year=y,desc=d,image=i)
#         m.save()
#         return home(request)
#     return render(request,'add.html')

class add(CreateView):
    model=Movie
    template_name="add1.html"
    fields=['name','desc','year','image']
    success_url=reverse_lazy('details:home')


# def details(request,n):
#     m=Movie.objects.get(id=n)
#     return render(request,'details.html',{'m':m})

class details(DetailView):
    model=Movie
    template_name="details.html"
    context_object_name='m'

# def delete(request,n):
#     m=Movie.objects.get(id=n)
#     m.delete()
#     return home(request)

class delete(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url=reverse_lazy('details:home')

# def update(request,n):
#     m=Movie.objects.get(id=n)
#     if(request.method=="POST"):
#         form=movieform(request.POST,request.FILES,instance=m)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form=movieform(instance=m)
#     return render(request,'add1.html',{'form':form})

class update(UpdateView):
    model = Movie
    template_name = "add1.html"
    fields = ['name', 'desc', 'year', 'image']
    success_url = reverse_lazy('details:home')




# Create your views here.
