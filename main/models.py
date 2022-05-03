from django.db import models
from django.contrib.auth.models import User
class slotdb(models.Model):
    slotid=models.BigAutoField(primary_key=True)
    slot_start=models.TimeField()
    slot_end=models.TimeField(default=None)
    capacity=models.IntegerField()
    active=models.BooleanField(default=False)
class bookingdb(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    slotid=models.ForeignKey(slotdb,on_delete=models.CASCADE)
    date=models.DateField(default=None)
    attended=models.BooleanField(default=False)




