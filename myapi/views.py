from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

from rest_framework import viewsets

from .serializers import CiscoSerializer, RegistrationSerializer
from crudapp.models import CiscoModel
from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token



# class CiscoViewSet(viewsets.ModelViewSet):
#     queryset = CiscoModel.objects.all().order_by('sapid')
#     serializer_class = CiscoSerializer

@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def api_detail_cisco_view(request, sapid):
	try:
		cisco_obj = CiscoModel.objects.get(sapid=sapid)
	except CiscoModel.DoesNotExist as e:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		serializer = CiscoSerializer(cisco_obj)
		return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((permissions.AllowAny,))
def api_update_cisco_view(request, sapid):
	try:
		cisco_obj = CiscoModel.objects.get(sapid=sapid)
	except CiscoModel.DoesNotExist as e:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'PUT':
		serializer = CiscoSerializer(cisco_obj, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data["message"] = "update successful"
			return Response(data=data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



@api_view(['DELETE',])
@permission_classes((permissions.AllowAny,))
def api_delete_cisco_view(request, sapid):
	try:
		cisco_obj = CiscoModel.objects.get(sapid=sapid)
	except CiscoModel.DoesNotExist as e:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'DELETE':
		is_deleted =  cisco_obj.delete()
		data = {}

		if is_deleted:
			data['message'] = 'delete successful'
		else:
			data['message'] = 'delete failed'

		return Response(data=data)


@api_view(['POST',])
@permission_classes((permissions.AllowAny,))
def api_create_cisco_view(request):
	if request.method == 'POST':
		serializer = CiscoSerializer(data=request.data)
		data = {}

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def registration_view(request):

	if request.method == 'POST':
		data = {}
		serializer = RegistrationSerializer(data=request.data)
		if serializer.is_valid():
			user_obj =  serializer.save()
			data['message'] =  'Registered successfully'
			data['email'] = user_obj.email
			data['username'] = user_obj.username
			token = Token.objects.get(user=user_obj).key
			data['token'] = token
		else:
			data = serializer.errors

		return Response(data)