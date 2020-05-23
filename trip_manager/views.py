from django.shortcuts import render, redirect
from . import forms
from django.http import JsonResponse, HttpResponse
from .models import trip_data, join_trip, Trip_Comments
from django.contrib.auth.decorators import login_required

# Create your views here.

def trip_details(request, abc):
    trip= trip_data.objects.get(id=abc)
    trips_list = trip_data.objects.all().order_by('Date')
    form=forms.CreateTrip()
    return render(request,'./trip_manager/trip_page.html',{'form':form,'trips':trips_list,'trip_detail':trip})

def trip_details_page(request, abc):
    trip= trip_data.objects.get(id=abc)
    trips_list = trip_data.objects.all().order_by('Date')
    comment_trip = Trip_Comments.objects.all().order_by('comment_date_time')
    return render(request,'./trip_manager/trip_details.html',{"comments":comment_trip,'trips':trips_list,'trip_detail':trip})

# @login_required(login_url="/profile/")
def trip_page(request):
    # global form
   
    
    form=forms.CreateTrip()
    comment_trip = Trip_Comments.objects.all().order_by('comment_date_time')
    trip_joint=  join_trip.objects.filter(joinin_user=request.user) 
    print(trip_joint)
    if request.method == 'POST':
        form=forms.CreateTrip(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.author=request.user
            instance.save()
            instance.id
            trips = trip_data.objects.all().order_by('Date')
            return redirect('trip_manager/trip_page.html', {"comments":comment_trip,'form':form,'trips':trips, 'trip_joint':trip_joint})
        
    else:
        pass
    trips = trip_data.objects.all().order_by('Date')
    return render(request,'./trip_manager/trip_page.html', {"comments":comment_trip,'form':form, 'trips':trips})


def joinTrip(request, abc):
    t_join=join_trip()
    t_join.trip_data_id = abc
    t_join.joinin_user = request.user
    t_join.save()
    trip= trip_data.objects.get(id=abc)
    trips_list = trip_data.objects.all().order_by('Date')
    form=forms.CreateTrip()
    return render(request,'./trip_manager/trip_page.html',{'form':form,'trips':trips_list,'trip_detail':trip})

def comment_trip(request, abc):
    # check that user actually joined the trip
    if (join_trip.objects.filter(joinin_user=request.user)) and (join_trip.objects.filter(trip_data_id=abc)) :
    # if join_trip.objects.filter(trip_data_id=abc) :
        # create a trip_comment object
        comment = Trip_Comments()
        # passing data to the object and saving it
        comment.description = str(request.POST.dict()["comment"])
        comment.commenting_user = request.user
        comment.trip_data_id = abc
        comment.save()
        
        # comment list 
        form = forms.CreateTrip()
        trips_list = trip_data.objects.all().order_by('Date')
        
        comment_trip = Trip_Comments.objects.all().order_by('comment_date_time')
        
        return render(request,'./trip_manager/trip_page.html',{ "comments":comment_trip, 'form':form,'trips':trips_list})
    else:
        print(str(request.user))
        return HttpResponse ('user did not register this trip')

def make_trip_public(request,abc):
    # make a trip that was initialty private public
    # check if the user trying to change it is the user that actually created it and if the trip exist
    trip = trip_data.objects.get(id=abc)
    if trip.author == request.user:
        trip.is_public = True
        trip.save()
        print(trip_data.objects.get(id=abc))
        return HttpResponse("Trip was  made public")
    else:
         return HttpResponse("Trip was not made public")
        
        
        
def create_group():
    pass