from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Location, Profile, ISeeYaUser, Marker, ISeeYaMap, LocationMap, ProfileMap
from .serializers import LocationSerializer, ProfileSerializer, MarkerSerializer, ISeeYaUserSerializer, ISeeYaMapSerializer, LocationMapSerializer, ProfileMapSerializer

from rest_framework.authtoken.models import Token

ADDRESS = "address"
PROFILE = "profile"
ROBOHASH_URL = "https://robohash.org/"
DUMMY_LOCATION_ID = 10

@api_view(['POST'])
def createIseeYaUser(request):
  key = request.data["key"]
  user = Token.objects.get(key=key).user
  data = {
    "django_auth_user" : user.id
  }
  serializer = ISeeYaUserSerializer(data=data)
  if serializer.is_valid():
    serializer.save()  
    print(serializer.validated_data)

  return Response({
    "message": "Got some data!", 
    "key" : key,
    "user" : user.id,
    "serializer.data" : serializer.data,
  })

@api_view(['POST'])
def get_iseeya_user(request):
  key = request.data["key"]
  user = Token.objects.get(key=key).user
  iseeya_user = ISeeYaUser.objects.get(django_auth_user=user)
  serializer = ISeeYaUserSerializer(iseeya_user)
  return Response(serializer.data)

##########  ##########

# ISeeYaUser
class ISeeYaUserList(generics.CreateAPIView):
  queryset = ISeeYaUser.objects.all()
  serializer_class = ISeeYaUserSerializer

  def create(self, request, *args, **kwargs):
    key = request.data["key"]
    user = Token.objects.get(key=key).user
    email = user.email
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    location_id = request.data["location_id"]

    serializer = ISeeYaUserSerializer(data={ "django_auth_user_id" : user.id })
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    iseeya_user = serializer.data
    iseeya_user_pk = iseeya_user["pk"]
    print(iseeya_user_pk)

    profile_data = {
      "first_name" : first_name,
      "last_name" : last_name,
      "email" : email,
      "profile_image_link" : ROBOHASH_URL + email.split("@")[0],
      "iseeya_user_id" : iseeya_user_pk,
      "label" : f"{first_name} {last_name}",
      "location_id" : location_id
    }
    profileSerializer = ProfileSerializer(data=profile_data)
    profileSerializer.is_valid(raise_exception=True)
    profileSerializer.save()

    address_map_data = {
      "type" :  ADDRESS,
      "name" : "Places I've Lived",
      "owner_id" : iseeya_user_pk
    }
    addressMapSerializer = ISeeYaMapSerializer(data=address_map_data)
    addressMapSerializer.is_valid(raise_exception=True)
    addressMapSerializer.save()

    friends_map_data = {
      "type" :  PROFILE,
      "name" : "Friends",
      "owner_id" : iseeya_user_pk
    }
    friendsMapSerializer = ISeeYaMapSerializer(data=friends_map_data)
    friendsMapSerializer.is_valid(raise_exception=True)
    friendsMapSerializer.save()

    headers = self.get_success_headers(serializer.data)
    return Response({
      "iseeya_user" : serializer.data,
      "status" : status.HTTP_201_CREATED, 
      "headers" : headers
    })

class ISeeYaUserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = ISeeYaUser.objects.all()
  serializer_class = ISeeYaUserSerializer

# location
class LocationList(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

# profile
class ProfileList(generics.ListCreateAPIView):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

# Marker
class MarkerList(generics.ListCreateAPIView):
  queryset = Marker.objects.all()
  serializer_class = MarkerSerializer

class MarkerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Marker.objects.all()
  serializer_class = MarkerSerializer

# ISeeYaMap
class ISeeYaMapList(generics.ListCreateAPIView):
  queryset = ISeeYaMap.objects.all()
  serializer_class = ISeeYaMapSerializer

class ISeeYaMapDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = ISeeYaMap.objects.all()
  serializer_class = ISeeYaMapSerializer

# LocationMap
class LocationMapMapList(generics.ListCreateAPIView):
  queryset = LocationMap.objects.all()
  serializer_class = LocationMapSerializer

class LocationMapMapDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = LocationMap.objects.all()
  serializer_class = LocationMapSerializer

# ProfileMap
class ProfileMapList(generics.ListCreateAPIView):
  queryset = ProfileMap.objects.all()
  serializer_class = ProfileMapSerializer

class ProfileMapDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = ProfileMap.objects.all()
  serializer_class = ProfileMapSerializer
