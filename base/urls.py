from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "Web Trends Admin"
admin.site.site_title = "Web Trends Admin Panel"
admin.site.index_title = "Welcome to Web Trends Portal"

urlpatterns = [
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
