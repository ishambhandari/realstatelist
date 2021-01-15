from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact 
from django.core.mail import send_mail
from rest_framework.response import Response 
from .serializers import ContactSerializer

class ContactCreateView(APIView):
    model = Contact
    permission_classes = (permissions.AllowAny, )
    serializer_class = ContactSerializer

    def post(self,request, format=None):
        data = self.request.data 
        contact_subject = data['subjects']
        contact_email = data['email']
        contact_message = data['message']
        
        try:
            send_mail(contact_subject, contact_message, contact_email ,['ishambhandari007@gmail.com'],)
        
            contact = Contact(name=data['name'], email = data['email'], subjects= data['subjects'], message = data['message'],)
            contact.save()
            return Response({'success':'Message Send Successfully'})

        except:
            return Response({'error':'Failed'})