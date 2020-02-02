from django.contrib import admin

# Register your models here.
from catalog.models import Profile, SingleLocationRecord, CleanReviewModel, MasterAddModel, BetaFeedbackModel#, UserNotification

## PROFILE ADMIN - extending USER model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'userpic', 'homecity', 'number_rating',)

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)

## SINGLE LOCATION ADMIN - database of record for FindSpot rankings
class SingleLocationRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_ratings', 'count_wishlist', 'ave_ratings', 'lat', 'long',)

# Register the admin class with the associated model
admin.site.register(SingleLocationRecord, SingleLocationRecordAdmin)

## CLEAN REVIEW MODEL - database keeping single (and updatable) instances for USER and SPOTS
class CleanReviewModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'rating', 'lat', 'long',)

# Register the admin class with the associated model
admin.site.register(CleanReviewModel, CleanReviewModelAdmin)

## CLEAN REVIEW MODEL - database keeping single (and updatable) instances for USER and SPOTS
class MasterAddModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'rating','lat', 'long',)

# Register the admin class with the associated model
admin.site.register(MasterAddModel, MasterAddModelAdmin)

class BetaFeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback',)

# Register the admin class with the associated model
admin.site.register(BetaFeedbackModel, BetaFeedbackModelAdmin)

# class UserNotificationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'notification',)
#
# # Register the admin class with the associated model
# admin.site.register(UserNotification, UserNotificationAdmin)
