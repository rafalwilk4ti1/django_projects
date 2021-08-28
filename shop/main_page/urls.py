from django.urls import path
from . import views  # importing our view file

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.main_page, name='main_page'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('sendemails', views.mail_letter, name='sendemails')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
