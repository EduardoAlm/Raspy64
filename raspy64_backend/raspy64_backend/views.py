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

from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from base64 import b64decode
import Crypto
from Crypto.PublicKey import RSA
import rsa
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

key_pair = RSA.generate(2048, e=537)
private_key = open("privatekey.pem", "wb")
private_key.write(key_pair.exportKey(passphrase="WeLoveInacio"))
private_key.close()
public_key = open("public_key.pem", "wb")
public_key.write(key_pair.publickey().exportKey())
public_key.close()
'''
private_key = None
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=1024, backend=default_backend())
public_key = private_key.public_key()
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo)
'''
x0 = random.randint(0, 537)
x1 = random.randint(0, 537)
m0 = -1
m1 = -1


def file_get_contents(filename):
    with open(filename) as f:
        return f.read()


def compute_message():
    m0 = [1] * 10 + [0] * 90
    m1 = [1] * 10 + [0] * 90


class FirstCommView(APIView):
    def get(self, request, format=None):

        result = {
            'N': file_get_contents("public_key.pem"),
            'e': 537,
            'x0': x0,
            'x1': x1
        }
        compute_message()
        return Response(result, status=status.HTTP_200_OK)


class RealReqView(APIView):
    def post(self, request, format=None):
        v = b64decode(request.data['base64'])
        vlen = len(v)
        x0 = request.data['x0']
        x1 = request.data['x1']
        m0 = random.randint(0, 1)
        m1 = random.randint(0, 1)
        print(type(v))
        print(type(x0))
        print(type(x1))

        key = RSA.importKey(file_get_contents(
            "privatekey.pem"), passphrase="WeLoveInacio")
        print("h1")
        cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
        print("h2")
        decrypted_message = cipher.decrypt(v)
        print(decrypted_message)
        decrypted = decrypted_message.decode()
        print(decrypted)
        k0 = int(decrypted) - x0
        print(k0)
        k1 = int(decrypted) - x1
        print(k1)
        while m1 == -1 | m0 == -1:
            compute_message()
        print(m0)
        print(m1)

        res0 = base64.b64encode(bytes(str(m0+k0), "utf-8"))
        res1 = base64.b64encode(bytes(str(m1+k1), "utf-8"))

        h0 = hmac.new(bytes("WeLoveInacio", 'utf-8'),
                      res0, hashlib.sha256)

        h1 = hmac.new(bytes("WeLoveInacio", 'utf-8'),
                      res1, hashlib.sha256)
        result = {
            'm0_linha': m0+k0,
            'm1_linha': m1+k1,
            'hmac0': base64.b64encode(h0.digest()).decode(),
            'hmac1': base64.b64encode(h1.digest()).decode()
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
