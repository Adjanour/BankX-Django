from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from Accounts.models import Account, Transaction , User
from APIx.serializers import AccountSerializer

from django.core.files.storage import default_storage
# Create your views here.


@csrf_exempt
def accountApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            account = Account.objects.all()
            account_serializer = AccountSerializer(account, many=True)
            return JsonResponse(account_serializer.data, safe=False)
        else:
            account = Account.objects.filter(id=id)
            account_serializer = AccountSerializer(account, many=True)
            response = JsonResponse(account_serializer.data, safe=False)
            response_data = json.loads(response.content)
            if not response_data:
                return JsonResponse("NO DATA FOUND",safe=False)
            else:
                return JsonResponse(account_serializer.data, safe=False)
            


    elif request.method == 'POST':
        account_data = JSONParser().parse(request)
        account_serializer = AccountSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add")

    elif request.method == 'PUT':
        account_data = JSONParser().parse(request)
        account = Account.objects.get(id = account_data['Id'])
        account_serializer = AccountSerializer(account, data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse("Update Successful",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == "DELETE":
        account = Account.objects.get(AccountId=id)
        account.delete()
        return JsonResponse("Deleted Successfully", safe=False)