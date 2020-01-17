from django.urls import path
from . import views

urlpatterns = [
    # Login pages
    path('createaccount', views.createaccount, name='createaccount'),
    path('login', views.login, name='login'),
    # Add spots (also Home page :: landing page post-login)
    path('', views.landingadd, name='home'),
    path('adddetail/<name>/<lat>/<lng>', views.adddetail, name='adddetail'),
    # Find spots
    path('findspots', views.findspot, name='findspot'),
    # Browse spots
    path('browsespots', views.browsespots, name='browsespots'),
    #Spot detail
    path('spotfulldetail/<name>/<city>', views.spotfulldetail, name='spotfulldetail'),
    #User profile page
    path('profile/<user>', views.userprofile, name='userprofile'),
    path('profile/<user>/response', views.userprofileresponse, name='userprofileresponse'),

]
