from django.contrib import admin

from .models import Stock, User, TargetAllocation

# Register your models here.
admin.site.register(Stock)
admin.site.register(User)
admin.site.register(TargetAllocation)
