from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .storage import UserStorage  # Ensure this is imported correctly

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        """List all users."""
        users = UserStorage.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Create a new user."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = UserStorage.create_user(user_data)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve a single user."""
        user = UserStorage.get_user(pk)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Update a user."""
        user_data = request.data
        user = UserStorage.update_user(pk, user_data)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """Delete a user."""
        success = UserStorage.delete_user(pk)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)