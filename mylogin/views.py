# Create your views here.

from django.shortcuts import render_to_response,render,get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext 

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from forms import LoginForm

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html',RequestContext(request,{'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return render_to_response('index.html',RequestContext(request))
            else:
                return render_to_response('login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('login.html',RequestContext(request,{'form':form,}))


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")


@login_required
def index(request):
    return render_to_response('index.html')
