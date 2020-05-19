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
import numpy as np
from numpy.random import choice
from simplecrypt import encrypt, decrypt


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

'''random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
pk = key.publickey().exportKey('DER')'''


pk = bytes("tjAia9eqElIIZScEdfrbrIquh332B0ske1ffv3UN1FRQh0oS/GjuaIPls5eDy9EoUfIlhGqrkcYX1s39XOgw9X/rqP4hmtU8ymm0fJ0wpQ6qIjrN+gvQBNoQk6cWgoSzItg+fhGqECBoNUHzyswXFkVXX1h1S0eIRz9r6nHc87k=", 'utf-8')

#--------keyExchange----------------#

'''class SendpkView(APIView):
    def get(self, request, format=None):
        print(pk)
        return Response(str(pk), status=status.HTTP_200_OK)'''


# ----------Oblivious Transfer--------

class RandomReqView(APIView):
    def get(self, request, format=None):
        draw = np.random.randint(0, 2, 10)
        return Response(str(encrypt(pk, str(draw))), status=status.HTTP_200_OK)


class RealReqView(APIView):
    def get(self, request, format=None):
        draw = []
        weighted_random = [1] * 10 + [0] * 90
        for i in range(0, 10):
            draw.append(random.choice(weighted_random))
        return Response(str(encrypt(pk, str(draw))), status=status.HTTP_200_OK)


'''
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
    def post(self, request, format=None, id=None, Email=None, Raspadinha=None, Telemovel=None, Username=None):
        data = request.data
        try:
            database.child("Users/").update(key.decrypt(id))
            database.child("Users/").child(key.decrypt(id)
                                           ).child("Email").update(key.decrypt(Email))
            database.child("Users/").child(key.decrypt(id)
                                           ).child("Raspadinha").update(key.decrypt(Raspadinha))
            database.child("Users/").child(key.decrypt(id)
                                           ).child("Telemovel").update(key.decrypt(Telemovel))
            database.child("Users/").child(key.decrypt(id)
                                           ).child("Username").update(key.decrypt(Username))
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


#----------Oblivious Transfer--------------#
'''
