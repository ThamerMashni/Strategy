from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .services.courier import Courier
from .services.AramexStrategy import AramexStrategy
from .services.SmsaStrategy import SmsaStrategy
from .data.waybill import DefaultWaybill
from .data.person import Person

from rest_framework.decorators import api_view 
# Create your views here.
validStrats = ['aramex','smsa']

@api_view(['POST'])
def createWaybill(request, strategy):
    if strategy not in validStrats:
        return Response("Unknown strategy!",status= status.HTTP_400_BAD_REQUEST)
    else:
        shipper = Person()
        shipper.name = 'Ali'
        customer = Person()
        customer.name = 'Thamer'
        
        waybill = DefaultWaybill(shipper=shipper, customer=customer,items=None,sentDate=None )

        if strategy == validStrats[0]: 
            courier = Courier(strategy=AramexStrategy())
            res = courier.create_waybill(waybill)
            return Response(f'createWaybill called strat: {strategy}, response: {res}', status=status.HTTP_200_OK)
        
        elif strategy == validStrats[1]:
            courier = Courier(strategy=SmsaStrategy())
            res = courier.create_waybill(waybill)
            return Response(f'createWaybill called strat: {strategy}, response: {res}', status=status.HTTP_200_OK)
        
@api_view(['POST'])
def printWaybill(request, strategy):
    if strategy not in validStrats:
        return Response("Unknown strategy!",status= status.HTTP_400_BAD_REQUEST)
    else:
        if strategy == validStrats[0]: 
            courier = Courier(strategy=AramexStrategy())
            res = courier.print_waybill("sampleAwb")
            return Response(f'printWaybill called strat: {strategy}, response: {res}', status=status.HTTP_200_OK)

        elif strategy == validStrats[1]:
            courier = Courier(strategy=SmsaStrategy())
            res = courier.print_waybill("sampleAwb")
            return Response(f'printWaybill called strat: {strategy}, response: {res}', status=status.HTTP_200_OK)

@api_view(['POST'])
def trackShipment(request, strategy):
    if strategy not in validStrats:
        return Response("Unknown strategy!",status= status.HTTP_400_BAD_REQUEST)
    else:
        if strategy == validStrats[0]: 
            courier = Courier(strategy=AramexStrategy())
            res = courier.track_shipment("sampleAwb")
            return Response(f'trackShipment called strat: {strategy}, response: {res}', status=status.HTTP_200_OK)
            
        elif strategy == validStrats[1]:
            courier = Courier(strategy=SmsaStrategy())
            res = courier.track_shipment("sampleAwb")
            return Response(f'trackShipment called strat: {strategy}, response: {res}', status=status.HTTP_200_OK)
