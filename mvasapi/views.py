from django.shortcuts import render
from django.shortcuts import redirect, render
from mvasapi.models import Transaction
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.all().order_by('id');
        context = {'transactions' : transactions}
        return render(request, "mvasapi/index.html", context)
    else:
        return redirect('/accounts/login/')


def api_test(request):
    payload = {'key1': 'value1', 'key2': 'value2'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data=payload)
    postdata = response.json()
    print(postdata)
    return JsonResponse(postdata)

def api_test_idv(request, id):
    # print(id)
    transactions = get_object_or_404(Transaction, id=id);
    if transactions.far_rate == 0:
        transactions.far_rate = ''

    data = {
        'username' : 'it@shinhan.com',
        'sandi_bank' : '2550',
        'data' : {
            'transaction_id' : transactions.transaction_id,
            'transaction_date' : transactions.transaction_date,
            'corporate_id' : transactions.corporate_id,
            'corporate_name' : transactions.corporate_name,
            'platform' : transactions.platform,
            'deal_type' : transactions.deal_type,
            'direction' : transactions.direction,
            'base_currency' : transactions.base_currency,
            'quote_currency' : transactions.quote_currency,
            'base_volume' : transactions.base_volume,
            'base_volume' : transactions.quote_volume,
            'periods' : transactions.periods,
            'near_rate' : transactions.near_rate,
            'far_rate' : transactions.far_rate,
            'near_value_date' : transactions.near_value_date,
            'far_value_date' : transactions.far_value_date,
            'confirmed_at' : transactions.confirmed_at,
            'confirmed_by' : transactions.confirmed_by,
            'trader_id' : transactions.trader_id,
            'trader_name' : transactions.trader_name,
            'transaction_purpose' : transactions.transaction_purpose
        }
    }

    headers = {'X-BI-Client-Id': 'test'}

    response = requests.post('https://api.bi.go.id/bi/sismontavar/sismontavar/data', data=data, headers=headers)
    # response = requests.post('https://reqres.in/api/users', json=data, headers=headers)
    postdata = response.json()
    print(response.status_code)
    # return JsonResponse(postdata)
    # return JsonResponse(postdata['httpCode'] ,safe=False)
    # return JsonResponse(dict(request.headers), safe=False)
    return JsonResponse(response.status_code, safe=False)




