from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trip_dashboard/$', views.trip_dashboard, name="trip_dashboard"),
    url(r'^get_create_form/$', views.get_create_form, name="get_create_form"),
    url(r'^create_trip/$', views.create_trip, name="create_trip"),
    url(r'^get_update_form/(?P<trip_id>\d+)$', views.get_update_form, name="get_update_form"),
    url(r'^tripUpdate/(?P<trip_id>\d+)$', views.tripUpdate, name="tripUpdate"),
    url(r'^remove_trip/(?P<trip_id>\d+)$', views.remove_trip, name="remove_trip"),
    url(r'^get_trip_detail/(?P<trip_id>\d+)$', views.get_trip_detail, name="get_trip_detail"),
    url(r'^join_trip/(?P<trip_id>\d+)$', views.join_trip, name="join_trip"),
    url(r'^cancel_join/(?P<trip_id>\d+)$', views.cancel_join, name="cancel_join"),
]
