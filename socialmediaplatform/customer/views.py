from django.shortcuts import render, HttpResponse

# Create your views here.
def gallery(request):
    return HttpResponse("<h1>view Gallery Here</h1>")
def offers(request):
    return HttpResponse("<h1>view offers</h1>")
def contact(request):
    return HttpResponse("<h1>view contacts</h1>")

