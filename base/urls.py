from django.urls import path       # It connects a URL handles the logic for that URL.
from . import views                # for eg views.home would be a function defined in your views.py file.
from django.contrib import admin   # This is build in adminstration interface.

admin.site.site_header = "Web Trends Admin"
admin.site.site_title = "Web Trends Admin Panel"
admin.site.index_title = "Welcome to Web Trends Portal"

urlpatterns = [                    # Thiss list contains all the URL patterns for your application.
    path('',views.home, name="home"),
    path('contact/',views.ContactUs,name="Contact Us"),
    path('saveenquiry/',views.saveEnquiry,name="saveenquiry"),
    path('about/',views.about,name="About"),
    path('tech-details/',views.TechDetails,name="TechDetails"),
    path('webperformance/',views.Webperformance,name="Webperformance"),
    path('webDevelopment/',views.webDevelopment,name="webDevelopment"),
    path('augmentedreality/',views.Augmentedreality,name="Augmentedreality"),
    path('blockchain/',views.Blockchain,name="Blockchain"),
    path('virtualreality/',views.Virtualreality,name="Virtualreality"),
    path('robotics/',views.Robotics,name="Robotics"),
    path('dataanalytics/',views.dataanalytics,name="dataanalytics"),
    path('iotsolutions/',views.iotsolutions,name="iotsolutions"),
    path('machinelearning/',views.machinelearning,name="machinelearning"),
    path('addTopics/',views.addTopics,name="addTopics"),
    path('search/',views.search,name="search"),
    path('signup',views.signup,name="signup"),
    path('login',views.Userlogin,name="Userlogin"),
    path('logout/',views.Userlogout,name="Userlogout"),

]
# contact/= This means that when the user goes to http://www.example.com/contact/,This pattern will match.
# views.contactUS= Specifies the view function (ContactUs in your views.py) that will handle the contact page logic.
# name="Contact US": Assigns the name "Contact Us" to this URL pattern, for use in templates.

# App URLS
# App-level URLs handle routing views within the same application. 
# They are defined in the urls.py file inside the application folder. 
# For example, blog-related URLs might be specified in myproject/blog/urls.py

