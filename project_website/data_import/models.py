from django.db import models


class House(models.Model):
    areas = models.CharField(max_length=200)
    values = models.IntegerField()
    twelve_month_change = models.DecimalField(max_digits=50, decimal_places=2)
    three_month_change = models.DecimalField(max_digits=50, decimal_places=2)
    
    
    def __str__(self):
        return self.areas

class FamilyIncome(models.Model):
    year = models.IntegerField()
    family_income = models.DecimalField(max_digits=50, decimal_places=2)
    change_compared_to_lastyear = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.year)
    

class HouseValueGrowth(models.Model):
    year = models.IntegerField()
    akl_house_value_growth = models.DecimalField(max_digits=50, decimal_places=3)
    nz_house_value_growth = models.DecimalField(max_digits=50, decimal_places=3)
    
    def __str__(self):
        return str(self.year)
    

class AverageRentalGrowth(models.Model):
    year = models.IntegerField()
    akl_avg_rental_growth = models.DecimalField(max_digits=50, decimal_places=3)
    nz_avg_rental_growth = models.DecimalField(max_digits=50, decimal_places=3)
    
    def __str__(self):
        return str(self.year)
    
    
class MortgageRates(models.Model):
    date = models.CharField(max_length=100)
    three_year_rate = models.DecimalField(max_digits=50, decimal_places=2)
    four_year_rate = models.DecimalField(max_digits=50, decimal_places=2)
    five_year_rate = models.DecimalField(max_digits=50, decimal_places=2)
    
    def __str__(self):
        return str(self.date)

# Create your models here.
