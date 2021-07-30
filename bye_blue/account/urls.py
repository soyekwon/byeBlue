from django.urls import path
import account.views
import main.views

urlpatterns = [
    path('signup/',account.views.signup,name="signup"),
    path('login/',account.views.login,name="login"),
    path('logout/',account.views.logout,name="logout"),

]