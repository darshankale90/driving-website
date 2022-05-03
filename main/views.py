import requests
from django.shortcuts import render
from main import models as pmodels
from django.contrib.auth import *
from django.contrib.auth import login as log_auth
from django.http import *
from django.urls import reverse
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
import json
import requests


def home(request):
    return render(request, 'home.html', context={})

@login_required
def slot(request):
    mid = request.session['mid']

    if(request.method == "GET"):
        sdate = datetime.datetime.now().date()
        ldate = (sdate + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        sdate = sdate.strftime("%Y-%m-%d")

        udetails = models.User.objects.get(id=mid)
    if(request.method == "POST"):
        date = 0
        name = request.POST.get('form_name')
        if name == 'slot_confirm':
            slotid = request.POST.get('slot_select')
            date = request.POST.get('date')
            new_slot = pmodels.bookingdb.objects.create(
                slotid_id=slotid, date=date, userid_id=mid)
            return render(request, 'success.html')
        else:
            date = request.POST.get("slot_date")
            print(date)
            booked = 0
            try:
                slot_p = pmodels.bookingdb.objects.get(
                    date=date, userid_id=mid)
                booked = 1
                print(booked)
                return render(request, 'slotconfirm.html', context={"booked": 1, "date": datetime.datetime.strptime(date, '%Y-%m-%d').date()})
            except:
                print(booked)
                avail_list = []
                date = request.POST.get("slot_date")
                slotids = pmodels.slotdb.objects.filter(active=True)
                day_books = pmodels.bookingdb.objects.filter(date=date)
                for i in slotids:
                    available = i.capacity - day_books.filter(slotid_id=i.slotid).count();
                    if(available > 0):
                        avail_list.append(i)

                return render(request, 'slotconfirm.html', context={"avail_slots": avail_list, "date": datetime.datetime.strptime(date, '%Y-%m-%d').date(), "rdate": date})

    return render(request, 'appointment.html', context={"udetails": udetails, "sdate": sdate, "ldate": ldate})


def login(request):
    if request.method == "POST":

        email = request.POST.get('email');
        passwrd = request.POST.get('password');
        # try:
        user = models.User.objects.get(email=email)

        if user.check_password(passwrd):
            print(user);
            log_auth(request, user);
            request.session['mid'] = user.id;
            request.session['name'] = user.first_name;
            return HttpResponseRedirect(reverse('homepage'))


        else:
            messages.error(request, "Email or Password incorrect")
        # except models.User.DoesNotExist:
                # messages.error(request, "Email or Password incorrect")
    return render(request, 'login3.html')


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:

            user = models.User.objects.get(email=email)
            print("User alrady")
            messages.error(request, "User already exists")

        except:
            print(email)
            passwrd = request.POST.get('password')
            phone = request.POST.get('phone')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')


            obj = models.User.objects.create(email=email.lower(),username=phone,first_name=fname,last_name=lname)
            obj.set_password(passwrd)
            obj.save()
            messages.success(
                request, "Registration Successfull. KINDLY LOGIN !")
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'login3.html', context={"signup":1})

@login_required

def simple_upload(request):
    mid=request.session['mid']
    name=models.User.objects.get(id=mid);
    if request.method == 'POST' and request.FILES['filename']:
        headers = {"Authorization": "Bearer ya29.A0ARrdaM-wy0HeUa0KJIGVMTSgtJsvZKO3FJMuBs089WFipIMUdupYjEBeA-uzeGqtXVDF194zEkyRmutvhWJ_ISdTWe0K21svAK7ZuN_Cf5BDuREtglQKitzrRkAXaPv_bzH2G6MIUGGWVeLedJu0RY5TMwLi"}
        for i in request.FILES.getlist('filename'):
            # myfile = request.FILES['filename']
            # fs = FileSystemStorage()
            # print(i.name)
            # filename = fs.save(i.name, i)
            # uploaded_file_url = fs.url(filename)
            para = {
                "name": name.first_name+" "+ name.last_name + " "+ i.name,
            }
            files = {
                'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                'file': i,
            }
            r = requests.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers=headers,
                files=files
            )
        return render(request, 'upload_success.html')
    return render(request, 'fileupload.html')

def logout_view(request):
    del request.session['mid']
    logout(request)
    # messages.success("Logout Successfull")
    return HttpResponseRedirect(reverse('homepage'))
