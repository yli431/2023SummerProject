from django.conf import settings
from django.template import loader
from django.http import HttpResponse, JsonResponse
from data_import.models import AverageHouseValueNZ, AverageRentalGrowth, FamilyIncome, House, HouseValueGrowth, MeanHouseValueSuburbsCHCH, MortgageRates

# Create your views here.
def dashboard_views(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())

def get_data_for_mortgage_rates(request) -> JsonResponse:
    rates = MortgageRates.objects.all().order_by("date")
    mortgage_rates = []
    for rate in rates:
        if rate.date is None:
            continue
        mortgage_rates.append(
            {
                "date": rate.date.strftime("%d/%m/%Y"),
                "three_year_rate": rate.three_year_rate,
                "four_year_rate": rate.four_year_rate,
                "five_year_rate": rate.five_year_rate,
            }
        )    
    return JsonResponse({"mortgage_rates": mortgage_rates})


def get_data_for_family_income(request) -> JsonResponse:
    family_income_items = FamilyIncome.objects.all()
    family_income = []

    for family_income_item in family_income_items:
        family_income.append(
            {
                "year": family_income_item.year,
                "family_income": family_income_item.family_income,
                # "change_compared_to_lastyear": family_income_item.change_compared_to_lastyear,
                "region": family_income_item.region,
            }
        )    
    return JsonResponse({"family_income": family_income})

def get_data_for_rental_growth(request) -> JsonResponse:
    rental_growth_items = AverageRentalGrowth.objects.all()
    rental_growth = []
    for rental_growth_item in rental_growth_items:
        rental_growth.append( 
            {
                "year": rental_growth_item.year,
                "akl_avg_rental_growth": rental_growth_item.akl_avg_rental_growth,
                "nz_avg_rental_growth": rental_growth_item.nz_avg_rental_growth,
            }
        )
    return JsonResponse({"rental_growth": rental_growth})

def get_data_for_house_value_growth(request) -> JsonResponse:
    house_value_growth_items = HouseValueGrowth.objects.all()
    house_value_growth = []
    for house_value_growth_item in house_value_growth_items:
        house_value_growth.append( 
            {
                "year": house_value_growth_item.year,
                "akl_house_value_growth": house_value_growth_item.akl_house_value_growth,
                "nz_house_value_growth": house_value_growth_item.nz_house_value_growth,
            }
        )
    return JsonResponse({"house_value_growth": house_value_growth})

def get_data_for_avg_house_value_nz(request):
    house_value_nz_items = AverageHouseValueNZ.objects.all()
    house_value_nz = []
    for house_value_item in house_value_nz_items:
        house_value_nz.append(
            {
            "name": house_value_item.name,
            "year_2003": house_value_item.year_2003,
            "year_2004": house_value_item.year_2004,
            "year_2005": house_value_item.year_2005,
            "year_2006": house_value_item.year_2006,
            "year_2007": house_value_item.year_2007,
            "year_2008": house_value_item.year_2008,
            "year_2009": house_value_item.year_2009,
            "year_2010": house_value_item.year_2010,
            "year_2011": house_value_item.year_2011,
            "year_2012": house_value_item.year_2012,
            "year_2013": house_value_item.year_2013,
            "year_2014": house_value_item.year_2014,
            "year_2015": house_value_item.year_2015,
            "year_2016": house_value_item.year_2016,
            "year_2017": house_value_item.year_2017,
            "year_2018": house_value_item.year_2018,
            "year_2019": house_value_item.year_2019,
            "year_2020": house_value_item.year_2020,
            "year_2021": house_value_item.year_2021,
            "year_2022": house_value_item.year_2022,
            "year_2023": house_value_item.year_2023,
            }
        )
    return JsonResponse({"house_value_nz": house_value_nz})

    
def get_data_for_house_value_and_change(request) -> JsonResponse:
    house_items = House.objects.all()
    house_value_and_change = []
    for house_item in house_items:
        house_value_and_change.append( 
            {
                "areas": house_item.areas,
                "values": house_item.values,
                "twelve_month_change": house_item.twelve_month_change,
                "three_month_change": house_item.three_month_change,
            }
        )
    return JsonResponse({"house_value_and_change": house_value_and_change})

def get_data_for_mean_house_value_of_chch_suburbs(request) -> JsonResponse:
    suburb_items = MeanHouseValueSuburbsCHCH.objects.all().order_by("suburb", "date")
    house_value_of_chchsuburbs_dict = {}
    
    for suburb_item in suburb_items:
        if suburb_item.suburb not in house_value_of_chchsuburbs_dict:
            house_value_of_chchsuburbs_dict[suburb_item.suburb]=[
                {
                    "year": suburb_item.date.year,  # type: ignore
                    "month": suburb_item.date.month,  # type: ignore
                    "price": suburb_item.price,
                }
            ]
        else:
            house_value_of_chchsuburbs_dict[suburb_item.suburb].append(
                {
                    "year": suburb_item.date.year,  # type: ignore
                    "month": suburb_item.date.month,  # type: ignore
                    "price": suburb_item.price,
                }
            )

    return JsonResponse({"house_value_of_chchsuburbs_dict": house_value_of_chchsuburbs_dict})
