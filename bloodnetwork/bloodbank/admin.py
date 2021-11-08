from django.contrib import admin

from bloodbank.models import Category, bloodbank,Donor


# Register your models here.
admin.site.register (bloodbank)
admin.site.register (Category)
admin.site.register (Donor)