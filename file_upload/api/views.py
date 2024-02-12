from django.db import transaction
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer

from .models import File
from .tasks import file_handling


class FileUploadView(APIView):
    parser_classes = [FormParser, MultiPartParser,]
    serializer_class = FileSerializer

    @transaction.atomic
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            transaction.on_commit(lambda: file_handling.delay(id=serializer.instance.id))
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class FileListView(APIView):
    serializer_class = FileSerializer

    def get(self, request):
        files = File.objects.all()
        serializer = self.serializer_class(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

