from django.shortcuts import render,redirect
from .models import Teacher


# Create your views here.


def home(req):
    return render(req, 'home.html')


def addStudent(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        div = req.POST['div']
        doj = req.POST['doj']
        marks = req.POST['marks']
        mob = req.POST['mob']
        loc = req.POST['loc']

        data = Teacher.objects.create(name=name, email=email, div=div, doj=doj, marks=marks, mob=mob, loc=loc)
        data.save()

    return render(req, 'addstud.html')


def studList(req):
    stud = Teacher.objects.all()
    return render(req, 'studlist.html', {'students': stud})


def deleteStud(req, id):
    Teacher.objects.get(pk=id).delete()
    return redirect('studlist')


def updateStud(req,id):
    if req.method == 'POST':
        data = req.POST
        stdb = Teacher.objects.filter(id = id).first()

        name = data.get('name')
        email = data.get('email')
        div = data.get('div')
        doj = data.get('doj')
        marks = data.get('marks')
        mob = data.get('mob')
        loc = data.get('loc')
        stu= Teacher(name=name, email=email, div=div, doj=doj, marks=marks, mob=mob, loc=loc)
        if stdb:
            stdb.name = stu.name
            stdb.email = stu.email
            stdb.div = stu.div
            stdb.doj = stu.doj
            stdb.marks = stu.marks
            stdb.mob = stu.mob
            stdb.loc = stu.loc
            stdb.save()
        else:
            stu.save()
    return render(req,'update.html')