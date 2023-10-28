from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Bio
from profiles.serializers import BioSerializer


# Create your views here.

class BioView(APIView):
    def get(self, request):
        bios = Bio.objects.all()
        serializer = BioSerializer(bios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BioDetailsView(APIView):
    def get(self, request, bio_id):
        try:
            bio = Bio.objects.get(id=bio_id)
            serializer = BioSerializer(bio)
            return Response(serializer.data)
        except Bio.DoesNotExist:
            return Response({"message": "bio not found"}, status=status.HTTP_404_NOT_FOUND)
