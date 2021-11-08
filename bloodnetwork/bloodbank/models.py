from django.db import models

# Create your models here.
from django.db import models
from User.models import Blood


# Create your models here.

class bloodbank(models.Model):
    Blood_Bank_Name = models.CharField(max_length= 69)
    Address = models.CharField(max_length= 200)
    def __str__(self):
        return f"{self.Blood_Bank_Name}   ({self.Address})"
    
class Category(models.Model):
    Blood_Bank_ID = models.ForeignKey(bloodbank, on_delete= models.CASCADE)
    Category_choices=[
        ('RBC',"RBC"),
        ("Plasma","Plasma"),
        ("Platelet","Platelet")
    ]
    category = models.CharField(
        max_length=9, blank=True, null=True,
        choices =Category_choices,
        )
    Blood_Type = models.ForeignKey(Blood,on_delete=models.CASCADE,related_name="bloodtype",null=True)
    price_per_bag = models.IntegerField(null = True)
    Quantity = models.IntegerField(null = True)
    Exipration_date = models.DateField()
    def __str__(self):
         return self.category

class Donor(models.Model):
    Donor_Name = models.CharField(max_length= 69)
    Donor_Email = models.EmailField()
    Donor_Phone= models.CharField(max_length=15,null=True)
    Donor_District=models.CharField(max_length=15,null=True)
    Donor_Area=models.CharField(max_length=15,null=True)
    Donor_Postalcode=models.IntegerField()
    Date_Of_Donation=models.DateField()
    Donor_Bloodhroup=models.CharField(max_length=5,null=True)
    Blood_Bank_Name=models.CharField(max_length=70,null=True)

    def __str__(self):
        return self.Donor_Name