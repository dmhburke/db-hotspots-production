from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q, Max
from django.urls import reverse
import json, requests
from hotSpotsApp.settings import *
from opencage.geocoder import OpenCageGeocode
from pprint import pprint
from operator import itemgetter
from decimal import Decimal

#Import User model here
from django.contrib.auth.models import User

#Import custom models here
from catalog.models import CleanReviewModel, SingleLocationRecord, MasterAddModel

#Import forms here
from catalog.forms import ProfileForm, AddSpotsForm, MasterAddForm, SpotFinderForm, BetaFeedbackForm

## CREATE NEW ACCOUNT using Profile form and model
def createaccount (request):
    """Create user account"""
# Add view details here
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.userpic = form.cleaned_data.get('userpic')
            user.profile.homecity = form.cleaned_data.get('homecity')
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = ProfileForm()

    return render(request, 'createaccount.html', {'form': form})

## Search FOURSQUARE API for new spots
@login_required
def landingadd(request):

    logged_in_user = request.user
    user_city = logged_in_user.profile.homecity

    search_result = {}
    if 'name' in request.POST:
          form = AddSpotsForm(request.POST)
          if form.is_valid():
              search_result = form.search(request)
    else:
          form = AddSpotsForm(initial={'city': user_city})

    context={
    'form': form,
    'search_result': search_result,
    }

    return render(request, 'landingadd.html', context=context)

## Combine FOURSQUARE API with GOOGLE API to add spot to review or wishlist
@login_required
def adddetail(request, name, lat, lng):

####FOURSQUARE API####
    lat = lat
    long = lng
    targetLocation = str(lat) + ', ' + str(long)

    detailsURL = 'https://api.foursquare.com/v2/venues/suggestcompletion'
    detailsParams = dict(
        client_id='0PR1PTLMSLBM0ORYW5U2YGL43IOZXFVKWFIC2DHHXOP30Z35',
        client_secret='SJDG5K1D5NARSRZYAAYPJMTJBPIGW4ONUTQBT4HTDNUGSLQQ',
         v='20180323',
         ll=targetLocation,
         query=name,
         limit=10,
         )
    detailsResponse = requests.get(url=detailsURL, params=detailsParams)
    detailsData = detailsResponse.json()
    detailsStatus = detailsResponse.status_code
    detailsInfo = json.loads(detailsResponse.text)

    detailsResult = detailsInfo['response']['minivenues'][0]
    resultName = detailsResult['name']
    try:
        resultAddress = detailsResult['location']['address']
    except:
        resultAddress = ''
    try:
        resultCity = detailsResult['location']['city']
    except:
        resultCity = ''
    try:
        resultCountry = detailsResult['location']['country']
    except:
        resultCountry = ''
    try:
        resultCategory1 = detailsResult['categories'][0]['name']
    except:
        resultCategory1 = ""
    try:
        resultCategory2 = detailsResult['categories'][1]['name']
    except:
        resultCategory2 = ""
    try:
        resultCategory3 = detailsResult['categories'][2]['name']
    except:
        resultCategory3 = ""
    try:
        resultPostcode = detailsResult['location']['postalCode']
    except:
        resultPostcode = ""

    imageQuery = resultName + " " + resultAddress

####GOOGLE IMAGE API ######
    searchURL = 'https://www.googleapis.com/customsearch/v1'
    searchParams = dict(
        cx=google_project_cx,
        key=google_dev_api_key,
        q=imageQuery,
        searchType='image',
        fileType='.jpg',
        num=6,
    )

    searchResponse = requests.get(url=searchURL, params=searchParams)
    searchStatus = searchResponse.status_code
    searchData = searchResponse.json()
    searchInfo = json.loads(searchResponse.text)

    try:
        imageResult = searchInfo['items']
    except:
        imageResult = None

###ADD ADDITIONAL LOCATION DETAILS####
    key = 'a98d10680c0c41d082d9de1c23dcec22'
    geocoder = OpenCageGeocode(key)

    locationResponse = geocoder.reverse_geocode(lat, long)

    try:
        resultSuburb = locationResponse[0]['components']['suburb']
    except:
        resultSuburb = ''

####FORM FOR USERS INPUTS ####
    if request.method == 'POST':
        form = MasterAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.name = resultName
            post.city = resultCity
            post.address = resultAddress
            post.category1 = resultCategory1
            post.category2 = resultCategory2
            post.category3 = resultCategory3
            post.postcode = resultPostcode
            post.suburb = resultSuburb
            post.lat = lat
            post.long = long
            post.save()
            return redirect('browsespots') #or whatever the url
    else:
        form = MasterAddForm()

    friends_here = CleanReviewModel.objects.filter(name=name).exclude(user=request.user).count()

    context = {
    'form': form,
    'name': name,
    'targetLocation': targetLocation,
    'detailsData': detailsData,
    'resultName': resultName,
    'resultCity': resultCity,
    'resultCountry': resultCountry,
    'resultAddress': resultAddress,
    'resultCategory1': resultCategory1,
    'resultCategory2': resultCategory2,
    'resultCategory3': resultCategory3,
    'resultPostcode': resultPostcode,
    'searchStatus': searchStatus,
    'imageResult': imageResult,
    'searchData': searchData,
    'resultSuburb': resultSuburb,
    'searchStatus': searchStatus,
    'searchData': searchData,
    'friends_here': friends_here,
    'resultName': resultName,
    }

    return render(request, 'adddetail.html', context=context)

