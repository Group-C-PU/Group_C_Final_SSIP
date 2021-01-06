from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import requests

def calender_Holiday(request):
        endpoint = 'https://date.nager.at/api/v2/publicholidays/2021/ID'
        response = requests.get(endpoint)
        data = response.json()
        context = {
            'datas':data,
        }
        return render(request,'holiday_list/holiday_list.html',context=context)