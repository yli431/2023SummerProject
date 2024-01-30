from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import AverageRentalGrowth, FamilyIncome, House, HouseValueGrowth, MortgageRates
import csv


def import_house_price_data(request):
    csv_file_path = 'D:\\workspace\\2023SummerProject\\data\\NZ_HousePriceIndex_27NOV2023.csv'
    
    with open(csv_file_path, 'r') as csv_file:
        # csv_reader = csv.DictReader(csv_file)
        csv_reader = csv.reader(csv_file)
        num_of_data = 0
        if House.objects.all().exists():
            print("Data already exist.")
        else:
            for row in csv_reader:
                House.objects.create(
                    areas = row['ï»¿Territorial authority'],
                    values = row['Average current value'].replace(",", ""),
                    twelve_month_change = row["12 month change%"].replace("%", ""),
                    three_month_change = row["3 month change %"].replace("%", ""),
                )
                num_of_data += 1            
    # return HttpResponse(f'{num_of_data} lines of House price Nov 2023 data imported successfully.')
    return HttpResponse(f'{num_of_data} lines of House price Nov 2023 data imported successfully.')


def import_family_income_data(request):
    csv_file_path = 'D:\\workspace\\2023SummerProject\\data\\NZ family income excl AKL.csv'
    
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        num_of_data = 0
        if FamilyIncome.objects.all().exists():
            print("Data already exist.")
        else:
            for row in csv_reader:
                FamilyIncome.objects.create(
                    year = row['ï»¿Year'],
                    family_income = row['Income'].replace(",", ''),
                    change_compared_to_lastyear = row['Change'].replace("%", ""),
                )
                num_of_data += 1
    return HttpResponse(f'{num_of_data} lines of family income data imported successfully.')


def import_house_value_growth(request):
    csv_file_path = 'D:\\workspace\\2023SummerProject\\data\\House_value_growth_2006-2023.csv'
    
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        num_of_data = 0
        if HouseValueGrowth.objects.all().exists():
            print("Data already exist.")
        else:
            for row in csv_reader:
                HouseValueGrowth.objects.create(
                    year = row['ï»¿Year'],
                    akl_house_value_growth = row['Auckland'],
                    nz_house_value_growth = row['New Zealand'],
                )
                num_of_data += 1
    return HttpResponse(f'{num_of_data} lines of house value growth data imported successfully.')


def import_average_rental_growth(request):
    csv_file_path = 'D:\\workspace\\2023SummerProject\\data\\Growth_in_average_rent_2001-2023.csv'
    
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        num_of_data = 0
        if AverageRentalGrowth.objects.all().exists():
            print("Data already exist.")
        else:
            for row in csv_reader:
                AverageRentalGrowth.objects.create(
                    year = row['ï»¿Year'],
                    akl_avg_rental_growth = row['Auckland'],
                    nz_avg_rental_growth = row['New Zealand'],
                )
                num_of_data += 1
    return HttpResponse(f'{num_of_data} lines of average rental growth data imported successfully.')


def import_mortgage_rate(request):
    csv_file_path = 'D:\\workspace\\2023SummerProject\\data\\mortgage rates 2006-2023.csv'
    
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        num_of_data = 0
        if MortgageRates.objects.all().exists():
            print("Data already exist.")
        else:
            for row in csv_reader:
                MortgageRates.objects.create(
                    date = row['ï»¿Date'],
                    three_year_rate = row['3 year rate'],
                    four_year_rate = row['4 year rate'],
                    five_year_rate = row['5 year rate']
                )
                num_of_data += 1
    return HttpResponse(f'{num_of_data} lines of mortgage rate data imported successfully.')
