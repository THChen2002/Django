from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime
import random

def student(request):
	std1 = {"name" : "Mike", "sid" : "A1101", "age" : 18}
	std2 = {"name" : "Eric", "sid" : "A1102", "age" : 20}
	std3 = {"name" : "Mary", "sid" : "A1103", "age" : 19}
	stds = [std1, std2, std3]
	return render(request, 'myapp/std.html', locals())

def hello(request):
	#return HttpResponse("Hello World")
	return render(request, 'myapp/hello.html')

def hello1 (request, username):
	now = datetime.now()
	return render(request, 'myapp/hello1.html', locals())

times = 0

def hello2 (request, username):
	global times
	times += 1
	local_times = times
	now = datetime.now()
	num1 = random.randint(1,6)
	num2 = random.randint(1,6)
	num3 = random.randint(1,6)
	dict1 = {"num1" : num1, "num2" : num2, "num3" : num3}
	score = random.randint(0,100)
	return render(request, 'myapp/hello2.html', locals())
	#return render(request, 'hello2.html', {"username" : locals(), "now" : now, "dice" : dict1})

	
