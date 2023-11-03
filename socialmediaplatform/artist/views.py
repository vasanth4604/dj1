from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, HttpResponse
from .models import Artist, Person
import requests
from django.core.mail import send_mail
import random
# Create your views here



def home(request):
    return render(request,"artist/adminhome.html")
def myworks(request):
    mw = [
        {'category': 'Abstract Painting',
         'doc': '30-08-2023',
         'price': '1000 USD',
         'rating': '5',
         'inspiration': 'From Nature',
         },

        {'category': 'Digital',
         'doc': '15-07-2023',
         'price': '500 USD',
         'rating': '4',
         'inspiration': 'Technology Driven Nature',
         }
    ]
    return render(request, 'artist/myworks.html', {'mw': mw})
def profile(request):
    return render(request, template_name='artist/profile.html')
def history(request):
    works = [{"noc": "krishna", "pdate": "01-09-2023", "mop": "cash", "amount": "1000 USD", "category": "AbstractPainting"},
             {"noc": "vasanth", "pdate": "31-08-2023", "mop": "netbanking", "amount": "5000 USD", "category": "Digital"}]

    return render(request, 'artist/history.html',{"works":works})


def artlist(request):
    data=Artist.objects.all
    return render(request,'artist/artlist.html',{'data': data})

def climate(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=guntur&appid=5d1df6ff6b4953926271d95af4f172c9')
    data = response.json()
    return render(request, 'artist/climate.html', {'data': data})

def generate_otp():
    return str(random.randint(1000, 9999))

otp_storage = {}

def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generate_otp()


        otp_storage[email] = otp

        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'artist/validate_otp.html')
    return render(request, 'artist/send_otp.html')

def validate_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_otp = request.POST['otp']


        stored_otp = otp_storage.get(email)

        if user_otp == stored_otp:

            return HttpResponse('<h1>Login Success</h1>')
        else:
            return HttpResponse('<h1>Login Failed</h1>')
    return render(request, 'artist/validate_otp.html')

def list_person(request):
    items_per_page = 4
    data1 = Person.objects.all()
    paginator = Paginator(data1, items_per_page)
    page_number = request.GET.get('page')

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'artist/list_person.html', {"data": page})