@login_required
def findspot(request):

##Define user and city
    logged_in_user = request.user
    user_city = logged_in_user.profile.homecity

    situation_result = {}
    category_result = {}
    location_result = {}
    # source_result = {}

    if request.method =='POST':
         form = SpotFinderForm(request.POST)
         if form.is_valid():
             category_result = form.category_query(request)
             situation_result = form.situation_query(request)
             location_result = form.location_query(request)
             # source_result = form.source_query(request)
    else:
          form = SpotFinderForm(initial={
          'location': user_city,
          })

## -- LOCATION RESULTS --
    postcode_result1 = {}
    postcode_result2 = {}
    postcode_result3 = {}
    postcode_result4 = {}

    if location_result == "Los Angeles, CA":
        postcode_result1 = 90
        postcode_result2 = 90
        postcode_result3 = 90
        postcode_result4 = 90
    elif location_result == "New York City, NY":
        postcode_result1 = 1
        postcode_result2 = 1
        postcode_result3 = 1
        postcode_result4 = 1
    elif location_result == "London, UK":
        postcode_result1 = "N"
        postcode_result2 = "E"
        postcode_result3 = "W"
        postcode_result4 = "S"
    elif location_result == "Seattle, WA":
        postcode_result1 = 98
        postcode_result2 = 98
        postcode_result3 = 98
        postcode_result4 = 98
    elif location_result == "Sydney, Australia":
        postcode_result1 = 20
        postcode_result2 = 21
        postcode_result3 = 22
        postcode_result4 = 25
    else:
        postcode_result1 = ""
        postcode_result2 = ""
        postcode_result3 = ""
        postcode_result4 = ""

## -- TYPE RESULTS --

    optioncategory1_result = {}
    optioncategory2_result = {}
    optioncategory3_result = {}

    if category_result == "FOOD":
        optioncategory1_result = "Restaurant"
        optioncategory2_result = "Food"
        optioncategory3_result = "Café"
    elif category_result == "COFFEE":
        optioncategory1_result = "Café"
        optioncategory2_result = "Coffee shop"
        optioncategory3_result = "Coffee shop"
    elif category_result == "WINE":
        optioncategory1_result = "Wine"
        optioncategory2_result = "Wine"
        optioncategory3_result = "Wine"
    elif category_result == "BEER":
        optioncategory1_result = "Beer"
        optioncategory2_result = "Pub"
        optioncategory3_result = "Gastropub"
    elif category_result == "COCKTAILS":
        optioncategory1_result = "Cocktail"
        optioncategory2_result = "Bar"
        optioncategory3_result = "Nightlife"
    else:
        optioncategory1_result = ""
        optioncategory2_result = ""
        optioncategory3_result = ""

## ratings details
    your_rating = CleanReviewModel.objects.filter(user=request.user)

## SEARCH RESULT TO FIND ALL RESULTS
    spot_finder = SingleLocationRecord.objects.filter(
               (Q(postcode__startswith=postcode_result1) | Q(postcode__startswith=postcode_result2) | Q(postcode__startswith=postcode_result3) | Q(postcode__startswith=postcode_result4)) &
               Q(perfect_for__contains=situation_result) &
               (Q(category1__contains=optioncategory1_result) | Q(category1__contains=optioncategory2_result) | Q(category1__contains=optioncategory3_result)
               ))

