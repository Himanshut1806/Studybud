from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Topic
from django.contrib.auth.models import User
from .models import contactEnquiry



technologies_list = Topic.objects.all() # filter, get
#HTML Pages
def home(request):
    return render(request,'home.html',{'technologies': technologies_list})

def ContactUs(request):
    return render(request,'contact.html',{'technologies': technologies_list})

def about(request):
    return render(request,'about.html',{'technologies': technologies_list})

def Webperformance(request):
    return render(request,'webperformance.html',{'technologies': technologies_list})

def webDevelopment(request):
    return render(request,'webDevelopment.html',{'technologies': technologies_list})

def Augmentedreality(request):
    return render(request,'augmentedreality.html',{'technologies': technologies_list})

def Blockchain(request):
    return render(request,'blockchain.html',{'technologies': technologies_list})

def Virtualreality(request):
    return render(request,'virtualreality.html',{'technologies': technologies_list})

def Robotics(request):
    return render(request,'robotics.html',{'technologies': technologies_list})

def dataanalytics(request):
    return render(request,'dataanalytics.html',{'technologies': technologies_list})

def iotsolutions(request):
    return render(request,'iotsolutions.html',{'technologies': technologies_list})

def machinelearning(request):
    return render(request,'machinelearning.html',{'technologies': technologies_list})

def TechDetails(request):
    context = {}
    tech_id = request.GET.get('tech_id')
    tech_details = Topic.objects.get(id =tech_id)
    context['tech_details'] = tech_details
    context['technologies'] = technologies_list
    return render(request,'technology-details.html', context)

def addTopics(request):
    if request.method == "POST":
        techName = request.POST.get('techName')
        techDesc = request.POST.get('techDesc')
        print(techName, techDesc, "09090909")
    return render(request,'addTopics.html',{'technologies': technologies_list})

def search(request):
    allTopic= Topic.objects.all()
    params={'allTopic':allTopic}
    return render(request, 'search.html',params)

#Authentications APIs
def signup(request):
    if request.method == 'POST':
        username= request.POST['username']
        FirstName1= request.POST['FirstName1']
        LastName1= request.POST['LastName1']
        Email1= request.POST['Email1']
        Password1= request.POST['Password1']
        Password2= request.POST['Password2']
        if User.objects.filter(username=username).first():
            messages.error(request, "User already exist")
            return redirect('/')
        
        if Password1 != Password2:
            messages.error(request,"Passwords doesn't match")
            return redirect('/')
# Create user
        myuser= User.objects.create_user(username, Email1, Password1)
        myuser.first_name = FirstName1
        myuser.last_name = LastName1
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse('Not Allowed')

def Userlogin(request):
    if request.method == 'POST':

        username= request.POST['username']
        password= request.POST['password']
       
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/')
        
    return HttpResponse('404 - Not Found')

def Userlogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')


def saveEnquiry(request):
    if request.method == 'POST':
        print("Post request is working")
        FirstName1= request.POST['FirstName1']
        LastName1= request.POST['LastName1']
        Email1= request.POST['Email1']
        mobileno= request.POST['Mobileno']
        subject= request.POST['subject']
        en=contactEnquiry(firstname=FirstName1,lastname=LastName1,email=Email1,mobileno=mobileno,subject=subject) #insert these data in models
        en.save()
    return render(request,'contact.html',{'technologies': technologies_list})
