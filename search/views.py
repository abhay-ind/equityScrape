from django.shortcuts import render
from django.conf import settings
from .apps import SearchConfig
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import csv

# Create your views here.

from rest_framework.views import APIView


class searchApi(APIView):
    def get(self, request):
        searchtext = request.GET.get("search")
        listOfNames = SearchConfig.redis_instance.keys(searchtext.upper() + "*")
        dictResult = list()
        for idx, i in enumerate(listOfNames):
            values = SearchConfig.redis_instance.get(listOfNames[idx])
            elements = (values.decode())[1:-1].split(",")
            eachD = dict()
            eachD["name"] = listOfNames[idx].decode()
            eachD["code"] = elements[0]
            eachD["open"] = elements[1]
            eachD["high"] = elements[2]
            eachD["low"] = elements[3]
            eachD["close"] = elements[4]
            dictResult.append(eachD)
        return JsonResponse({"result": dictResult})


class downloadWhole(APIView):
    def get(self, request):
        response = HttpResponse(
            content_type="text/csv",
        )
        response["Content-Disposition"] = 'attachment; filename="wholedownload.csv"'

        listOfName = SearchConfig.redis_instance.keys("*")
        # print(sorted(listOfName))
        writer = csv.writer(response)
        writer.writerow(["NAME", "CODE", "OPEN", "HIGH", "LOW", "CLOSE"])
        for idx, i in enumerate(listOfName):
            values = SearchConfig.redis_instance.get(listOfName[idx])
            elements = (values.decode())[1:-1].split(",")
            elements.insert(0, listOfName[idx].decode())
            writer.writerow(elements)

        return response


class downloadCurrent(APIView):
    def get(self, request):
        response = HttpResponse(
            content_type="text/csv",
        )
        response["Content-Disposition"] = 'attachment; filename="wholedownload.csv"'
        writer = csv.writer(response)
        writer.writerow(["NAME", "CODE", "OPEN", "HIGH", "LOW", "CLOSE"])
        searchtext = request.GET.get("search")
        listOfNames = SearchConfig.redis_instance.keys(searchtext + "*")
        for idx, i in enumerate(listOfNames):
            values = SearchConfig.redis_instance.get(listOfNames[idx])
            elements = (values.decode())[1:-1].split(",")
            elements.insert(0, listOfNames[idx].decode())
            writer.writerow(elements)
        return response
