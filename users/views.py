
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated, ValidationError
from django.contrib.auth import get_user_model
from .serializers.common import UserSerializer
import jwt
from django.conf import settings 
from datetime import datetime, timedelta



# Create your views here.
