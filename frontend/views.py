from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.utils.encoding import  smart_str
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .models import Employee,City,Country,State,Post
from .forms import RegisterForm,UpdateForm,AddForm,EditProfileForm,LoginForm,ForgetPassForm,password_reset,EditUserForm,UpdatePostForm
from django.contrib.auth.models import User
from django.contrib import sessions
from django.contrib import messages
import json
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from django.db.models import F
from .models import *
from django.db.models import Count
from django.contrib.auth.forms import PasswordChangeForm
import os
import getpass
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django import forms
from random import *
import os
from smtplib import SMTPException
import smtplib
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import user_tokenizer
from django.template.loader import get_template
from django.views.generic import View,CreateView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

def index(request):
    web  = Post.objects.all().get(title="Home",status=True)
    return render(request, 'frontend/index.html',{'web':web})
def about(request):
    posts = Post.objects.all().get(title="About Us", status=True)
    context = {
        'posts': posts,
    }
    return render(request, 'frontend/about.html',context)

def services(request):
    post = Post.objects.all().get(title="Services", status=True)
    return render(request, 'frontend/services.html',{'post':post})
def Product(request):
    return render(request, 'frontend/Product.html')

def userlogin(request):
    return render(request, 'frontend/userlogin.html')


def login1(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            u = Employee.objects.get(username=username)
            print(u)
            if u.status:
                p = u.password
                x = u.username
                if password == p:
                    request.session['username'] = username
                    request.session['password'] = password
                    return render(request, 'frontend/logged.html',
                                  {'WELCOME': x, 'wel': username, 'aa': request.session['username'],
                                   'bb': request.session['password']})

                else:
                   error = "Invalid Login Details Please Try Again"
                return render(request, 'frontend/userlogin.html', {'error': error})
            else:
                error = "Your Account has been Deactivated"
                return render(request, 'frontend/userlogin.html', {'error': error})
        except Exception as e:
            error = "NO SUCH USER EXIST...PLEASE SIGNUP TO LOGIN"
            context = {'error':error}
            return render(request,'frontend/userlogin.html',context)
    else:
        error = "Invaild User Login please signup First"
        return render(request, 'frontend/userlogin.html',{'error':error})

def logout1(request):
        try:
            del request.session['username']
            del request.session['password']
            return render(request, 'frontend/userlogin.html')
        except KeyError:
            print("x")

def forgot(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = ForgetPassForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = Employee.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "backend/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': domain,
                        'site_name': 'Interface',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset_done")
    password_reset_form = ForgetPassForm()
    return render(request=request, template_name="frontend/reset_pass.html",
                  context={"password_reset_form": password_reset_form})


def register(request):
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        print(fm)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            fname = fm.cleaned_data['firstname']
            lname = fm.cleaned_data['lastname']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            country = fm.cleaned_data['country']
            state = fm.cleaned_data['state']
            city = fm.cleaned_data['city']
            reg = Employee(username=uname, firstname=fname, lastname=lname, email=email, password=password, country=country, state=state, city=city)
            reg.save()
            messages.success(request, "The User Sucessfully created ! please login")
            return render(request, 'frontend/register.html')
    else:
        fm = RegisterForm()
        countries = Country.objects.filter(pk=101)
        return render(request, 'frontend/register.html', {'form': fm, 'countries':countries})

def UserStatus(request,id):
    studs = Employee.objects.get(id=id)
    if studs.status:
        studs.status = False
    else:
        studs.status=True
    studs.save()
    studs = Employee.objects.all()
    return render(request,'backend/usertable.html',{'studs':studs})


def UserTable(request):
    studs = Employee.objects.all()

    context = {
        'studs': studs,
    }
    return render(request, 'backend/usertable.html', context)


def delete_data(request,id):
    if request.method == "POST":
        pi=Employee.objects.get(pk=id)
        pi.delete()
        return redirect('UserTable')

def Update_data(request,id):
    if request.method == "POST":
        pi = Employee.objects.get(pk=id)
        fm = UpdateForm(request.POST, instance=pi)
        print(fm)
        if fm.is_valid():
            fm.save()

            return redirect('UserTable')
    else:
         pi = Employee.objects.get(pk=id)
         fm = UpdateForm(instance=pi)
    countries = Country.objects.filter(pk=101)
    return render(request,'backend/updatedata.html',{'form':fm, 'pi':pi,'countries':countries})


def adduser(request):
    if request.method == "POST":
        fm = AddForm(request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            fname = fm.cleaned_data['firstname']
            lname = fm.cleaned_data['lastname']
            email = fm.cleaned_data['email']
            country = fm.cleaned_data['country']
            state = fm.cleaned_data['state']
            city = fm.cleaned_data['city']
            reg = Employee(username=uname, firstname=fname, lastname=lname, email=email,country=country, state=state, city=city)
            reg.save()
            return redirect('UserTable')
    else:
        fm = AddForm()
        countries = Country.objects.filter(pk=101)
    return render(request, 'backend/adduser.html',{'form':fm,'countries':countries})


def EditProfile(request,id):
    if request.method == "POST":
        obj = User.objects.get(pk=id)
        fm = EditProfileForm(request.POST,instance=obj)
        print(fm)
        if fm.is_valid():
            fm.save()
            return redirect('dashboard')
    else:
        obj = User.objects.get(pk=id)
        fm = EditProfileForm(instance=obj)
    return render(request, 'backend/editprofile.html', {'form': fm})



def stateFetch(request, id):
    # serialized_queryset = serializers.serialize('python', some_queryset)
    # serialize object
    # serialized_object = serializers.serialize('python', [some_object, ])
    # id = request.post('id')
    states = State.objects.filter(country_id=id)
    # state = State.objects.all(country_id=id)
    data = serializers.serialize('json', states)
    return HttpResponse(data, content_type="application/json")

def cityFetch(request, id):

    cities = City.objects.filter(state_id=id)
    data = serializers.serialize('json', cities)
    return HttpResponse(data, content_type="application/json")


def ContentTable(request):
    content = Post.objects.all()


    context = {
        'content': content,

    }
    return render(request, 'backend/ContentTable.html', context)

def PostStatus(request,id):
    content = Post.objects.get(id=id)
    if content.status:
        content.status = False
    else:
        content.status = True
    content.save()
    content = Post.objects.all()
    return render(request, 'backend/ContentTable.html',{'content': content})

def UpdatePost(request,id):
    if request.method == "POST":
        pi = Post.objects.get(pk=id)
        fm = UpdatePostForm(request.POST, request.FILES, instance=pi)
        print(fm)
        if fm.is_valid():
            fm.save()
            return redirect('ContentTable')
    else:
        pi = Post.objects.get(pk=id)
        fm = UpdatePostForm( request.FILES,instance=pi)
    return render(request,'backend/UpdatePost.html',{'form': fm, 'pi': pi})

def delete_post(request,id):
    if request.method == "POST":
        pi=Post.objects.get(pk=id)
        pi.delete()
        return redirect('AllContent')
