from django.urls import path
from .views import user_register,user_login,user_logout,index,restrictedView

urlpatterns = [
    path("",index,name="home"),
    path("signup/",user_register,name="signup"),
    path("login/",user_login,name="login"),
    path("logout/",user_logout,name="logout"),
    path("restrict",restrictedView,name="restrict")
]