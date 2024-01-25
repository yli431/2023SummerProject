from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('house_price_index/', views.import_house_price_data),
    path('family_income/', views.import_family_income_data),
    path('house_value_growth/', views.import_house_value_growth),
    path("average_rental_growth/", views.import_average_rental_growth),
    path('mortgage_rates/', views.import_mortgage_rate),
    path('try_frontend/', views.try_frontend),
    path('click_and_process/', views.click_and_process),
]

    # path("", views.index, name="index"),
    # # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
