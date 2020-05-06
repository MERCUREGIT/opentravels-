from django.urls import path
from django.urls import path, re_path
from trip_manager import views


app_name='trip_manager'
urlpatterns = [
    path(r'', views.trip_page, name='trip_page'),
    re_path(r'^(?P<abc>[\w-]+)/$', views.trip_details, name='trip_detail'), 
    re_path(r'^trip_details/(?P<abc>[\w-]+)/$', views.trip_details_page, name='trip_details_page'), 
    re_path(r'^join/(?P<abc>[\w-]+)/$', views.joinTrip, name='join_trip'),
    re_path(r'^comment/(?P<abc>[\w-]+)/$', views.comment_trip, name='comment_trip'),
    re_path(r'^make_trip_public/(?P<abc>[\w-]+)/$', views.make_trip_public, name='make_trip_public')  
    
]

