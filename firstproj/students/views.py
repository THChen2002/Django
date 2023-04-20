from django.shortcuts import render, redirect
from students.form import PostForm

# Create your views here.
from students.models import student

def listone(request): 
    try: 
        unit = student.objects.get(stdName="Mary") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "students/listone.html", locals())

def listall(request):  
    allStudents = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "students/listall.html", locals())

def post(request):
    if request.method == "POST":
        mess = "姓名:" + request.POST['stdName'] + "\n學號:" + request.POST['stdID'] + "\性別:" + request.POST['stdSex'] + "\n生日:" + request.POST['stdBirth'] + "\n電話:" + request.POST['stdPhone']
    else:
        mess = "表單資料尚未送出!"
    return render(request, "students/addstudent.html", locals())

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
    return render(request, "students/addstudent1.html", locals())

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
    return render(request, "students/stdform.html", locals())

def delete(request, stdID = None):
    if id != None:
        if request.method == "POST":
            stdID = request.POST['stdID']
        #刪除一筆記錄
        try:
            unit = student.objects.get(stdID = stdID)
            unit.delete() #刪除資料庫資料
            return redirect('/listall')
        except:
            mess = "查無該學號"
    return render(request, "students/delete.html", locals())

def edit(request, stdID=None, mode=None):
    if mode == "edit":
        unit = student.objects.get(stdID = stdID)
        unit.stdName = request.GET["stdName"]
        unit.stdID = request.GET["stdID"]
        unit.stdSex = request.GET["stdSex"]
        unit.stdBirth = request.GET["stdBirth"]
        unit.stdPhone = request.GET["stdPhone"]
        unit.save()
        mess = "已修改完成"
        return redirect('/')
    else:
        try:
            unit = student.objects.get(stdID=stdID)
            strDate = str(unit.stdBirth)
            strDate2 = strDate.replace(" 年 ", "-")
            strDate2 = strDate.replace(" 月 ", "-")
            strDate2 = strDate.replace(" 日 ", "-")
            unit.stdBirth = strDate2
        except:
            mess = "此學號不存在"
        return render(request, "students/edit.html", locals())