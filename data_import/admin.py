from django.contrib import admin
from .models import AverageRentalGrowth, FamilyIncome, House, HouseValueGrowth, MortgageRates
from django.utils.html import format_html

# admin.site.register(House)
# admin.site.register(FamilyIncome)
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("areas", "display_values", "display_twelve_month_change", "display_three_month_change")
    
    def display_values(self, obj: House) -> str:
        return format_html("{}", obj.values)
    display_values.short_description = 'Values($)'
    
    def display_twelve_month_change(self, obj: House) -> str:
        return f"{obj.twelve_month_change}"
    display_twelve_month_change.short_description = "Twelve Month Change(%)" 

    def display_three_month_change(self, obj: House) -> str:
        return f"{obj.three_month_change}"
    display_three_month_change.short_description = "Three Month Change(%)" 

# Register your models here.
@admin.register(FamilyIncome)
class FamilyIncomeAdmin(admin.ModelAdmin):
    list_display = ("year", "display_family_income", "display_change")
    
    def display_family_income(self, obj: FamilyIncome):
        return f"{obj.family_income}"
    display_family_income.short_description = "family_income($)"

    def display_change(self, obj: FamilyIncome):
        return f"{obj.change_compared_to_lastyear}"
    display_change.short_description = "change_compared_to_lastyear(%)"


@admin.register(HouseValueGrowth)
class HouseValueGrowthAdmin(admin.ModelAdmin):
    list_display = ("year", "akl_house_value_growth", "nz_house_value_growth")


@admin.register(AverageRentalGrowth)
class AverageRentalGrowthAdmin(admin.ModelAdmin):
    list_display = ("year", "akl_avg_rental_growth", "nz_avg_rental_growth")


@admin.register(MortgageRates)
class MortgageRatesAdmin(admin.ModelAdmin):
    list_display = ("date", "three_year_rate", "four_year_rate", "five_year_rate")
