from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer, FollowSerializer, BlockSerializer
from users.models import CustomUser, Follow, Block


# @authentication_classes([])  # Empty list means no authentication classes
# @permission_classes([AllowAny])
class UserView(APIView):
    permission_classes = [IsAdminUser]

    # def get(self, request):
    #     users = CustomUser.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_staff:  # Assuming 'is_staff' indicates admin status
                users = CustomUser.objects.all()
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data)
            else:
                # Return limited information for non-admin users
                user_data = {
                    'id': request.user.id,
                    'username': request.user.username,
                    'email': request.user.email,
                    # Add other fields you want to include for non-admin users
                }
                return Response({'user': user_data})
        else:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=401)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class UserDetailsView(APIView):
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class FollowView(APIView):
    def get(self, request):
        follows = Follow.objects.all()
        serializer = FollowSerializer(follows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class FollowDetailsView(APIView):
    def get(self, request, follow_id):
        try:
            follow = Follow.objects.get(id=follow_id)
            serializer = FollowSerializer(follow)
            return Response(serializer.data)
        except Follow.DoesNotExist:
            return Response({"message": "Follow not found"}, status=status.HTTP_404_NOT_FOUND)


class BlockView(APIView):
    def get(self, request):
        blocks = Block.objects.all()
        serializer = BlockSerializer(blocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class BlockDetailsView(APIView):
    def get(self, request, block_id):
        try:
            block = Block.objects.get(id=block_id)
            serializer = BlockSerializer(block)
            return Response(serializer.data)
        except Block.DoesNotExist:
            return Response({"message": "Block not found"}, status=status.HTTP_404_NOT_FOUND)
