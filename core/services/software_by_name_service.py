from core import models


class SoftwareByNameService:

    @staticmethod
    def get_software_by_name(software_name: str):
        software = models.Software.objects.filter(name=software_name).values().first()
        return software

    @staticmethod
    def put_software_by_name(software_name: str, validated_data: dict):
        software = models.Software.objects.filter(name=software_name).update(**validated_data)
        return software

    @staticmethod
    def patch_software_by_name(software_name: str, validated_data: dict):
        patched_software = models.Software.objects.filter(name=software_name).update(**validated_data)
        new_software_name = validated_data.get('name') or software_name
        return models.Software.objects.filter(name=new_software_name).values().first()

    @staticmethod
    def delete_software_by_name(software_name: str):
        models.Software.objects.filter(name=software_name).delete()
