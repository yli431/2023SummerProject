from django.urls import path
from dashboard import views


urlpatterns = [
    path('dashboard/', views.dashboard_views),
    path('fetch-mortgage-rate-data/', views.get_data_for_mortgage_rates),
    path('fetch-family-income-data/', views.get_data_for_family_income),
    path('fetch-rental-growth-data/', views.get_data_for_rental_growth),
    path('fetch-house-value-growth-data/', views.get_data_for_house_value_growth),
    path('fetch-house-value-nz-data/', views.get_data_for_avg_house_value_nz),
    path('fetch-house-value-change-data/', views.get_data_for_house_value_and_change),
]
