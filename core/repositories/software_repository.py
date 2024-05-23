from core.models import Software
from core.repositories.database_module.execute_query import execute_query
from core.repositories.database_module.setup_database import setup_database
from django.conf import settings


class SoftwareRepository:
    def __init__(self):
        setup_database(settings.BASE_DIR)

    def create_software(self, validated_data):
        return execute_query(
            """INSERT INTO software (name, version, description, license_number, developer_company) VALUES (?, ?, ?, ?, ?);""",
            (validated_data['name'], validated_data['version'], validated_data['description'],
             validated_data['license_number'],
             validated_data['developer_company'])
        )

    def get_all_software(self) -> list[Software]:
        result = execute_query("""SELECT * FROM software;""")
        return list(
            map(lambda software: Software(software[0], software[1], software[2], software[3], software[4]), result))

    def is_software_already_exists(self, software_name: str) -> bool:
        result = execute_query("SELECT * FROM software WHERE name = ?", (software_name,))
        if len(result) == 0:
            return False
        return True

    def get_software_by_name(self, software_name: str) -> Software:
        result = execute_query("SELECT * FROM software WHERE name = ?", (software_name,))
        if len(result) == 0:
            return None

        return list(
            map(lambda software: Software(software[0], software[1], software[2], software[3], software[4]), result))[0]

    def put_software_by_name(self, software_name: str, validated_data: dict) -> Software:
        result = execute_query("UPDATE software SET name = ?, version = ?, description = ?, license_number = ?, developer_company = ? WHERE name = ?",
                               (validated_data['name'], validated_data['version'], validated_data['description'], validated_data['license_number'], validated_data['developer_company'],
                                software_name))
        return Software(**validated_data)

    def patch_software_by_name(self, software_name: str, validated_data: dict) -> Software:
        gotten_software = self.get_software_by_name(software_name)

        new_software_name = validated_data.get('name', None) or gotten_software.name
        new_software_version = validated_data.get('version', None) or gotten_software.version
        new_software_description = validated_data.get('description', None) or gotten_software.description
        new_software_license_number = validated_data.get('license_number', None) or gotten_software.license_number
        new_software_developer_company = validated_data.get('developer_company', None) or gotten_software.developer_company

        print(new_software_name)
        result = execute_query("UPDATE software SET name = ?, version = ?, description = ?, license_number = ?, developer_company = ? WHERE name = ?",(
            new_software_name,
            new_software_version,
            new_software_description,
            new_software_license_number,
            new_software_developer_company,
            new_software_name))

        return self.get_software_by_name(new_software_name)

    def delete_software_by_name(self, software_name: str):
        result = execute_query("DELETE FROM software WHERE name = ?", (software_name,))


