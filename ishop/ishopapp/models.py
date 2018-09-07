from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Phone(models.Model):
    PID = models.AutoField(primary_key=True)
    ContactNo = models.CharField(max_length=8)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Item(models.Model):
    IID = models.AutoField(primary_key=True)
    Seller = models.ForeignKey(User, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=7, decimal_places=1)
    Textbook = 'Textbook'
    Instrument = 'Instrument'
    SchoolUniform = 'SchoolUniform'
    Stationary = 'Stationary'
    Others = 'Others'
    TYPE_CHOICE = (
        (Textbook, 'Textbook'),
        (Instrument, 'Instrument'),
        (SchoolUniform, 'SchoolUniform'),
        (Stationary, 'Stationary'),
        (Others, 'Others'),
    )
    Type = models.CharField(
        max_length=13,
        choices=TYPE_CHOICE
    )
    LaunchDate = models.DateField(auto_now_add=True)
    TradingLocation = models.CharField(max_length=50)
    Status = models.BooleanField(default=False)
    Name = models.CharField(max_length=30)
    Description = models.TextField(max_length=30)
