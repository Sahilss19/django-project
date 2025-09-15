from django.shortcuts import render , HttpResponse 
from django.views import View


#function based view
def home (request):
    return HttpResponse("heee bro")

#class based view

class HomeView(View):
    def get(self,request , *args ,**kwargs):
        return HttpResponse("<h1> Hello from class</h1>")

#for html page 

class HomeView(View):
    def get(self,request , *args ,**kwargs):
        return render(request , 'finance/home.html')