from django.shortcuts import render, redirect
from news import models
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django import template
import math

page1 = 1

def index(request, pageindex=None):  #首頁
	global page1
	pagesize = 8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "news/index.html", locals())

def detail(request, detailid=None):  #詳細頁面
	unit = models.NewsUnit.objects.get(id=detailid)
	category = unit.catego
	title = unit.title
	pubtime = unit.pubtime
	nickname = unit.nickname
	message = unit.message
	unit.press += 1
	unit.save()
	return render(request, "news/detail.html", locals())

def login(request):  #登入
	messages = ''  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['password']  #取得輸入密碼
		user1 = authenticate(username=name, password=password)  #驗證
		if user1 is not None:  #驗證通過
			if user1.is_active:  #帳號有效
				auth.login(request, user1)  #登入
				return redirect('/newsadminmain/')  #開啟管理頁面
			else:  #帳號無效
				messages = '帳號尚未啟用！'
		else:  #驗證未通過
			messages = '登入失敗！'
	return render(request, "news/login.html", locals())

def logout(request):  #登出
	auth.logout(request)
	return redirect('/newsindex/')

def adminmain(request, pageindex=None):  #管理頁面
	global page1
	pagesize = 8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "news/adminmain.html", locals())

def newsadd(request):  #新增資料
	message = ''  #清除訊息
	category = request.POST.get('news_type', '')  #取得輸入的類別
	subject = request.POST.get('news_subject', '')
	editor = request.POST.get('news_editor', '')
	content = request.POST.get('news_content', '')
	ok = request.POST.get('news_ok', '')
	if subject=='' or editor=='' or content=='':  #若有欄位未填就顯示訊息
		message = '每一個欄位都要填寫...'
	else:
		if ok=='yes':  #根據ok值設定enabled欄位
			enabled = True
		else:
			enabled = False
		unit = models.NewsUnit.objects.create(catego=category, nickname=editor, title=subject, message=content, enabled=enabled, press=0)
		unit.save()
		return redirect('/newsadminmain/')
	return render(request, "news/newsadd.html", locals())

def newsedit(request, newsid=None, edittype=None):  #修改資料
	unit = models.NewsUnit.objects.get(id=newsid)  #讀取指定資料
	categories = ["公告", "更新", "活動", "其他"]
	if edittype == None:  #進入修改頁面,顯示原有資料
		type = unit.catego
		subject = unit.title
		editor = unit.nickname
		content = unit.message
		ok = unit.enabled
	elif edittype == '1':  #修改完畢,存檔
		category = request.POST.get('news_type', '')
		subject = request.POST.get('news_subject', '')
		editor = request.POST.get('news_editor', '')
		content = request.POST.get('news_content', '')
		ok = request.POST.get('news_ok', '')
		if ok=='yes':
			enabled = True
		else:
			enabled = False
		unit.catego=category
		unit.nickname=editor
		unit.title=subject
		unit.message=content
		unit.enabled=enabled
		unit.save()
		return redirect('/newsadminmain/')
	return render(request, "news/newsedit.html", locals())

def newsdelete(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.NewsUnit.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.catego.strip())
		subject = unit.title
		editor = unit.nickname
		content = unit.message
		date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/newsadminmain/')
	return render(request, "news/newsdelete.html", locals())

