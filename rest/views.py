from rest_framework import generics, views, status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from api import settings
import os


class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename):
        try:
            file_obj = request.FILES['file']
            file_ext = file_obj.content_type.split("/")[1]
            specific_folder = settings.MEDIA_ROOT + os.sep + file_ext

            if not os.path.exists(settings.MEDIA_ROOT):
                os.mkdir(settings.MEDIA_ROOT)
            if not os.path.exists(specific_folder):
                os.mkdir(specific_folder)

            f_path = specific_folder+os.sep+file_obj.name+"."+file_ext
            f_url = settings.BASE_URL + settings.MEDIA_URL + file_ext + \
                "/" + file_obj.name+"."+file_ext

            destination = open(f_path, 'wb+')

            for chunk in file_obj.chunks():
                destination.write(chunk)
            destination.close()

            return Response(f_url, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
