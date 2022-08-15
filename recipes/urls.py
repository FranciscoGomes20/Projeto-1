from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', home, name='home'),
    path('contato', contato, name='contato')
]
