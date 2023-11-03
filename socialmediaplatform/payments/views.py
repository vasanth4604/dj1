from django.shortcuts import render, HttpResponse

# Create your views here.
def pay(request):
    return HttpResponse("<h1>view amount</h1>")
