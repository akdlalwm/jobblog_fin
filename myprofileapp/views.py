from django.shortcuts import render

# Create your views here.


def profile(request):
    return render(request, "myprofile.html")


def cummunity(request):
    return render(request, "cummunity.html")
