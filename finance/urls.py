from django.urls import path
from finance.views import home , HomeView

urlpatterns = [
    path('home/' , home , name = "home"),
    path('ghar/' , HomeView.as_view () , name = 'ghar') 

]