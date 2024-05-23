from rest_framework import status
from rest_framework.exceptions import ValidationError

from core import models
from core.models import Software
from core.repositories.software_repository import SoftwareRepository
from core.serializers import SoftwareSerializer


class SoftwareService:
    def __init__(self, software_repository: SoftwareRepository):
        self.software_repository = software_repository

    def post_software(self, validated_data):
        result = self.software_repository.create_software(validated_data)
        # created_software = models.Software.objects.create()
        return result

    def get_all_software(self) -> list[Software]:
        # software = models.Software.objects.all().values()
        return self.software_repository.get_all_software()

    def is_software_already_in_db(self, software_name: str) -> bool:
        # return Software.objects.filter(name=software_name).exists()
        return self.software_repository.is_software_already_exists(software_name)
