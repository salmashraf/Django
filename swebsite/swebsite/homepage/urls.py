from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
#from django.conf import settings

from . import views
urlpatterns= [

path('admin/', admin.site.urls),
path('', views.pagesIndex),
path ('books/', views.viewBooks),
path('about/', views.homepageAbout),

]