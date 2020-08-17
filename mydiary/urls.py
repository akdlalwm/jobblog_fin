"""mydiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


import diaryapp.views
import myprofileapp.views
import myalbumapp.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", diaryapp.views.main, name="main"),
    path("detail/<int:diary_id>", diaryapp.views.detail, name="detail"),
    path("next/<int:diary_id>", diaryapp.views.next, name="next"),
    path("before/<int:diary_id>", diaryapp.views.before, name="before"),
    path("write/", diaryapp.views.write, name="write"),
    path("rewrite/<int:diary_id>", diaryapp.views.rewrite, name="rewrite"),
    path("remove/<int:diary_id>", diaryapp.views.remove, name="remove"),
    path("myprofileapp/myprofile/", myprofileapp.views.profile, name="myprofile"),
    path("myprofileapp/community/", myprofileapp.views.cummunity, name="cummunity"),
    path("myalbumapp/myalbum/", myalbumapp.views.myalbum, name="myalbum"),
    path(
        "myalbumapp/remove_album/<int:album_id>",
        myalbumapp.views.remove_album,
        name="remove_album",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
