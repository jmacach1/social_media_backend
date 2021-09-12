from rest_framework import serializers
from .models import Location, Profile, ISeeYaUser, Marker, ISeeYaMap, LocationMap, ProfileMap 
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
  class Meta:
      model = User
      fields = ['id']

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = [ "pk", "city", "stateOrProvince", "country", "lat", "lon" ]
    extra_kwargs = {
      "stateOrProvince" : { "required" : False },
    }

class ProfileSerializer(serializers.ModelSerializer):
  iseeya_user_id = serializers.IntegerField(write_only=True, min_value=1)
  location_id = serializers.IntegerField(write_only=True, min_value=1)

  class Meta:
    model = Profile
    fields = [ 
      "pk", "first_name", "middle_name", "last_name", 
      "profile_image_link", "label", "iseeya_user", 
      "iseeya_user_id", "email", "friends", "location",
      "location_id"
    ]
    extra_kwargs = {
      "middle_name" : { "required" : False },
      "profile_image_link" : { "required" : False },
      "label" : { "required" : False },
    }
    depth = 1

class MarkerSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(required=False, allow_null=True)
  
  class Meta:
    model = Marker
    fields = [ "pk", "type", "location", "profile"]
    depth = 1
    

class ISeeYaMapSerializer(serializers.ModelSerializer):
  markers = MarkerSerializer(read_only=True, many=True)
  owner_id = serializers.IntegerField(write_only=True, min_value=1)
  
  class Meta:
    model = ISeeYaMap
    fields = [ "pk", "type", "name", "owner", "markers", "owner_id" ]
    extra_kwargs = {
      "owner" : { "read_only" : True }
    }

class LocationMapSerializer(serializers.ModelSerializer):
  locations = LocationSerializer(read_only=True, many=True)
  owner_id = serializers.IntegerField(write_only=True, min_value=1)
  
  class Meta:
    model = ISeeYaMap
    fields = [ "pk", "type", "name", "owner", "owner_id", "locations"]
    extra_kwargs = {
      "owner" : { "read_only" : True }
    }

class ProfileMapSerializer(serializers.ModelSerializer):
  profiles = ProfileSerializer(read_only=True, many=True)
  owner_id = serializers.IntegerField(write_only=True, min_value=1)
  
  class Meta:
    model = ISeeYaMap
    fields = [ "pk", "type", "name", "owner", "profiles", "owner_id" ]
    extra_kwargs = {
      "owner" : { "read_only" : True }
    }

class ISeeYaUserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True, required=False)
  iseeya_maps = ISeeYaMapSerializer(read_only=True, many=True)
  location_maps = ISeeYaMapSerializer(read_only=True, many=True)
  profile_maps = ISeeYaMapSerializer(read_only=True, many=True)
  django_auth_user_id = serializers.IntegerField(write_only=True, min_value=1)

  class Meta:
    model = ISeeYaUser
    fields = [ 
      "pk", "django_auth_user", "django_auth_user_id",
      "profile", "iseeya_maps", "location_maps", "profile_maps"
    ]
    depth = 1