## HOTSPOTS RANKING ALGORITHM TO RANK RELEVANT RESULTS
    hotspots_rank = {}

    def hotspots_rank_score(name):

        # Variables for calculations
        par_review_score = Decimal(3.00)
        review_kicker_quotient = Decimal(0.10)
        wishlist_kicker_quotient = Decimal(3.5)

        # Check if anyone has rated and add crowd_kicker_review
        try:
            average_score = SingleLocationRecord.objects.get(name=name).ave_ratings # e.g. 5
            net_average_score = Decimal(average_score - par_review_score) #e.g 2
            count_reviews = SingleLocationRecord.objects.get(name=name).count_ratings #e.g. 1
            crowd_kicker_review = (net_average_score*review_kicker_quotient)*count_reviews # e.g. 2*0.1*1=0.2
        except:
            average_score = Decimal(0.00)
            crowd_kicker_review = Decimal(0.00)

        # Check if anyone has added to wishlist
        try:
            count_wishlist = SingleLocationRecord.objects.get(name=name).count_wishlist # should be zero if none
        except:
            count_wishlist = 0

        if count_wishlist > 0:
            crowd_kicker_wishlist = Decimal(wishlist_kicker_quotient + (count_wishlist*(wishlist_kicker_quotient/10)))
        else:
            crowd_kicker_wishlist = Decimal(0.00)

        # Check if user has rated
        try:
            user_rating = CleanReviewModel.objects.get(user=request.user, name=name).rating
        except:
            user_rating = False

        #Calculate hotspots_rank_quotient if either user has rated or not rated
        if user_rating:
            hotspots_rank_quotient = user_rating + crowd_kicker_review + crowd_kicker_wishlist
        else:
            hotspots_rank_quotient = average_score + crowd_kicker_review + crowd_kicker_wishlist

        return hotspots_rank_quotient

    # This for loop assigns a hotspots_rank_score to each result from the spot_finder query set
    print("<<RESULTS DICTIONARY>>")
    for spot in spot_finder:
        hotspots_rank_result = hotspots_rank_score(spot.name)
        hotspots_rank[spot] = hotspots_rank_result ## ADD/DELETE .NAME FOR TERMINAL/TEMPLATE

    hotspots_rank_ranked = {}

    for name, score in sorted(hotspots_rank.items(), key=lambda item: item[1], reverse=True):
        hotspots_rank_ranked[name] = score
        print ("%s: %.2f" % (name, score))

    print("<<RANKED DICTIONARY>>")
    print(hotspots_rank_ranked)

    #GET ALL PEOPLE WHO'VE BEEN TO SPOT
    friends_whove_been = CleanReviewModel.objects.all().order_by("-date")

    context = {
    'form': form,
    'spot_finder': spot_finder,
    'postcode_result': postcode_result1,
    'optioncategory1_result': optioncategory1_result,
    'situation_result': situation_result,
    'logged_in_user': logged_in_user,
    'hotspots_rank_ranked': hotspots_rank_ranked,
    'friends_whove_been': friends_whove_been,
    'your_rating': your_rating,
    }

    return render(request, 'findspots.html', context=context)

@login_required
def browsespots(request):
    """View to browse yours, wishlist and activity"""

    activity_stream = CleanReviewModel.objects.all().order_by('-date')

    your_spots = CleanReviewModel.objects.filter(user=request.user, rating__gte=0).order_by("-rating", "-date")

    your_wishlist = CleanReviewModel.objects.filter(user=request.user, rating=None).order_by("-date")

    context={
    'activity_stream': activity_stream,
    'your_spots': your_spots,
    'your_wishlist': your_wishlist,
    }

    return render(request,'browsespots.html', context=context)

def spotfulldetail(request, name, city):
    # DEFINE USER
    user = request.user

    # IMAGE CAROUSEL
    imageQuery = name + " " + city


    searchURL = 'https://www.googleapis.com/customsearch/v1'
    searchParams = dict(
        cx=google_project_cx,
        key=google_dev_api_key,
        q=imageQuery,
        searchType='image',
        fileType='.jpg',
        num=6,
    )

    searchResponse = requests.get(url=searchURL, params=searchParams)
    searchStatus = searchResponse.status_code
    searchData = searchResponse.json()
    searchInfo = json.loads(searchResponse.text)

    imageResult = searchInfo['items']

    #REVIEW DETAILS
    numberVisits = CleanReviewModel.objects.filter(name=name).exclude(user=request.user).count()
    countRatings = CleanReviewModel.objects.filter(name=name).exclude(rating=None).count()
    numberReviews = SingleLocationRecord.objects.filter(name=name).count()
    ave_rating = SingleLocationRecord.objects.get(name=name).ave_ratings

    try:
        your_rating = CleanReviewModel.objects.get(name=name, user=user).rating
    except:
        your_rating = None

    # SPOT DETAILS FOR VIEW RENDERING
    address = SingleLocationRecord.objects.get(name=name).address
    lat = SingleLocationRecord.objects.get(name=name).lat
    long = SingleLocationRecord.objects.get(name=name).long

    # GENERATES REVCHRON LIST OF PAST REVIEWS FOR TARGET SPOT
    review_list = MasterAddModel.objects.filter(name=name).order_by('-date')

    waitlist_or_none = CleanReviewModel.objects.filter(user=request.user, name=name).count()

    context = {
    'name': name,
    'city': city,
    'imageResult': imageResult,
    'address': address,
    'numberReviews': numberReviews,
    'numberVisits': numberVisits,
    'countRatings': countRatings,
    'ave_rating': ave_rating,
    'your_rating': your_rating,
    'lat': lat,
    'long': long,
    'review_list': review_list,
    'waitlist_or_none': waitlist_or_none,
    }

    return render(request, 'spotfulldetail.html',context=context)

@login_required
def userprofile(request, user):

    user = request.user
    first_name = user.get_short_name()
    full_name = user.get_full_name()

    if request.method == 'POST':
        form = BetaFeedbackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.feedback = post.feedback
            post.save()
            return redirect('userprofileresponse', user=user) #or whatever the url
    else:
        form = BetaFeedbackForm()

    context = {
        'user': user,
        'first_name': first_name,
        'full_name': full_name,
        'form': form,
    }

    return render(request, 'userprofile.html', context=context)

@login_required
def userprofileresponse(request, user):

    user = request.user
    first_name = user.get_short_name()
    full_name = user.get_full_name()

    context = {
        'user': user,
        'first_name': first_name,
        'full_name': full_name,
    }

    return render(request, 'userprofileresponse.html', context=context)
