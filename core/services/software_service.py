from rest_framework import status
from rest_framework.exceptions import ValidationError

from core import models
from core.models import Software


class SoftwareService:
    @staticmethod
    def post_software(serialized_request):
        created_software = models.Software.objects.create(**serialized_request)
        return created_software

    @staticmethod
    def get_all_software():
        software = models.Software.objects.all().values()
        return {"total_count": len(software), "software": software}

    @staticmethod
    def is_software_already_in_db(software_name: str):
        return Software.objects.filter(name=software_name).exists()
