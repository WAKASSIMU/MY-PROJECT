from django.shortcuts import render
from rest_framework.decorators import api_view
from.models import*
from.serializers import*
from rest_framework import Response
# Create your views here.
@api_view (['GET'])
def getChairperson(request):
    Chairperson.object.all ()
    serializer = ChairpersonSerializer (Chairperson, many=True)
    return Response (serializer.data)
