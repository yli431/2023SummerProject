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
    region = models.CharField(max_length=50, default="Other")
    
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


class AverageHouseValueNZ(models.Model):
    name = models.CharField(max_length=100)
    year_2003 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2004 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2005 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2006 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2007 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2008 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2009 = models.DecimalField(max_digits=50, decimal_places=1)   
    year_2010 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2011 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2012 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2013 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2014 = models.DecimalField(max_digits=50, decimal_places=1)   
    year_2015 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2016 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2017 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2018 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2019 = models.DecimalField(max_digits=50, decimal_places=1)   
    year_2020 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2021 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2022 = models.DecimalField(max_digits=50, decimal_places=1)
    year_2023 = models.DecimalField(max_digits=50, decimal_places=1)   
    
    def __str__(self):
        return str(self.name)


class AverageHouseValueCHCH(models.Model):
    suburb = models.CharField(max_length=100)
    month = models.IntegerField()
    year = models.IntegerField()
    house_value = models.IntegerField()
    
    def __str__(self):
        return str(self.suburb)
