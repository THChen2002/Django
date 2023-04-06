from django.shortcuts import render, redirect

# 匯入相關套件
from django.http import HttpResponse
import datetime
# login authentication
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

from CookieSessionApp.form import PostForm

# Create your views here.
# 新增設定cookie函式
def set_cookie(request,key=None,value=None):
	response = HttpResponse('Cookie 儲存完畢!')
	response.set_cookie(key, value)
	return response
    
# 新增取得cookie函式
def get_cookie(request,key=None):
	if key in request.COOKIES:
		return HttpResponse('%s : %s' %(key,request.COOKIES[key]))
	else:
		return HttpResponse('Cookie 不存在!')

# 新增設定cookie函式，加入有效時間
def set_cookie2(request,key=None,value=None):
	response = HttpResponse('Cookie 有效時間1小時!')
	response.set_cookie(key,value,max_age=3600)
	return response			

# 新增刪除cookie函式	
def delete_cookie(request,key=None):
    if key in request.COOKIES:
        response = HttpResponse('Delete Cookie: '+key)	
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse('No cookies:' + key)

# 瀏覽次數計算
def pagecount(request):
	if "counter" in request.COOKIES:
		counter=int(request.COOKIES["counter"])
		counter+=1
	else:		
		counter=1
	response = HttpResponse('今日瀏覽次數：' + str(counter))		
	tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
	tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0)
	expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT") 
	response.set_cookie("counter", counter, expires=expires)
	return response
    
# 顯示所有cookies
def get_allcookies(request):
	if request.COOKIES!=None:
		strcookies=""
		for key1,value1 in request.COOKIES.items():
			strcookies= strcookies + key1 + ":" + value1 + "<br>"
		return HttpResponse('%s' %(strcookies))
	else:
		return HttpResponse('Cookie 不存在!')
        
# 新增設定session函式
def set_session(request,key=None,value=None):
	response = HttpResponse('Session 儲存完畢!')
	request.session[key]=value
	return response

# 新增取得session函式
def get_session(request,key=None):
	if key in request.session:
		return HttpResponse('%s : %s' %(key,request.session[key]))
	else:
		return HttpResponse('Session 不存在!')
		
# 新增投票函式，並存入session中
def vote(request):
	if not "vote" in request.session:
		request.session["vote"]=True
		msg="您第一次投票!"		
	else:		
		msg="您已投過票!"			
	response = HttpResponse(msg)		
	return response					

# 顯示所有sessions
def get_allsessions(request):
	if request.session!=None:
		strsessions=""
		for key1,value1 in request.session.items():
			strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
		return HttpResponse(strsessions)
	else:
		return HttpResponse('Session 不存在!')	

# 新增設定session函式，持續時間30秒
def set_session2(request,key=None,value=None):
	response = HttpResponse('Session 儲存完畢!')
	request.session[key]=value
	request.session.set_expiry(30) # 設持續的時間為30秒
	return response

# 新增刪除session函式
def delete_session(request,key=None):
	if key in request.session:
		response = HttpResponse('Delete Session: '+key)	
		del request.session[key]
		return response
	else:
		return HttpResponse('No Session:' + key)
"""
def login(request):
	#預設帳號密碼
	username = "jeng"
	password = "1234"
	if request.method == 'POST':
		if not 'username' in request.session:
			if request.POST['username']==username and request.POST['password']==password:
				request.session['username']=username #儲存Session
				mess=username + " 您好，登入成功！"
				status="login"
	else:
		if 'username' in request.session:
			if request.session['username']==username:
				mess=request.session['username'] + " 您已登入過了！"
				status="login"				
	return render(request, 'login.html',locals())
	
def logout(request):
	if 'username' in request.session:
		mess=request.session['username'] + ' 您已登出!'
		del request.session['username']	#刪除Session	
	return render(request, 'login.html',locals())
"""
def mypage(request):
	if request.user.is_authenticated:
		name=request.user.username
	return render(request, "mypage.html", locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/mypage/')
				mess = '登入成功！'
			else:
				mess = '帳號尚未啟用！'
		else:
			mess = '登入失敗！'
	return render(request, "login.html", locals())
	
def logout(request):
	auth.logout(request)
	return redirect('/mypage/')	

def adduser(request):	
	try:
		user=User.objects.get(username="test")
	except:
		user=None
	if user!=None:
		mess = user.username + " 帳號已建立!"
		return HttpResponse(mess)
	else:	# 建立 test 帳號			
		user=User.objects.create_user("test","test@test.com.tw","a123456!")
		user.first_name="wen" # 姓名
		user.last_name="lin"  # 姓氏
		user.is_staff=True	# 工作人員狀態
		user.save()
		return redirect('/admin/')

def register(request):
	userform = PostForm()
	if request.method == "POST":
		userName = request.POST['userName']
		userPassword = request.POST['userPassword']
		userEmail = request.POST['userEmail']
		userFirstName = request.POST['userFirstName']
		userLastName = request.POST['userLastName']
		user=User.objects.create_user(userName,userEmail,userPassword)
		user.first_name=userFirstName # 姓名
		user.last_name=userLastName  # 姓氏
		user.save()
		return redirect('/mypage/')
	return render(request, "register.html", locals())