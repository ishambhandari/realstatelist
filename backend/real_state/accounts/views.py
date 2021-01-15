from django.contrib.auth import get_user_model 
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import permissions
# Create your views here.

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        #retrieves the form data
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2'] 
        if password == password2:
            if User.object.filter(email=email).exists():
                return Response({'error':'Email already exists'})
            else:
                if len(password) < 6: 
                    return Response({'error':'Password must be atleast 6 character'})
                else:
                    user = User.object.create_user(email = email, password = password, name = name)
                    user.save()
                return Response({'success':'User created successfully'})

        else: 
            return Response({'error':'Passwords do not match'})


