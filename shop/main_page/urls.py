from django.urls import path
from . import views  # importing our view file

urlpatterns = [
    path("", views.main_page, name='main')
]
