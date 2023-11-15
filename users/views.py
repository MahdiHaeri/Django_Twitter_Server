# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from users.serializers import UserSerializer, FollowSerializer, BlockSerializer
#
#
# class UserView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#
# class UserDetailsView(APIView):
#     def get(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         except User.DoesNotExist:
#             return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#
#
# class FollowView(APIView):
#     def get(self, request):
#         follows = Follow.objects.all()
#         serializer = FollowSerializer(follows, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = FollowSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#
# class FollowDetailsView(APIView):
#     def get(self, request, follow_id):
#         try:
#             follow = Follow.objects.get(id=follow_id)
#             serializer = FollowSerializer(follow)
#             return Response(serializer.data)
#         except Follow.DoesNotExist:
#             return Response({"message": "Follow not found"}, status=status.HTTP_404_NOT_FOUND)
#
#
# class BlockView(APIView):
#     def get(self, request):
#         blocks = Block.objects.all()
#         serializer = BlockSerializer(blocks, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BlockSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#
# class BlockDetailsView(APIView):
#     def get(self, request, block_id):
#         try:
#             block = Block.objects.get(id=block_id)
#             serializer = BlockSerializer(block)
#             return Response(serializer.data)
#         except Block.DoesNotExist:
#             return Response({"message": "Block not found"}, status=status.HTTP_404_NOT_FOUND)
