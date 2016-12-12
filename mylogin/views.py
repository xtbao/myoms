#coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from models import Users
from .form import *
from django import forms
import hashlib
import time

# Create your views here.

def index(request):
    return render_to_response('index.html')

def login(request):
    if request.method == 'POST':
        uf = UserFormLogin(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            md5 = hashlib.md5()
            md5.update(password)
            password = md5.hexdigest()
            userResult = Users.objects.filter(username=username, password=password)
            if (len(userResult) > 0):
                return render_to_response('index.html')
            else:
                return HttpResponse("用户名或密码错误")
    else:
        uf = UserFormLogin()


    return render_to_response("userlogin.html", {'uf': uf})


def register(request):
    curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            #pdb.set_trace()
            #try:
            filterResult = Users.objects.filter(username=username)
            if len(filterResult) > 0:
                return render_to_response('register.html',
                                          {"errors": "用户名已存在"})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
               # errors = []
                if (password2 != password1):
                   # errors.append("两次输入的密码不一致!")
                   # return render_to_response('register.html',
                                          #    {'errors': errors})
                    #return HttpResponse('register.html',
                    #                   {"errors": "两次输入的密码不一致!,请重新输入密码"})
                    return HttpResponse("两次输入的密码不一致!,请重新输入密码")
                md5 = hashlib.md5()
                md5.update(password2)
                password = md5.hexdigest()
                email = uf.cleaned_data['email']
                #将表单写入数据库
                user = Users.objects.create(username=username,
                                           password=password,
                                           email=email)
                #user = Users(username=username,password=password,email=email)
                user.save()
                #返回注册成功页面
                return render_to_response(
                    'success.html', {'username': username,
                                     'operation': "zhuce"})
    else:
        uf = UserForm()


    return render_to_response('register.html', {'uf': uf})
