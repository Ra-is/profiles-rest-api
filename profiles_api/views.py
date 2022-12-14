from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticated


from . import permissions

from . import models

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Users HTTP methods ad function (get, post, put, patch, delete)'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request, format=None):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """handle partial update an object"""
        return Response({'method':'Patch'})

    def delete(self, request, pk=None):
        """handle delete object"""
        return Response({'method':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """Api for viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """Return Hello mgs"""
        view_set = [
        'Users action (list, create, retrieve, update, destroy)'
    ]
        return Response({'message':'Hello','a_vieset':view_set})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its id"""
        return Response({'method':'Retrieve'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'put'})
    
    def partial_update(self,request,pk=None):
        """Handle updating partially an object"""
        return Response({'method':'patch'})
    
    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'method':'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handles creating of feed its"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
        
        )
    
    def perform_create(self, serializer):
        """sets the user profile to the login in user"""
        serializer.save(user_profile=self.request.user)
        







 






        
        