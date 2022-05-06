"""B6_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path, include,re_path
from book import views 
from django.conf.urls import url


# urlpatterns =static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+{
#     path('admin/',admin.site.urls),path('home/',homepage),
# }


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage, name="homepage"),
    path('show-all-books/',views.show_all_books, name="show all books"),
    path('edit/<int:id>/', views.edit_data, name="edit"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
]


urlpatterns +=[
    re_path(r'^aaa$',views.view_a, name='view_a'),
    re_path(r'^bbb$',views.view_b, name='view_b'),
    re_path(r'^ccc$',views.view_c, name='view_c'),
    re_path(r'^ddd$',views.view_d, name='view_d'),
]
 

urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls')),
    path('user-login/', views.user_login, name="user_login"),
]
