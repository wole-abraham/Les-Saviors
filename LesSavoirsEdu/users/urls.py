from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup_view, name="sign_up"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile, name='profile'),
    

]