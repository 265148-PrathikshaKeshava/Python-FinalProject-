from django.urls import path
from . import views

urlpatterns = [
    path('emi/', views.emi_calculator, name='emi_calculator'),
    path('sip/', views.sip_calculator, name='sip_calculator'),
    path('fd/', views.fd_calculator, name='fd_calculator'),
    path('rd/', views.rd_calculator, name='rd_calculator'),
    path('retirement/', views.retirement_savings_estimator, name='retirement_savings_estimator'),
    path('loan-eligibility/', views.home_loan_eligibility_estimator, name='home_loan_eligibility_estimator'),
    path('credit-card/', views.credit_card_interest_calculator, name='credit_card_interest_calculator'),
    path('taxable-income/', views.taxable_income_calculator, name='taxable_income_calculator'),
    path('budget/', views.simple_budget_planner, name='simple_budget_planner'),
    path('net-worth/', views.net_worth_calculator, name='net_worth_calculator'),
]
