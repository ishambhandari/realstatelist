from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ListingSerializer, ListingDetailSerializer
from .models import Listing
from rest_framework import permissions

# Create your views here.
class ListingView(ListAPIView):
    queryset = Listing.objects.filter(is_published = True).order_by('-list_date')
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class ListingsView(RetrieveAPIView):
    queryset = Listing.objects.filter(is_published = True).order_by ('-list_date')
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer

    def post(self, request, format = None):
        queryset = Listing.objects.order_by ('-list_date').filter(is_published = True)
        data = self.request.data

        sale_type = data['sale_type']
        queryset = queryset.filter(sale_type__iexact=sale_type)

        price = data['price']
        if price == '0+':
            price = 0 
        elif price == '$5000000':
            price = 5000000
        elif price == '$10000000':
            price = 10000000
        elif price == '$50000000':
            price = 50000000
        elif price == 'Any' :
            price = -1 
        
        if price != -1:
            queryset = queryset.filter(price__gte = price)
        
        bedrooms = data ['bedrooms']
        if bedrooms == '0+':
            bedroom = 0
        elif bedrooms == '1+':
            bedroom = 1
        elif bedrooms == '2+':
            bedroom = 2
        elif bedrooms == '3+':
            bedroom = 3
        elif bedrooms == '4+':
            bedroom = 4
        elif bedrooms == '5+':
            bedroom = 5
        
        queryset = queryset.filter(bedrooms__gte = bedrooms)
        
        property_type = data['property_type']
        queryset = queryset.filter(property_type__iexact = property_type)
        
        bathrooms = data['bathrooms']
        if bathrooms == '0+':
            bathrooms = 0.0
        elif bathrooms == '1+':
            bathrooms = 1.0
        elif bathrooms == '2+':
            bathrooms = 2.0
        elif bathrooms == '3+':
            bathrooms = 3.0
        elif bathrooms == '4+':
            bathrooms = 4.0
        
        land_area = data['land_area']
        if land_area == '2+':
            land_area = 2
        elif land_area == '4+':
            land_area = 4
        elif land_area == '6+':
            land_area = 6
        elif land_area == '8+':
            land_area = 8
        elif land_area == '12+':
            land_area = 12
        elif land_area == 'Any':
            land_area = 0

        if land_area != 0:
            queryset = queryset.filter(land_area__gte = land_area)
        
        keywords = data['keywords']
        queryset = queryset.filter(description__icontains = keywords)

        serializer = ListingSerializer(queryset, many = True)

