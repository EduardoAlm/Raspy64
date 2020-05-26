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
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import random
from json import JSONEncoder
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import operator


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
private_key = None
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend())
public_key = private_key.public_key()
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo)

x0 = random.randint(0, 65537)
x1 = random.randint(0, 65537)


class FirstCommView(APIView):
    def get(self, request, format=None):

        result = {
            'N': pem,
            'e': 65537,
            'x0': x0,
            'x1': x1
        }

        return Response(result, status=status.HTTP_200_OK)


class RealReqView(APIView):
    def get(self, request, format=None, v=None, x0=None, x1=None):

        m0 = random.randint(0, 1)
        m1 = random.randint(0, 1)

        k0 = private_key.decrypt(str(operator.xor(v, x0)), padding.OAEP(mgf=padding.MGF1(
            algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

        k1 = private_key.decrypt(str(operator.xor(v, x1)), padding.OAEP(mgf=padding.MGF1(
            algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

        result = {
            'm0_linha': operator.xor(m0, k0),
            'm1_linha': operator.xor(m1, k1),
        }

        return Response(result, status=status.HTTP_200_OK)


'''class RealReqView(APIView):
    def get(self, request, format=None):
        draw = []
        weighted_random = [1] * 10 + [0] * 90
        for i in range(0, 10):
            draw.append(choice(weighted_random))

        res2 = base64.b64encode((bytes(str(draw), 'utf-8')))

        h = hmac.new(bytes("OneLoveInacio", 'utf-8'),
                     res2, hashlib.sha256)
        print(h.digest())

        # print(res2)

        result = {
            'hmac': base64.b64encode(h.digest()).decode(),
            'msg': res2
        }

        return Response(result, status=status.HTTP_200_OK)'''
