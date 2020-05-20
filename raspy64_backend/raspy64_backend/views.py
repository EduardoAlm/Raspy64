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
import base64
import hmac
import hashlib

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


class RandomReqView(APIView):
    def get(self, request, format=None):
        draw = np.random.randint(0, 2, 10)
        return Response(str(encrypt(pk, str(draw))), status=status.HTTP_200_OK)


class RealReqView(APIView):
    def get(self, request, format=None):
        draw = []
        weighted_random = [1] * 10 + [0] * 90
        for i in range(0, 10):
            draw.append(choice(weighted_random))

        res2 = base64.b64encode((bytes(str(draw), 'utf-8')))

        h = hmac.new(bytes("OneLoveInacio", 'utf-8'),
                     res2, hashlib.sha256)
        print(h.hexdigest())

        # print(res2)

        result = {
            'hmac': h.hexdigest(),
            'msg': res2
        }

        return Response(result, status=status.HTTP_200_OK)
