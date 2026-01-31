from django.contrib import admin
from .models import AppUser,CarModel,Car,Advertisement,UserProfiles

admin.site.register([UserProfiles])
admin.site.register([AppUser])
admin.site.register([Car])
admin.site.register([CarModel])
admin.site.register([Advertisement])


