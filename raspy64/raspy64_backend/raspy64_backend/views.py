from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .models import Users
from .serializers import userSerializer
from django.db import connection
from django.db import transaction, DatabaseError
from django.http import JsonResponse
import datetime
import time
import pyrebase

config = {
    'apiKey': "AIzaSyC-aDSTtVmZUJD6EsQQqRSwsARKeviP1ss",
    'authDomain': "raspy64-55ac5.firebaseapp.com",
    'databaseURL': "https://raspy64-55ac5.firebaseio.com",
    'projectId': "raspy64-55ac5",
    'storageBucket': "raspy64-55ac5.appspot.com",
    'messagingSenderId': "683886857240",
    'appId': "1:683886857240:web:1cb1265703df2403e6076d",
    'measurementId': "G-0244STL3X6"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

#----------Login --------------------#


class UserGetPhoneView(APIView):
    def get(self, request, format=None, id=None):
        try:
            users = database.child("Users/").child(id).get()
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(users.val(), status=status.HTTP_200_OK)

#-----------Registo--------------------#


class UserPostView(APIView):
    def post(self, request, format=None, id=None):
        data = request.data
        try:
            database.child("Users/").update(data)
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

#----------Oblivious Transfer--------------#
