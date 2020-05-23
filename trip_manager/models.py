from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
# [\d-]+
class trip_data(models.Model):
    origin = models.CharField( max_length=50)
    destination = models.CharField( max_length=50)
    Date = models.DateField(auto_now_add=False)
    Time = models.TimeField( auto_now_add=False)
    PostDate = models.DateField(auto_now_add=True)
    description = models.TextField()
    agency= models.CharField( max_length=50)
    author = models.ForeignKey(User,default='anonymous',on_delete=models.CASCADE)
    thumb=models.ImageField( default='default.png', blank=True)
    is_public = models.BooleanField(_("Pushish Trip"), default=True)
    group_exist =  models.BooleanField(default=False)
    # add author
    
    def __str__(self):
         return self.origin

    def presentDescription(self):
        return self.description[:250] + "..."
   
    def display_trip_all(self):
        if self.is_public==True:
             return self
        else:
             pass        
    
class join_trip(models.Model):
     joinin_user = models.ForeignKey(User,default='anonymous',on_delete=models.CASCADE)
     trip_data_id = models.IntegerField(blank=False)
     
    
     
     
class Trip_Comments(models.Model):
     commenting_user = models.ForeignKey(User,default='anonymous',on_delete=models.CASCADE)
     trip_data_id = models.IntegerField(blank=False)
     comment_date_time = models.DateTimeField(auto_now_add=True)
     description = models.TextField()
     thumb=models.ImageField(default=None, blank=True)
     
     def getNumberOfComments(self):
          count = self.objects.filter(trip_data_id = self.trip_data_id).count()
          return count
     
     