from django.contrib import admin

from .models import *

admin.site.register(Patient)
admin.site.register(Address)
admin.site.register(GridCoordinate)
admin.site.register(DateBetween)
admin.site.register(Category)
admin.site.register(Detail)
admin.site.register(Location)


