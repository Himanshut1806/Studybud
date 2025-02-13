from django.shortcuts import render, redirect    # Render used to render a template with the context.Redirect used to redirect the user to another URL.
from django.http import HttpResponse             # HttpResponse used to return a raw HTTP response.
from django.contrib import messages              # messages framework for displaying messages to the user.
from django.contrib.auth import authenticate, login, logout   #authenticate: verifies user credentials.
from .models import Topic                        # This assumes that have a model named 'Topic' deifned in your 'models.py'.
from django.contrib.auth.models import User      # Imports the build-in User model for authentication.
from .models import contactEnquiry               # Imports the contact enquiry models from the current app models.py file.

technologies_list = Topic.objects.all() # filter, get Global Variables : Retrieves all topic objects from the database and assign them to the technologies_list variable.this variable 
                                        # accessible to all the view function in this file,so the technologies can be rendered in all the messages.
#HTML Pages
def home(request):                    # def home (request): Defines the home Views.
    return render(request,'home.html',{'technologies': technologies_list})   # return render : render the home.html template and passess the technologies_list to it. 

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

def TechDetails(request):                   # which displays details for a specific technology.
    context = {}                            # Initializes an empty dictionary to hold context data.
    tech_id = request.GET.get('tech_id')    # Retrieves the value of the 'tech_id' parameter from the GET request (tech_id= 5).
    tech_details = Topic.objects.get(id =tech_id)  # Retrieves the 'Topic' object from the database with the matching ID.
    context['tech_details'] = tech_details
    context['technologies'] = technologies_list
    return render(request,'technology-details.html', context)  # Renders the technology details.html template, passsing the context data.

def addTopics(request):
    if request.method == "POST":                   # Checks if the request method is POST.
        techName = request.POST.get('techName')    # Retrieves the value of the 'techname' field from the POST request.
        techDesc = request.POST.get('techDesc')    # POST.get uses the tuple method () and only POST can use list[] method.
        print(techName, techDesc)
    return render(request,'addTopics.html',{'technologies': technologies_list})

def search(request):
    allTopic= Topic.objects.all()
    params={'allTopic':allTopic}                   # Creates a dictionary params to hold context data,containing all topics..
    return render(request, 'search.html',params)   # Renders the search.html templates,paasing the params dictionary as context.

#Authentications APIs
def signup(request):                             # Handles  user registration.
    if request.method == 'POST':                 # Checks if the request method is POST (a from submission).
        username= request.POST['username']       # Retrieves the username from POST request. 
        FirstName1= request.POST['FirstName1']
        LastName1= request.POST['LastName1']
        Email1= request.POST['Email1']
        Password1= request.POST['Password1']
        Password2= request.POST['Password2']
        if User.objects.filter(username=username).first():  # Checks if a user with the given username already exsists.
            messages.error(request, "User already exist")   # Adds an error message to the message framework.
            return redirect('/')                            # Return redirect to home page.
        
        if Password1 != Password2:
            messages.error(request,"Passwords doesn't match")
            return redirect('/')
# Create user
        myuser= User.objects.create_user(username, Email1, Password1)
        myuser.first_name = FirstName1
        myuser.last_name = LastName1
        myuser.save()
        messages.success(request,"Your account has been created successfully")
        return redirect('/')

    else:
        return HttpResponse('Not Allowed')

def Userlogin(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
       
        user= authenticate(username=username, password=password)  # Authenticates the user using the authenticate function. This checks if the username and password are valid.
        if user is not None:               # Checks if a user was successfully authenticated.
            login(request, user)           # Logs the user in using the login function.
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


def saveEnquiry(request):                    # Handles saving contact enquiries.
    if request.method == 'POST':
        FirstName1= request.POST['FirstName1']
        LastName1= request.POST['LastName1']
        Email1= request.POST['Email1']
        mobileno= request.POST['Mobileno']
        subject= request.POST['subject']
        en=contactEnquiry(firstname=FirstName1,lastname=LastName1,email=Email1,mobileno=mobileno,subject=subject) #insert these data in models
        en.save()                            # Saves the 'contactEnquiry' objects to the database.
    return render(request,'contact.html',{'technologies': technologies_list})  #Render the contact.html passing the technologies_list.This happens regardless of whether the request was a POST request.You probably want to redirect after successfully saving the enquiry or show a success message on the contact.html page.  



 