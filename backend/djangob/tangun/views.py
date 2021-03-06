from django.shortcuts import render
import os
import json
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tangun.models import MainList, Level, Fee, Payments
from django.views.decorators.csrf import ensure_csrf_cookie
 
@csrf_exempt
def send_data_list(request):
  data_front = json.loads(request.body)

  fee_list = Fee()
  main_list = MainList()
  main_list.first_name = data_front['name']
  main_list.last_name = data_front['surname']
  main_list.date_of_birth = data_front['birthdate']
  main_list.sex = data_front['sex']
  main_list.level = Level.objects.get(kup=data_front['level'])
  
  main_list.save()
  
  fee_list.player_id = main_list
  fee_list.save()

  response = JsonResponse({'code': 1})
  return response

@csrf_exempt
def get_data_list(request):

  main_list = MainList.objects.all().values()

  data_to_front = []
  for mlist in main_list:
    level = Level.objects.get(id=mlist['level_id']).kup
    data_to_front += [{
      'player_id':mlist['id'],
      'first_name':mlist['first_name'],
      'last_name':mlist['last_name'],
      'date_of_birth':mlist['date_of_birth'],
      'sex':mlist['sex'],
      'level':level,
    }]
  
  response = JsonResponse({'data': data_to_front})
  return response

@csrf_exempt
def get_data_fee(request):

  fee_list = Fee.objects.all().values()

  data_to_front = []
  for fee in fee_list:
    data_to_front += [{
      'id': fee['player_id_id'],
      'first_name': MainList.objects.get(id=fee['player_id_id']).first_name,
      'last_name': MainList.objects.get(id=fee['player_id_id']).last_name,
      'january': fee['january'],
      'february': fee['february'],
      'march': fee['march'],
      'april': fee['april'],
      'may': fee['may'],
      'june': fee['june'],
      'september': fee['september'],
      'october': fee['october'],
      'november': fee['november'],
      'december': fee['december'],
    }]

  response = JsonResponse({'data': data_to_front})
  return response

@csrf_exempt
def get_data_payment_custom(request):
  data_front = json.loads(request.body)

  player = MainList.objects.get(id=data_front)
  payment_list = Payments.objects.filter(player_id=player).values()

  response = JsonResponse({'data': list(payment_list)})
  return response

@csrf_exempt
def send_data_fee(request):
  data_front = json.loads(request.body)

  for data in data_front:
    fee = Fee.objects.get(player_id=data['id'])
    fee.january = data['january']
    fee.february = data['february']
    fee.march = data['march']
    fee.april = data['april']
    fee.may = data['may']
    fee.june = data['june']
    fee.september = data['september']
    fee.october = data['october']
    fee.november = data['november']
    fee.december = data['december']
    fee.save()


  response = JsonResponse({'code': 1})
  return response

@csrf_exempt
def save_custom_payments(request):
  data_front = json.loads(request.body)

  from_db = Payments.objects.filter(player_id_id=data_front['id'])

  for month in data_front['monthsSelected']:
    for el in from_db:
      if str(el.year) == str(data_front['year']):
        if str(el.month) == month:
          el.value = data_front['value']
          el.save()

  response = JsonResponse({'code': 1})
  return response

#########_FILL_PAYMENTS_START_#########
@csrf_exempt
def fill_payments(request):
  code = 1
  try:
    main_list = MainList.objects.all().values()
    const_fee = 80
    const_year = 2020
    const_months = ['I','II','III','IV','V','VI','IX','X','XI','XII']

    for el in main_list:
      player_id = el['id']
      for month in const_months:
        if not Payments.objects.filter(player_id=player_id,month=month,year=const_year).exists():
          payments = Payments()
          payments.value = const_fee
          payments.month = month
          payments.year = const_year
          payments.player_id = MainList.objects.get(id=player_id)
          payments.save()
          # print('zapisano',player_id,month,const_year)

    code = 0

  except:
    code = 1

  response = JsonResponse({'code': code})
  return response
  #########_FILL_PAYMENTS_END_#########