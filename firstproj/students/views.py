from django.shortcuts import render, redirect
from students.form import PostForm

# Create your views here.
from students.models import student

def listone(request): 
    try: 
        unit = student.objects.get(stdName="Mary") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())

def listall(request):  
    allStudents = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())

def post(request):
    if request.method == "POST":
        mess = "姓名:" + request.POST['stdName'] + "\n學號:" + request.POST['stdID'] + "\性別:" + request.POST['stdSex'] + "\n生日:" + request.POST['stdBirth'] + "\n電話:" + request.POST['stdPhone']
    else:
        mess = "表單資料尚未送出!"
    return render(request, "addstudent.html", locals())

def post1(request):
    if request.method == "POST":
        stdName = request.POST['stdName']
        stdID = request.POST['stdID']
        stdSex = request.POST['stdSex']
        stdBirth = request.POST['stdBirth']
        stdPhone = request.POST['stdPhone']
        #新增一筆記錄
        unit = student.objects.create(stdName = stdName, stdID = stdID, stdSex = stdSex, stdBirth = stdBirth, stdPhone = stdPhone)
        unit.save() #寫入資料庫
        return redirect('/post1')
    else:
        mess = '請輸入資料(資料不作驗證)'
    return render(request, "addstudent1.html", locals())

def postform(request):
    stdform = PostForm()
    if request.method == "POST":
        stdName = request.POST['stdName']
        stdID = request.POST['stdID']
        stdSex = request.POST['stdSex']
        stdBirth = request.POST['stdBirth']
        stdPhone = request.POST['stdPhone']
        #新增一筆記錄
        unit = student.objects.create(stdName = stdName, stdID = stdID, stdSex = stdSex, stdBirth = stdBirth, stdPhone = stdPhone)
        unit.save() #寫入資料庫
    return render(request, "stdform.html", locals())