from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from account.models import Account
from account.serializers import AccountSerializer


# Create your views here.

@api_view(['POST'])
def create_account(request):
    if request.method == 'POST':
        account_data = JSONParser().parse(request)
        account_serializer = AccountSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse(account_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse('Only POST requests are accepted', status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT'])
def modify_account(request):
    if request.modethod == 'DELETE':
        pass
    else:
        pass


# i think login goes here, but not sure yet
@api_view(['GET'])
def login(request):
    pass


@api_view(['GET'])
def account_list(request):
    pass