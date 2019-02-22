from django.db import models
from apps.login_reg.models import User

class TripManager(models.Manager):
    def trip_validation(self, postData):
        errors = {}
        if len(postData['destination']) < 3:
            errors['destination'] = "Destination is required"
        if len(postData['start_date']) == 0:
            errors['start_date'] = "Start date is required"
        if len(postData['end_date']) == 0:
            errors['end_date'] = "End date is required"
        if len(postData['plan']) < 3:
            errors['plan'] = "Plan is required"

        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    plan = models.TextField()
    user_created_by = models.ForeignKey(User, related_name="trips")
    user_join = models.ManyToManyField(User, related_name="join_trips", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TripManager()