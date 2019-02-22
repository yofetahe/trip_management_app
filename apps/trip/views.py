from django.shortcuts import render, redirect
from .models import Trip
from django.contrib import messages
from apps.login_reg.models import User
from django.db.models import Q

def trip_dashboard(request):

    if 'user' not in request.session:
        return redirect('/../login/get_login_page')

    user = User.objects.get(id=request.session['user_id'])
    trips = Trip.objects.filter(Q(user_created_by=user) | Q(user_join=user)).order_by("created_at")
    other_trips = Trip.objects.all().exclude(user_join=user).exclude(user_created_by=user)
    context = {
        "trips": trips,
        "other_trips": other_trips
    }
    return render(request, 'trip/trip_dashboard.html', context)

def get_create_form(request):
    
    if 'user' not in request.session:
        return redirect('/../login/get_login_page')

    return render(request, 'trip/trip_create_form.html')

def create_trip(request):
    
    if 'user' not in request.session:
        return redirect('/../login/get_login_page')
   
    if 'submit' in request.POST:

        # validation
        errors = Trip.objects.trip_validation(request.POST)
        if len(errors) > 0:
            for tag, value in errors.items():
                messages.error(request, value, extra_tags=tag)
            return redirect(get_create_form)

        # creation
        user = User.objects.get(id=request.session['user_id'])
        Trip.objects.create(destination=request.POST['destination'], start_date=request.POST['start_date'], end_date=request.POST['end_date'], plan=request.POST['plan'], user_created_by=user )
    
    return redirect(trip_dashboard)

def get_update_form(request, trip_id):
    
    if 'user' not in request.session:
        return redirect('/../login/get_login_page')

    trip = Trip.objects.get(id=trip_id)
    context = {
        "trip": trip
    }
    return render(request, 'trip/trip_update_form.html', context)

def tripUpdate(request, trip_id):
    
    if 'user' not in request.session:
        return redirect('/../login/get_login_page')


    if 'submit' in request.POST:
        # validation
        errors = Trip.objects.trip_validation(request.POST)
        if len(errors) > 0:
            for tag, value in errors.items():
                messages.error(request, value, extra_tags=tag)
            return redirect('get_update_form', trip_id=trip_id)

        # update
        trip = Trip.objects.get(id=trip_id)
        trip.destination = request.POST['destination']
        trip.start_date = request.POST['start_date']
        trip.end_date = request.POST['end_date']
        trip.plan = request.POST['plan']
        trip.save()

    return redirect(trip_dashboard)

def remove_trip(request, trip_id):
    
    if 'user' not in request.session:
        return redirect('/../login/get_login_page')

    trip = Trip.objects.get(id=trip_id)
    trip.delete()
    return redirect(trip_dashboard)

def get_trip_detail(request, trip_id):
    
    if 'user' not in request.session:
        return redirect('/../login/get_login_page')

    trip = Trip.objects.get(id=trip_id)
    user = User.objects.get(id=request.session['user_id'])
           
    context = {
        "trip": trip,
        "user": user
    }

    return render(request, 'trip/trip_detail.html', context)


def join_trip(request, trip_id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=trip_id)
    trip.user_join.add(user)
    trip.save()
    
    return redirect(trip_dashboard)

def cancel_join(request, trip_id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=trip_id)
    trip.user_join.remove(user)
    
    return redirect(trip_dashboard)

