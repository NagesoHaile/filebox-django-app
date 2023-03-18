from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PersonalInfoSerializer
from .models import PersonalInfo
# Create your views here.
@api_view(["GET"])
def home(request):
    data = [
       {
        'name':'Nageso',
        'age': 22,
       },
         {
        
        'name':'thomy',
        'age': 22,
       },
         {
        'name':'donny',
        'age': 22,
       },
    ]
    return Response(data)

@api_view(['GET'])
def getPersonalInfos(request):
    personalInfos = PersonalInfo.objects.all()
    serializer = PersonalInfoSerializer(personalInfos,many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def getPersonalInfo(request,pk):
    personalInfo = PersonalInfo.objects.get(id=pk)
    serializer = PersonalInfoSerializer(personalInfo,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPersonalInfo(request):
    serializer = PersonalInfoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updatePersonalInfo(request,pk):
    data = request.data
    personalInfo = PersonalInfo.get(id=pk)
    serializer = PersonalInfoSerializer(instance=personalInfo,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE'])
def deletePersonalInfo(request,pk):
    personalInfo = PersonalInfo.objects.get(id=pk)
    personalInfo.delete()
    return Response('Information was deleted')   