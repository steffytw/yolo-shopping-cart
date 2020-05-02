from django.contrib import admin
from . models import userRegistration,productInformation

# Register your models here.
admin.site.register(userRegistration)
admin.site.register(productInformation)