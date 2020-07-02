from django.shortcuts import render
from saynotoxic import model_prediction
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status
from .models import apiqueryDB
from .serializers import apiSerializers
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.
class APiViewSet(viewsets.ModelViewSet):
    queryset=apiqueryDB.objects.all()
    serializer_class=apiSerializers
@api_view(['POST'])
def predict(request):
    try:
        my_data=request.data
        user_text=str(my_data['text'])
        #print(str(my_data['text']))
        result=model_prediction.get_prediction(user_text)
        return JsonResponse(result,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
