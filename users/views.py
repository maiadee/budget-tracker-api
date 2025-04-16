# allows you to define custom logic for handling these requests and returning appropriate responses
from rest_framework.views import APIView
# Response is used to return data in your API views. It automatically formats the returned data into the appropriate response type
from rest_framework.response import Response
#  imports two exceptions from DRF.
from rest_framework.exceptions import NotAuthenticated, ValidationError
# get_user_model() returns the User model you have configured for your application.
from django.contrib.auth import get_user_model
from .serializers.common import UserSerializer
import jwt
from django.conf import settings 
from datetime import datetime, timedelta

User = get_user_model()

# Create your views here
class RegisterView(APIView):
    def post(self, request):
        # get the user data and serialize it
        serialized_user = UserSerializer(data=request.data)
        # if data is valid, save / print data and return the response
        if serialized_user.is_valid():
            serialized_user.save()
            print(serialized_user.data)
            return Response(serialized_user.data, 201)
        return Response(serialized_user.errors, 422)

class LoginView(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            # 1. Search for the user by its username
            user = User.objects.get(username=username)

            # 2. Check plain text password matches hash, raise validation error if not
            if not user.check_password(password):
                raise ValidationError({ 'password': 'Passwords do not match' })
            
            # 3. Generate an expiry date
            exp_date = datetime.now() + timedelta(days=1)

            # Generate token using pyjwt package
            token = jwt.encode(
                payload={
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'is_admin': user.is_staff
                    },
                    'exp': int(exp_date.strftime('%s'))
                },
                key=settings.SECRET_KEY,
                algorithm='HS256'
            )

            # Send token in response
            return Response({ 'message': 'Login was successful', 'token': token })
            
        except (User.DoesNotExist, ValidationError) as e:
            # If either a DoesNotExist or a ValidationError is raised inside the catch, this except block will catch it
            print(e)
       
            raise NotAuthenticated('Invalid credentials')