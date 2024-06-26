from django.db import models


class Software(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    version = models.CharField(max_length=10)
    description = models.TextField()
    license_number = models.CharField(max_length=30)
    developer_company = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name};{self.version};{self.developer_company};{self.license_number};{self.developer_company}"

