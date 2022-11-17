<<<<<<< HEAD
from django.urls import path
from .views import Calendar

urlpatterns = [
    
=======
from django.urls import path
from .views import Calendar

urlpatterns = [
    path('meetings/', Calendar.as_view(), name='meetings'),
>>>>>>> d65580a18b32607951d64a0183298524951258ec
]