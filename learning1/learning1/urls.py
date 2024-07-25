"""
URL configuration for learning1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from form.views import *
from food.views import *
from fakedata.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home ,name='home'),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('datavisual/', datavisual, name='datavisulization'),
    path('foodreview/', foodreview, name='foodreview'),
    path('delete/<int:id>', deletequerry, name='delete'),
    path('update/<int:id>', updatequerry, name='update'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('fake/', fakedatageneration, name='fake'),



    path('admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
