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

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random


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

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
pk = key.publickey().exportKey('DER')


class SendpkView(APIView):
    def get(self, request, format=None):
        print(pk)
        return Response(str(pk), status=status.HTTP_200_OK)


#----------Login --------------------#


class UserGetPhoneView(APIView):
    def get(self, request, format=None, id=None, pk=None):
        try:
            users = database.child(
                "Users/").child(key.decrypt(id)).child("Telemovel").get()
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(pk.encrypt(users.val()), status=status.HTTP_200_OK)


class UserGetUIDView(APIView):
    def get(self, request, format=None, email=None, pk=None):
        try:
            users = database.child("Users/").get()
            for user in users.each():
                aux = user.key()
                temp = database.child("Users/").child(aux).child("Email").get()
                if temp.val() == key.decrypt(email):
                    print(user.key())
                    return Response(pk.encrypt(user.key()), status=status.HTTP_200_OK)
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response("u dum dum", status=status.HTTP_400_BAD_REQUEST)


#-----------Registo--------------------#


class UserPostView(APIView):
    def post(self, request, format=None, id=None):
        data = request.data
        try:
            database.child("Users/").update(pk.encrypt(data))
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


#----------Oblivious Transfer--------------#
