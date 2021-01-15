from django.urls import path
from .views import ListingsView, ListingView, SearchView 

urlpatterns = [
    path('<slug>', ListingsView.as_view()),
    path('', ListingView.as_view()),
    path('search', SearchView.as_view()),
]