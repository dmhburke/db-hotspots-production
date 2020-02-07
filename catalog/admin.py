from django.contrib import admin

# Register your models here.
from catalog.models import Profile, SingleLocationRecord, CleanReviewModel, MasterAddModel, BetaFeedbackModel, Notification, X_checkboxtest

## PROFILE ADMIN - extending USER model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'userpic', 'homecity', 'number_rating',)

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)

## SINGLE LOCATION ADMIN - database of record for FindSpot rankings
class SingleLocationRecordAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'count_ratings',
                    'pf_breakfast',
                    'pf_quick_lunch',
                    'pf_last_min_dinner',
                    'pf_impressing_guests',
                    'pf_date_night',
                    'pf_big_group',
                    'pf_peace_quiet',
                    'pf_living_large',
                    'pf_sunny_days',
                    'count_wishlist',
                    'ave_ratings',
                    'lat',
                    'long',)

# Register the admin class with the associated model
admin.site.register(SingleLocationRecord, SingleLocationRecordAdmin)

## CLEAN REVIEW MODEL - database keeping single (and updatable) instances for USER and SPOTS
class CleanReviewModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'pf_breakfast', 'rating', 'lat', 'long',)

# Register the admin class with the associated model
admin.site.register(CleanReviewModel, CleanReviewModelAdmin)

## CLEAN REVIEW MODEL - database keeping single (and updatable) instances for USER and SPOTS
class MasterAddModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'rating','pf_breakfast', 'lat', 'long',)

# Register the admin class with the associated model
admin.site.register(MasterAddModel, MasterAddModelAdmin)

class BetaFeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback',)

# Register the admin class with the associated model
admin.site.register(BetaFeedbackModel, BetaFeedbackModelAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'body', 'trigger_max', 'trigger_min',)

# Register the admin class with the associated model
admin.site.register(Notification, NotificationAdmin)


# EXPERIMENTS
class X_checkboxtestAdmin(admin.ModelAdmin):
    list_display = ('checkbox1','checkbox2',)

# Register the admin class with the associated model
admin.site.register(X_checkboxtest, X_checkboxtestAdmin)
