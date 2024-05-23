from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from core.serializers import SoftwareSerializer, APIErrorResponseSerializer, SoftwarePatchRequestSerializer
from core.services.software_by_name_service import SoftwareByNameService
from core.services.software_service import SoftwareService


# Create your views here.

class SoftwareViewSet(viewsets.ViewSet):
    software_service = SoftwareService()
    software_by_name_service = SoftwareByNameService()

    def create(self, request, *args, **kwargs):
        serializer = SoftwareSerializer(data=request.data)

        if not serializer.is_valid():
            error_response_data = {
                "description": "Error while creating software",
                "code": 422,
                "exceptionName": "Unprocessable Entity",
                "exceptionMessage": "Required fields are missing or invalid"
            }
            return Response(error_response_data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if self.software_service.is_software_already_in_db(serializer.validated_data["name"]):
            error_response_data = {
                "description": "Error while creating software",
                "code": 400,
                "exceptionName": "Bad Request",
                "exceptionMessage": "Current software already exists"
            }
            return Response(error_response_data, status=status.HTTP_400_BAD_REQUEST)

        self.software_service.post_software(serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        if request.query_params:
            error_response_data = {
                "description": "Error while getting all software",
                "code": 400,
                "exceptionName": "Bad Request",
                "exceptionMessage": "Query Parameters are not allowed during this operation"
            }
            return Response(error_response_data, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.software_service.get_all_software(), status=status.HTTP_200_OK)

    def retrieve(self, request, software_name, *args, **kwargs):
        if request.data:
            error_response_data = {
                "description": "Error while getting chosen software",
                "code": 422,
                "exceptionName": "Unprocessable Entity",
                "exceptionMessage": "Required fields are missing or invalid. Take into consideration that you only "
                                    "need a software name in url"
            }
            return Response(error_response_data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        software = self.software_by_name_service.get_software_by_name(software_name)
        if not software:
            error_response_data = {
                "description": "Error while getting chosen software",
                "code": 400,
                "exceptionName": "Bad Request",
                "exceptionMessage": "Chosen software not found"
            }
            return Response(error_response_data, status=status.HTTP_400_BAD_REQUEST)

        return Response(software, status=status.HTTP_200_OK)

    def update(self, request, software_name, *args, **kwargs):
        serializer = SoftwareSerializer(data=request.data)

        if not serializer.is_valid():
            error_response_data = {
                "description": "Error while putting software",
                "code": 422,
                "exceptionName": "Unprocessable Entity",
                "exceptionMessage": "Required fields are missing or invalid. Take into consideration that you need "
                                    "full body"
            }
            return Response(error_response_data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not self.software_service.is_software_already_in_db(software_name):
            error_response_data = {
                "description": "Error while putting software",
                "code": 400,
                "exceptionName": "Bad Request",
                "exceptionMessage": "Current software does not exist to be putted"
            }
            return Response(error_response_data, status=status.HTTP_400_BAD_REQUEST)

        self.software_by_name_service.put_software_by_name(software_name, serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, software_name, *args, **kwargs):
        put_serializer = SoftwarePatchRequestSerializer(data=request.data)
        if not put_serializer.is_valid():
            error_response_data = {
                "description": "Error while patching software",
                "code": 422,
                "exceptionName": "Unprocessable Entity",
                "exceptionMessage": "Required fields are invalid. Check the models"
            }

        if not self.software_service.is_software_already_in_db(software_name):
            error_response_data = {
                "description": "Error while patching software",
                "code": 400,
                "exceptionName": "Bad Request",
                "exceptionMessage": "Current software does not exist to be patched"
            }

        patched_software = self.software_by_name_service.patch_software_by_name(software_name, put_serializer.validated_data)
        return Response(patched_software, status=status.HTTP_201_CREATED)

    def destroy(self, request, software_name, *args, **kwargs):
        if request.data:
            error_response_data = {
                "description": "Error while deleting software",
                "code": 422,
                "exceptionName": "Unprocessable Entity",
                "exceptionMessage": "Required fields are missing or invalid. Take into consideration that you only "
                                    "need a software name in url"
            }
            return Response(error_response_data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not self.software_service.is_software_already_in_db(software_name):
            error_response_data = {
                "description": "Error while deleting software",
                "code": 404,
                "exceptionName": "Bad Request",
                "exceptionMessage": "Current software does not exist to be deleted"
            }
            return Response(error_response_data, status=status.HTTP_400_BAD_REQUEST)

        software = self.software_by_name_service.delete_software_by_name(software_name)
        return Response(status=status.HTTP_200_OK)
