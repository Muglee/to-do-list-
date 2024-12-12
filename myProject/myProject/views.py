from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.contrib import messages
from myApp.models import *
from myProject.forms import *
from datetime import date

def SignUpPage(req):
    if req.method =='POST':
        form=myUserCreationform(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"SignUp Successfully")
            return redirect('SignInPage')
    else:
        form=myUserCreationform(req.POST)
            
    context={
        'form':form,
    }
    return render(req,"signup.html",context)
  

def SignInPage(req):
    if req.method == 'POST':
        signinForm = myAuthenticationForm(req,data =req.POST)
        if signinForm.is_valid():
            i=signinForm.get_user()
            login(req,i)
            return redirect("dashboardPage")
    else:
        signinForm = myAuthenticationForm()
    
    context={
        "signinForm":signinForm
    }
    
    return render(req,"signin.html",context)

def dashboardPage(req):
    return render(req,"dashboardPage.html")

def logoutPage(req):
    logout(req)
    return redirect("SignInPage")

def categoryPage(req):
    if req.method == 'POST':
        form = CategoryForm(req.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = req.user
            category.save()
            return redirect("categorylist")
    else:
        form = CategoryForm()
        
    context={
        'form':form
    }
    return render(req,"categoryPage.html",context)


def categorylistPage(req):
    categorylist = categoryModel.objects.all()
    return render(req,"categorylist.html",{'categorylist':categorylist})


def categorytaskPage(req):
    if req.method == 'POST':
        form = CategorytaskForm(req.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = req.user
            task.save()
            return redirect("tasklistPage")
    else:
        form=CategorytaskForm()
    context={
        'form':form
    } 
    return render(req,"categorytaskPage.html",context)


def tasklistPage(req):
    task = TaskModel.objects.all()
    return render(req,"tasklistPage.html",{'task':task})


def deltaskPage(req,del_id):
    deltask=get_object_or_404(TaskModel,id=del_id).delete()
    return redirect('tasklistPage')

def markCompletedPage(req,mark_id):
    marktask=get_object_or_404(TaskModel,id=mark_id)
    marktask.status=("Completed")
    marktask.save()
    return redirect('tasklistPage')


def editTaskPage(req,edit_id):
    edittask=get_object_or_404(TaskModel,id=edit_id)
    if req.method == 'POST':
        form = CategorytaskForm(req.POST,instance=edittask)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = req.user
            task.save()
            return redirect("tasklistPage")
    else:
        form=CategorytaskForm(instance=edittask)
    context={
        'form':form
    } 
    return render(req,"editTaskPage.html",context)


def homePage(req):
    upcoming_task=TaskModel.objects.filter(status = "On_Going",due_date__gt = date.today())
    upcoming_task_count = TaskModel.objects.filter(status="On_Going").count()
    Completed_task_count = TaskModel.objects.filter(status="Completed").count()
    context = {
        'task':upcoming_task,
        'upcoming_task_count':upcoming_task_count,
        'Completed_task_count':Completed_task_count,
    }
    return render(req,"home.html",context)