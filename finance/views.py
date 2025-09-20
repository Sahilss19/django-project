from django.shortcuts import render , HttpResponse , redirect
from django.shortcuts import render, redirect
from django.views import View
from finance.forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin 
# kisi bhi class base view ko yeh restrict krta h register login k bad hi dikhega 


class registerView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'finance/Register.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
       
class dashboardView(LoginRequiredMixin , View):
     def get(self, request, *args, **kwargs):
        return render(request, 'finance/dashboard.html')
    




# #function based view
# def home (request):   
#     return HttpResponse("heee bro")

# #class based view

# class HomeView(View):
#     def get(self,request , *args ,**kwargs):
#         return HttpResponse("<h1> Hello from class</h1>")

# #for html page 

# class HomeView(View):
#     def get(self,request , *args ,**kwargs):
#         return render(request , 'finance/home.html')