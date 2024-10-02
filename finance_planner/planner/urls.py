from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transactions/', views.view_transactions, name='view_transactions'),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('financial-advice/', views.financial_advice, name='financial_advice'),
]
