import os
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.db.models import Sum, Count, Max
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from catalog.choices import *

# Import for Profile image rotation
from io import BytesIO
from django.core.files import File
from PIL import ExifTags
from PIL import Image as Img

#PROFILE MODEL - extends USER model with userpic and homecity
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, blank=True, null=True)
    userpic = models.ImageField(upload_to='profilepictures', blank=True, null=True)
    homecity = models.CharField(max_length=30, blank=True, null=True)
    number_rating = models.IntegerField(blank=True, null=True)
    high_rating = models.CharField(max_length=45, blank=True, null=True)
    last_rating = models.CharField(max_length=45, blank=True, null=True)

    def get_user_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('userdetail', args=[str(self.user)])

    def __str__(self):
        return '%s' % self.user

    def save(self, *args, **kwargs):
        try:
            if self.userpic:
                pilImage = Img.open(BytesIO(self.userpic.read()))
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break
                exif = dict(pilImage._getexif().items())

                if exif[orientation] == 3:
                    pilImage = pilImage.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    pilImage = pilImage.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    pilImage = pilImage.rotate(90, expand=True)

                output = BytesIO()
                pilImage.save(output, format='JPEG', quality=75)
                output.seek(0)
                self.userpic = File(output, self.userpic.name)
        except (AttributeError, KeyError, IndexError):
            # cases: image don't have getexif
            pass

        return super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

