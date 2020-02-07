from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.choices import *
import json, requests
from django.contrib.gis.geoip2 import GeoIP2

from catalog.models import MasterAddModel, BetaFeedbackModel, X_checkboxtest

#  Extends standard USER form to add userpic and homecity
class ProfileForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)
    userpic = forms.ImageField(required=True)
    homecity = forms.ChoiceField(choices=CITIES, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'userpic', 'homecity',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

# Powers Find Spots search
class AddSpotsForm(forms.Form):
    city = forms.ChoiceField(choices=CITIES, required=True)
    name = forms.CharField()

    def search(self, request):
        completeQuery = self.cleaned_data['name']
        selectedLocation = self.cleaned_data['city']

        formURL = 'https://api.foursquare.com/v2/venues/suggestcompletion'
        formParams = dict(
            client_id='0PR1PTLMSLBM0ORYW5U2YGL43IOZXFVKWFIC2DHHXOP30Z35',
            client_secret='SJDG5K1D5NARSRZYAAYPJMTJBPIGW4ONUTQBT4HTDNUGSLQQ',
            v='20180323',
            near= selectedLocation, #currentLocation
            query=completeQuery,
            limit=10,
        )

        formResponse = requests.get(url=formURL, params=formParams)
        formStatus = formResponse.status_code
        formDetails = formResponse.content
        formData = formResponse.json()

        return formData

        def get_apiresult_url(self):
             """Returns the url to access a particular instance of the search result"""
             return reverse('testpagedetail', args=[str(self.name)])

# Powers HotSpot reviews within ADDDETAIL view
class MasterAddForm(ModelForm):
    rating = forms.TypedChoiceField(choices=RATING, required=False, empty_value=None)
    pf_breakfast = forms.BooleanField(required=False)
    pf_quick_lunch = forms.BooleanField(required=False)
    pf_last_min_dinner = forms.BooleanField(required=False)
    pf_impressing_guests = forms.BooleanField(required=False)
    pf_date_night = forms.BooleanField(required=False)
    pf_big_group = forms.BooleanField(required=False)
    pf_peace_quiet = forms.BooleanField(required=False)
    pf_living_large = forms.BooleanField(required=False)
    pf_sunny_days = forms.BooleanField(required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":30}), required=False)

    class Meta:
        model = MasterAddModel
        fields = ('rating', 'pf_breakfast',
        'pf_quick_lunch',
        'pf_last_min_dinner',
        'pf_impressing_guests',
        'pf_date_night',
        'pf_big_group',
        'pf_peace_quiet',
        'pf_living_large',
        'pf_sunny_days',
        'notes',)

# Powers HotSpot search from database based on certain criteria
class SpotFinderForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY, required=False)
    situation = forms.ChoiceField(choices=SITUATION, required=False)
    location = forms.ChoiceField(choices=CITY, required=False)
    # source = forms.ChoiceField(choices=SOURCE, required=False)

    def category_query(self,request):
        categoryQuery = self.cleaned_data['category']
        return categoryQuery

    def situation_query(self,request):
        situationQuery = self.cleaned_data['situation']
        return situationQuery

    def location_query(self,request):
        locationQuery = self.cleaned_data['location']
        return locationQuery

    # def source_query(self,request):
    #     sourceQuery = self.cleaned_data['source']
    #     return sourceQuery

class BetaFeedbackForm(ModelForm):
    feedback = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":25}), required=False)

    class Meta:
        model = BetaFeedbackModel
        fields = ('feedback',)

class X_checkboxtestForm(ModelForm):
    checkbox1 = forms.BooleanField(required=False)
    checkbox2 = forms.BooleanField(required=False)

    class Meta:
        model = X_checkboxtest
        fields = ('checkbox1', 'checkbox2',)
