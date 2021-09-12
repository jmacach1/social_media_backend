from django.db import models
from django.contrib.auth.models import User

ADDRESS = "address"
PROFILE = "profile"
options = (
  (ADDRESS, ADDRESS),
  (PROFILE, PROFILE)
)

class Location(models.Model):
  city = models.CharField(max_length=50)
  stateOrProvince = models.CharField(max_length=50, blank=True)
  country = models.CharField(max_length=50)
  lat = models.FloatField()
  lon = models.FloatField()

  def __str__(self):
    return f"{self.city}, {self.country}"

class ISeeYaUser(models.Model):
  django_auth_user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.django_auth_user.username}"
  

class Profile(models.Model):
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50, blank=True)
  last_name = models.CharField(max_length=50)
  profile_image_link = models.CharField(max_length=255)
  label = models.CharField(max_length=50)
  email = models.CharField(max_length=50, blank=True)
  iseeya_user = models.OneToOneField(ISeeYaUser, on_delete=models.CASCADE, related_name="profile", default=1)
  friends = models.ManyToManyField('self', related_name="friends")
  location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1) 

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

class Marker(models.Model):
  type = models.CharField(max_length=30, choices=options, default=ADDRESS)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f"Marker location={self.location} profile={self.profile}"


class ISeeYaMap(models.Model):
  type = models.CharField(max_length=30, choices=options, default=ADDRESS)
  name = models.CharField(max_length=50)
  owner = models.ForeignKey(ISeeYaUser, on_delete=models.CASCADE, related_name='iseeya_maps')
  markers = models.ManyToManyField(Marker, related_name="iseeya_map")  

  def __str__(self):
    return f"Map owner={self.owner} name={self.name}"

###########
class LocationMap(models.Model):
  type = "location"
  name = models.CharField(max_length=50)
  owner = models.ForeignKey(ISeeYaUser, on_delete=models.CASCADE, related_name='location_maps')
  locations = models.ManyToManyField(Location, related_name="location_maps")  

  def __str__(self):
    return f"LocationMap owner={self.owner} name={self.name}"

class ProfileMap(models.Model):
  type = "profile"
  name = models.CharField(max_length=50)
  owner = models.ForeignKey(ISeeYaUser, on_delete=models.CASCADE, related_name='profile_maps')
  profiles = models.ManyToManyField(Profile, related_name="profile_maps")

  def __str__(self):
    return f"ProfileMap owner={self.owner} name={self.name}"