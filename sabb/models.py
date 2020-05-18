from django.db import models


# Create your models here.
class address(models.Model):
    line_first = models.CharField(blank=False, null=False, max_length=200)
    line_second = models.CharField(blank=True, null=True, max_length=200)
    city = models.CharField(blank=True, null=True, max_length=50)
    state = models.CharField(blank=True, null=True, max_length=50)
    pincode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.city


class hotel(models.Model):
    hotel_type_choice = (
        ("AC", "AC"),
        ("NON-AC", "NON-AC"),
        ("AC + NON_AC", "AC + NON-AC"),
    )
    hotel_name = models.CharField(max_length=50, blank=True, null=True)
    hotel_Address = models.ForeignKey(address, on_delete=models.CASCADE)
    hotel_type = models.CharField(max_length=20, choices=hotel_type_choice)

    def __str__(self):
        return self.hotel_name
