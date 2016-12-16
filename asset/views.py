#coding:utf-8
from django.shortcuts import render
from asset.models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from asset.form import *

# Create your views here.

@login_required
def idc(request):
    all_idc = Idc.objects.all()
    return render_to_response("idc.html",locals())

@login_required
def addidc(request):
    nameInput = request.GET['nameInput']
    msgInput = request.GET['msgInput']
    idc_add = Idc(idc_name=nameInput,remark=msgInput)
    idc_add.save()
    return HttpResponse('ok')

@login_required
def idc_delete(request,id=None):
    if request.method == 'GET':
        id = request.GET.get('id')
        Idc.objects.filter(id=id).delete()
        return HttpResponseRedirect('/idc/')


@login_required
def mac(request):
    all_host = HostList.objects.all()
    all_idc = Idc.objects.all()
    return render_to_response("mac.html",locals())

@login_required
def addmac(request):
    if request.method == 'GET':
        name = request.GET['name']
        ip = request.GET['ip']
        idc_name = request.GET['idc_name']
        service = request.GET['service']
        idc_bh = request.GET['idc_jg']
        mac_add = HostList(ip=ip,hostname=name,application=service,idc_name=idc_name,bianhao=idc_bh)
        mac_add.save()
        return HttpResponse('ok')

@login_required
def mac_delete(request,id=None):
    if request.method == 'GET':
        id = request.GET.get('id')
        HostList.objects.filter(id=id).delete()
        return HttpResponseRedirect('/asset/mac/')

@login_required
def mac_edit(request,id=None):
    if request.method == 'GET':
        id = request.GET.get('id')
        all_idc = Idc.objects.all()
        all_host=HostList.objects.filter(id=id)
        return render_to_response("mac_edit.html",locals())

@login_required
def macresult(request):
    if request.method =='GET':
        id = request.GET['id']
        ip = request.GET['ip']
        name = request.GET['name']
        idc_name = request.GET['idc_name']
        service = request.GET['service']
        idc_bh = request.GET['idc_jg']
        try:
            mac_update = HostList.objects.filter(id=id).update(ip=ip,hostname=name,application=service,idc_name=idc_name,bianhao=idc_bh)
            mac_update.save()
        except:
            print "get exception"
        finally:
            return HttpResponse('ok')
class UploadForm(forms.Form):
    headImg = forms.FileField()
