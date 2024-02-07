import csv
from io import TextIOWrapper
import io
from django import forms
from datetime import datetime
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path

from .models import AverageHouseValueCHCH, AverageHouseValueNZ, AverageRentalGrowth, FamilyIncome, House, HouseValueGrowth, MeanHouseValueSuburbsCHCH, MortgageRates
from django.utils.html import format_html

class AdminPageWithCSVUpload(admin.ModelAdmin):
    
    change_list_template = "changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls    
    
    def import_csv(self, request):
        if request.method == "POST":
            csv_file_in_mem = request.FILES["csv_file"]

            file = csv_file_in_mem.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(file))    

            # Generate a list of row dictionaries
            data_dict_list = [line for line in reader]
            
            self.create_data(data_dict_list)
            
            self.message_user(request, "Your csv file has been imported")

        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "CSV_import.html", payload
        )
    
    def create_data(self, data_dict_list):
        pass
        


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(House)
class HouseAdmin(AdminPageWithCSVUpload):
    def create_data(self, data_dict_list):
        for row in data_dict_list:
            House.objects.create(
                areas = row['\ufeffTerritorial authority'],
                values = row['Average current value'].replace(",", ""),
                twelve_month_change = row["12 month change%"].replace("%", ""),
                three_month_change = row["3 month change %"].replace("%", ""),
            )
        
    list_display = ("areas", "display_values", "display_twelve_month_change", "display_three_month_change")
    
    def display_values(self, obj: House) -> str:
        return format_html("{}", obj.values)
    display_values.short_description = 'Values($)'  # type: ignore
    
    def display_twelve_month_change(self, obj: House) -> str:
        return f"{obj.twelve_month_change}"
    display_twelve_month_change.short_description = "Twelve Month Change(%)"  # type: ignore

    def display_three_month_change(self, obj: House) -> str:
        return f"{obj.three_month_change}"
    display_three_month_change.short_description = "Three Month Change(%)"  # type: ignore
    

# Register your models here.
@admin.register(FamilyIncome)
class FamilyIncomeAdmin(AdminPageWithCSVUpload):
    
    def create_data(self, data_dict_list):
        for row in data_dict_list:
            FamilyIncome.objects.create(
                year = row['Year'],
                family_income = row['Income'].replace(",", ''),
                change_compared_to_lastyear = row['Change'].replace("%", ""),
                region = row["Region"],
            )            

    list_display = ("year", "display_family_income", "display_change", "region")
    
    def display_family_income(self, obj: FamilyIncome):
        return f"{obj.family_income}"
    display_family_income.short_description = "family_income($)"  # type: ignore

    def display_change(self, obj: FamilyIncome):
        return f"{obj.change_compared_to_lastyear}"
    display_change.short_description = "change_compared_to_lastyear(%)"  # type: ignore


@admin.register(HouseValueGrowth)
class HouseValueGrowthAdmin(AdminPageWithCSVUpload):
    
    def create_data(self, data_dict_list):
        for row in data_dict_list:
            HouseValueGrowth.objects.create(
                year = row['\ufeffYear'],
                akl_house_value_growth = row['Auckland'],
                nz_house_value_growth = row['New Zealand'],
            )            

    list_display = ("year", "akl_house_value_growth", "nz_house_value_growth")


@admin.register(AverageRentalGrowth)
class AverageRentalGrowthAdmin(AdminPageWithCSVUpload):

    def create_data(self, data_dict_list):
        for row in data_dict_list:
            AverageRentalGrowth.objects.create(
                year = row['\ufeffYear'],
                akl_avg_rental_growth = row['Auckland'],
                nz_avg_rental_growth = row['New Zealand'],
            )            

    list_display = ("year", "akl_avg_rental_growth", "nz_avg_rental_growth")


@admin.register(MortgageRates)
class MortgageRatesAdmin(AdminPageWithCSVUpload):
    
    def create_data(self, data_dict_list):
        for row in data_dict_list:
            MortgageRates.objects.create(
                date = row['\ufeffDate'],
                three_year_rate = row['3 year rate'],
                four_year_rate = row['4 year rate'],
                five_year_rate = row['5 year rate']
            )            
    list_display = ("date", "three_year_rate", "four_year_rate", "five_year_rate")
    
    
@admin.register(AverageHouseValueNZ)
class AverageHouseValueNZAdmin(AdminPageWithCSVUpload):
    
    def create_data(self, data_dict_list):
        for row in data_dict_list:
            AverageHouseValueNZ.objects.create(
                name = row['\ufeffName'],
                year_2003 = row['2003'],
                year_2004 = row['2004'],
                year_2005 = row['2005'],
                year_2006 = row['2006'],
                year_2007 = row['2007'],
                year_2008 = row['2008'],
                year_2009 = row['2009'],
                year_2010 = row['2010'],
                year_2011 = row['2011'],
                year_2012 = row['2012'],
                year_2013 = row['2013'],
                year_2014 = row['2014'],
                year_2015 = row['2015'],
                year_2016 = row['2016'],
                year_2017 = row['2017'],
                year_2018 = row['2018'],
                year_2019 = row['2019'],
                year_2020 = row['2020'],
                year_2021 = row['2021'],
                year_2022 = row['2022'],
                year_2023 = row['2023'],                
            )            
    list_display = ("name", "year_2003", "year_2004", "year_2005", "year_2006",
                    "year_2007", "year_2008", "year_2009", "year_2010", "year_2011", 
                    "year_2012", "year_2013", "year_2014", "year_2015", "year_2016", 
                    "year_2017", "year_2018", "year_2019", "year_2020", "year_2021", 
                    "year_2022", "year_2023")


@admin.register(AverageHouseValueCHCH)
class AverageHouseValueCHCHAdmin(AdminPageWithCSVUpload):
    
    def create_data(self, data_dict_list):
        for row in data_dict_list:
            date_object = datetime.strptime(row["Value date"], "%d/%m/%Y")

            AverageHouseValueCHCH.objects.create(
                suburb=row["\ufeffSuburb name"],
                month=date_object.month,
                year=date_object.year,
                house_value=row["Property price"],
            )           
    list_display = ("suburb", "month", "year", "house_value")


@admin.register(MeanHouseValueSuburbsCHCH)
class MeanHouseValueSuburbsCHCHAdmin(AdminPageWithCSVUpload):
    
    def create_data(self, data_dict_list):
        for row in data_dict_list:

            MeanHouseValueSuburbsCHCH.objects.create(
                suburb=row["suburb"],
                month=row["month"],
                year=row["year"],
                price=row["price"],
            )    
       
    list_display = ("suburb", "month", "year", "price")
    list_filter = ["suburb"]