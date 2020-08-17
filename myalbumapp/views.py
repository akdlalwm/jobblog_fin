from django.shortcuts import render, redirect, get_object_or_404
from .models import My_Image

# Create your views here.


def myalbum(request):
    if request.method == "POST":
        my_image = My_Image()
        my_image.title = request.POST["title"]
        try:
            my_image.image = request.FILES["image"]
        except:
            pass
        my_image.save()
        return redirect("/myalbumapp/myalbum")
    else:
        my_image = My_Image.objects.all().order_by("-id")
        return render(request, "myalbum.html", {"myimage": my_image})


def remove_album(request, album_id):
    my_image = get_object_or_404(My_Image, pk=album_id)
    my_image.delete()
    return redirect("/myalbumapp/myalbum")

