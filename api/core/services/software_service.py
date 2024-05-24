from core.models import Software
from core.repositories.software_repository import SoftwareRepository


class SoftwareService:
    def __init__(self, software_repository: SoftwareRepository):
        self.software_repository = software_repository

    def post_software(self, validated_data):
        result = self.software_repository.create_software(validated_data)
        return result

    def get_all_software(self) -> list[Software]:
        return self.software_repository.get_all_software()

    def is_software_already_in_db(self, software_name: str) -> bool:
        return self.software_repository.is_software_already_exists(software_name)
