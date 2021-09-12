from django.contrib import admin
from .models import Location, Profile, ISeeYaUser, ISeeYaMap, Marker, LocationMap, ProfileMap

admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(ISeeYaUser)
admin.site.register(ISeeYaMap)
admin.site.register(Marker)
admin.site.register(LocationMap)
admin.site.register(ProfileMap)
