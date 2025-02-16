# users/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .serializers import UserSerializer
from .storage import UserStorage

class UserListCreate(APIView):
    """List all users or create a new user."""
    
    def get(self, request):
        """List all users."""
        users = UserStorage.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Create a new user."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = UserStorage.create_user(user_data)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveUpdateDestroy(APIView):
    """Retrieve, update, or delete a user instance."""
    
    def get_object(self, pk):
        """Retrieve a user instance."""
        try:
            return UserStorage.get_user(pk)
        except KeyError:
            raise Exception("User not found")
    
    def get(self, request, pk):
        """Retrieve a user."""
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """Update a user."""
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            UserStorage.update_user(pk, user_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        """Partially update a user."""
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user_data = serializer.validated_data
            UserStorage.update_user(pk, user_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a user."""
        user = self.get_object(pk)
        UserStorage.delete_user(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)