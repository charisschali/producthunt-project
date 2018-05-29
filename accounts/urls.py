from django.urls import path
from .views import (
login,
logout,
singup,
)
urlpatterns = [
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('singup/',singup,name='singup'),
    # path('accounts/',include('accounts.urls'),name='accounts'),
]
