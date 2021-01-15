from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title','address','city','price','sale_type','property_type', 'bedrooms','bathrooms','land_size','photo_main','slug')

class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =Listing
        fields = '__all__'
        lookup_field = 'slug'
        