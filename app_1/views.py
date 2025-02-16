from django.shortcuts import render
from django.views import View
import requests


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html', {})

    def post(self, request):
        return render(request, 'index.html', {})


def time_api_call(request):
    url = 'https://worldtimeapi.org/api/timezone/Asia/Tehran'
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.get(url)
        if response.status_code == 200:
            transactions = response.json()
            if transactions['datetime']:
                return render(request, 'index.html', {"datetime": transactions['datetime']})
            else:
                return []
        else:
            return []

    except Exception as e:
        print('error', 'get_transactions_by_month - ' + str(e))
        return None

    # {
    #   "name": "سورن",
    #   "moshakhasat": "ELX سال",
    #   "karkhane": "82,558,000",
    #   "bazar": "91,000,000"
    # },


def car_price_api(request):
    url = 'http://api.codebazan.ir/car-price/'
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.get(url)
        if response.status_code == 200:
            transactions = response.json()
            if transactions['Result']:
                list = transactions['Result']
                if request.GET.get('id'):
                    id = request.GET.get('id')
                    i = list[int(id)]
                    return render(request, 'index.html', {"name": i['name'],
                                                          "moshakhasat": i['moshakhasat'],
                                                          "karkhane": i['karkhane'],
                                                          "bazar": i['bazar']})
                for i in list:
                    if i['name'] == 'قیمت رانا پلاس':
                        return render(request, 'index.html', {"name": i['name'],
                                                              "moshakhasat": i['moshakhasat'],
                                                              "karkhane": i['karkhane'],
                                                              "bazar": i['bazar']})
            else:
                return []
        else:
            return []

    except Exception as e:
        print('error', 'get_transactions_by_month - ' + str(e))
        return None
