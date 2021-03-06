# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from mysite import models, forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, 'Login successfully')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, "this account isn't active")
            else:
                messages.add_message(request, messages.WARNING, 'User name does not exist')
        else:
            messages.add_message(request, messages.INFO, 'Please check your input')
    else:
        login_form = forms.LoginForm()
    response = render(request, 'login.html', locals())
    return response

def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        try:
            user = User.objects.get(username=username)
            diaries = models.Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass
    messages.get_messages(request)
    return render(request, 'index.html', locals())

def listing(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:5]
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)

@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    if request.method == 'POST':
        user = User.objects.get(username=username)
        diary = models.Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "Diary is reserved")
            post_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, 'All the fields are required')
    else:
        post_form = forms.DiaryForm()
        messages.add_message(request, messages.INFO, 'All the fields are required')
    return render(request, 'posting.html',locals())

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = 'Thanks for your letter'
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
        else:
            message = 'Please check your input'
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html', locals())

def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = 'Your information is saved successfully'
            post_form.save()
            return HttpResponseRedirect('/list/')
        else:
            message = 'All the fields are required'
    else:
        post_form = forms.PostForm()
    return render(request, 'post2db.html', locals())

def logout(request):
    auth.logout(request)
    response = redirect('/')
    messages.add_message(request, messages.INFO, "Logout successfully")
    return response

@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            user = User.objects.get(username=username)
            userinfo = models.Profile.objects.get(user=user)
        except:
            pass
    return render(request, 'userinfo.html', locals())

