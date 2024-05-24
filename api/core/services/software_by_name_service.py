from core.repositories.software_repository import SoftwareRepository


class SoftwareByNameService:
    def __init__(self, software_repository: SoftwareRepository):
        self.software_repository = software_repository

    def get_software_by_name(self, software_name: str):
        return self.software_repository.get_software_by_name(software_name)

    def put_software_by_name(self, software_name: str, validated_data: dict):
        return self.software_repository.put_software_by_name(software_name, validated_data)

    def patch_software_by_name(self, software_name: str, validated_data: dict):
        return self.software_repository.patch_software_by_name(software_name, validated_data)

    def delete_software_by_name(self, software_name: str):
        self.software_repository.delete_software_by_name(software_name)