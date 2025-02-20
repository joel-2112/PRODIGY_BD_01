# users/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .storage import UserStorage

class UserListCreate(APIView):
    #this is for get al users in-memory
    def get(self, request):
        users = UserStorage.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    #to add users to memory
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = UserStorage.create_user(user_data)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveUpdateDestroy(APIView):
    
    def get_object(self, pk):
        try:
            return UserStorage.get_user(pk)
        except KeyError:
            raise Exception("User not found")
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            UserStorage.update_user(pk, user_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user_data = serializer.validated_data
            UserStorage.update_user(pk, user_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        UserStorage.delete_user(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)