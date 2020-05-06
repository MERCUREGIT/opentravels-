from django.contrib import admin
from .models import trip_data,  join_trip,Trip_Comments

# Register your models here.

admin.site.register(trip_data)
admin.site.register(join_trip)
admin.site.register(Trip_Comments)
