from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from file.models import File
from file.serializers import FileSerializer, FileUploadSerializer


class FileListAPIView(ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
