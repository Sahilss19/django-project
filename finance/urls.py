from django.urls import path
# from finance.views import home , HomeView
from finance.views import registerView

urlpatterns = [
    # path('home/' , home , name = "home"),
    # path('ghar/' , HomeView.as_view () , name = 'ghar') 

    path('register/' , registerView.as_view(), name = "register")

]