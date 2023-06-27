from rest_framework import generics, views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.http import HttpResponse
from wsgiref.util import FileWrapper


class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request):
        file_obj = request.FILES['file']
        file_ext = file_obj.content_type.split("/")[1]
        destination = open(file_obj.name+"."+file_ext, 'wb+')

        for chunk in file_obj.chunks():
            destination.write(chunk)
        destination.close()

        return Response(status=204)
