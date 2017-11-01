from django.shortcuts import render,render_to_response

# Create your views here.

#start from here
#coding:utf-8
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
import time
import datetime
from wsgiref.simple_server import make_server
from backend import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def login(request):
    return render(request,'index/login.html')

def lost_password(request):
    return render(request,'index/lost_password.html')

def index(request):
    ip = request.META['REMOTE_ADDR'] ;
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    timeArray = time.strptime(now, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))

    context = {}
    if request.POST:
        name = request.POST.get('admin_username')
        pw = request.POST.get('admin_password')
        check_name = models.Administrator.objects.filter(username=name,status=1).count()
        check_pw_obj = models.Administrator.objects.get(username=name)
        check_pw = check_password(request.POST.get('admin_password'),check_pw_obj.password)
        if check_name==1:
            if check_pw:
                context['admin_username'] = request.POST.get('admin_username')
                context['permission'] = check_pw_obj.permission
                context['admin_num'] = models.Administrator.objects.count()
                context['banner_num'] = models.Banners.objects.count()
                context['event_num'] = models.Events.objects.count()
                context['post_num'] = models.Posts.objects.count()
                context['title'] = 'MISUMI MOBILE SITE'
                request.session['admin_id'] = check_pw_obj.id
                request.session['admin_username'] = check_pw_obj.username
                request.session['admin_password'] = make_password(check_pw_obj.password)
                models.Administrator.objects.filter(username=request.POST.get('admin_username')).update(update_time=timeStamp)
                models.Administrator.objects.filter(username=request.POST.get('admin_username')).update(last_login_time=timeStamp)
                models.Administrator.objects.filter(username=request.POST.get('admin_username')).update(last_login_ip=ip)
                return render(request,'index/index.html',context)
            else:
                return render(request,'index/login.html')
        else:
            return render(request,'index/login.html')
    else:
        context['admin_username'] = request.session.get('admin_username')
        check_pw_obj = models.Administrator.objects.get(username=context['admin_username'])
        context['permission'] = check_pw_obj.permission
        context['admin_num'] = models.Administrator.objects.count()
        context['banner_num'] = models.Banners.objects.count()
        context['event_num'] = models.Events.objects.count()
        context['post_num'] = models.Posts.objects.count()
        context['title'] = 'MISUMI MOBILE SITE'
        return render(request,'index/index.html',context)

def logout(request):
    del request.session['admin_id']
    del request.session['admin_username']
    del request.session['admin_password']
    return HttpResponseRedirect('/backend/login')

def admin(request):
    if request.session.get('admin_username'):
        context = {}
        admin_obj = models.Administrator.objects.get(username=request.session.get('admin_username'))
        context['permission'] = admin_obj.permission
        context['admin_username'] = request.session.get('admin_username')
        context['module_name'] = '管理员管理'
        context['module_title'] = '管理员'
        context['title'] = 'MISUMI MOBILE SITE'
        context['all'] = models.Administrator.objects.all()
        show_list = models.Administrator.objects.all()
        paginator = Paginator(show_list, 1)
        page = request.GET.get('page')
        try:
            context['show_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['show_list'] = paginator.page(1)
        except EmptyPage:
            context['show_list'] = paginator.page(paginator.num_pages)
        return render(request,'administrator/index.html',context)
    else:
        return HttpResponseRedirect('/backend/login')
    