## MASTER ADD - Creates record for every entry submitted through form (will include multiple for user and spots)
class MasterAddModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60) # blank=True, null=True
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    # START Perfect_for criteria
    pf_breakfast = models.BooleanField(default=False)
    pf_quick_lunch = models.BooleanField(default=False)
    pf_last_min_dinner = models.BooleanField(default=False)
    pf_impressing_guests = models.BooleanField(default=False)
    pf_date_night = models.BooleanField(default=False)
    pf_big_group = models.BooleanField(default=False)
    pf_peace_quiet = models.BooleanField(default=False)
    pf_living_large = models.BooleanField(default=False)
    pf_sunny_days = models.BooleanField(default=False)
    # END Perfect_for criteria
    notes = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30,blank=True, null=True)
    country = models.CharField(max_length=30,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    category1 = models.CharField(max_length=30,blank=True, null=True)
    category2 = models.CharField(max_length=30,blank=True, null=True)
    category3 = models.CharField(max_length=30,blank=True, null=True)
    postcode = models.CharField(max_length=30,blank=True, null=True)
    suburb = models.CharField(max_length=30,blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    long = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s' % self.name

## CLEAN ADD - Creates record for user and spot that can be overwritten with latest data
class CleanReviewModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60) # blank=True, null=True
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    # START Perfect_for criteria
    pf_breakfast = models.BooleanField(default=False)
    pf_quick_lunch = models.BooleanField(default=False)
    pf_last_min_dinner = models.BooleanField(default=False)
    pf_impressing_guests = models.BooleanField(default=False)
    pf_date_night = models.BooleanField(default=False)
    pf_big_group = models.BooleanField(default=False)
    pf_peace_quiet = models.BooleanField(default=False)
    pf_living_large = models.BooleanField(default=False)
    pf_sunny_days = models.BooleanField(default=False)
    # END Perfect_for criteria
    notes = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30,blank=True, null=True)
    country = models.CharField(max_length=30,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    category1 = models.CharField(max_length=30,blank=True, null=True)
    category2 = models.CharField(max_length=30,blank=True, null=True)
    category3 = models.CharField(max_length=30,blank=True, null=True)
    postcode = models.CharField(max_length=30,blank=True, null=True)
    suburb = models.CharField(max_length=30,blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    long = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    # ave_rating = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    # count_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

@receiver(post_save, sender=MasterAddModel)
def build_clean(sender, instance, **kwargs):

    CleanReviewModel.objects.update_or_create(
    name=instance.name,
    user=instance.user,
    defaults = {
    'rating': instance.rating,
    'pf_breakfast': instance.pf_breakfast,
    'pf_quick_lunch': instance.pf_quick_lunch,
    'pf_last_min_dinner': instance.pf_last_min_dinner,
    'pf_impressing_guests': instance.pf_impressing_guests,
    'pf_date_night': instance.pf_date_night,
    'pf_big_group': instance.pf_big_group,
    'pf_peace_quiet': instance.pf_peace_quiet,
    'pf_living_large': instance.pf_living_large,
    'pf_sunny_days': instance.pf_sunny_days,
    'notes': instance.notes,
    'city': instance.city,
    'country': instance.country,
    'address': instance.address,
    'category1': instance.category1,
    'category2': instance.category2,
    'category3': instance.category3,
    'postcode': instance.postcode,
    'suburb': instance.suburb,
    'lat': instance.lat,
    'long': instance.long,
    'date': instance.date,
    })

class SingleLocationRecord(models.Model):
    name = models.CharField(max_length=60) # blank=True, null=True
    # START Perfect_for criteria
    pf_breakfast = models.IntegerField(blank=True, null=True)
    pf_quick_lunch = models.IntegerField(blank=True, null=True)
    pf_last_min_dinner = models.IntegerField(blank=True, null=True)
    pf_impressing_guests = models.IntegerField(blank=True, null=True)
    pf_date_night = models.IntegerField(blank=True, null=True)
    pf_big_group = models.IntegerField(blank=True, null=True)
    pf_peace_quiet = models.IntegerField(blank=True, null=True)
    pf_living_large = models.IntegerField(blank=True, null=True)
    pf_sunny_days = models.IntegerField(blank=True, null=True)
    # END Perfect_for criteria
    notes = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30,blank=True, null=True)
    country = models.CharField(max_length=30,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    category1 = models.CharField(max_length=30,blank=True, null=True)
    category2 = models.CharField(max_length=30,blank=True, null=True)
    category3 = models.CharField(max_length=30,blank=True, null=True)
    postcode = models.CharField(max_length=30,blank=True, null=True)
    suburb = models.CharField(max_length=30,blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    count_ratings = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    count_wishlist = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    ave_ratings = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    long = models.CharField(max_length=100, blank=True, null=True)

@receiver(post_save, sender=CleanReviewModel)
def build_single(sender, instance, **kwargs):

    count_pf_breakfast = CleanReviewModel.objects.filter(name=instance.name, pf_breakfast=True).count()
    count_pf_quick_lunch = CleanReviewModel.objects.filter(name=instance.name, pf_quick_lunch=True).count()
    count_pf_last_min_dinner = CleanReviewModel.objects.filter(name=instance.name, pf_last_min_dinner=True).count()
    count_pf_impressing_guests = CleanReviewModel.objects.filter(name=instance.name, pf_impressing_guests=True).count()
    count_pf_date_night = CleanReviewModel.objects.filter(name=instance.name, pf_date_night=True).count()
    count_pf_big_group = CleanReviewModel.objects.filter(name=instance.name, pf_big_group=True).count()
    count_pf_peace_quiet = CleanReviewModel.objects.filter(name=instance.name, pf_peace_quiet=True).count()
    count_pf_living_large = CleanReviewModel.objects.filter(name=instance.name, pf_living_large=True).count()
    count_pf_sunny_days = CleanReviewModel.objects.filter(name=instance.name, pf_sunny_days=True).count()

    count_wishlist = CleanReviewModel.objects.filter(name=instance.name, rating=None).count()
    count_ratings = CleanReviewModel.objects.filter(name=instance.name, rating__gte=1).count()
    sum_ratings = list(CleanReviewModel.objects.filter(name=instance.name).aggregate(Sum('rating')).values())[0]
    try:
        ave_ratings = sum_ratings / count_ratings
    except:
        ave_ratings = None

    SingleLocationRecord.objects.update_or_create(
    name=instance.name,
    defaults = {
    'pf_breakfast': count_pf_breakfast,
    'pf_quick_lunch': count_pf_quick_lunch,
    'pf_last_min_dinner': count_pf_last_min_dinner,
    'pf_impressing_guests': count_pf_impressing_guests,
    'pf_date_night': count_pf_date_night,
    'pf_big_group': count_pf_big_group,
    'pf_peace_quiet': count_pf_peace_quiet,
    'pf_living_large': count_pf_living_large,
    'pf_sunny_days': count_pf_sunny_days,
    'notes': instance.notes,
    'city': instance.city,
    'country': instance.country,
    'address': instance.address,
    'category1': instance.category1,
    'category2': instance.category2,
    'category3': instance.category3,
    'postcode': instance.postcode,
    'suburb': instance.suburb,
    'date': instance.date,
    'count_ratings': count_ratings,
    'count_wishlist': count_wishlist,
    'ave_ratings': ave_ratings,
    })

@receiver(post_save, sender=MasterAddModel)
def add_lat_long(sender, instance, **kwargs):

    SingleLocationRecord.objects.update_or_create(
    name=instance.name,
    defaults = {
    'lat': instance.lat,
    'long': instance.long,
    })

class BetaFeedbackModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200, blank=True, null=True)

class Notification(models.Model):
    name = models.CharField(max_length=35, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image_link = models.CharField(max_length=200, null=True)
    trigger_min = models.IntegerField(blank=True, null=True)
    trigger_max = models.IntegerField(blank=True, null=True)

class X_checkboxtest(models.Model):
    checkbox1 = models.BooleanField(default=False)
    checkbox2 = models.BooleanField(default=False)
