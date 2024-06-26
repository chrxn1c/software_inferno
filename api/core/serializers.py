from rest_framework import serializers


class SoftwareSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    version = serializers.CharField(max_length=10)
    description = serializers.CharField()
    license_number = serializers.CharField(max_length=30)
    developer_company = serializers.CharField(max_length=30)


class SoftwarePatchRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    version = serializers.CharField(max_length=10, required=False)
    description = serializers.CharField(required=False)
    license_number = serializers.CharField(max_length=30, required=False)
    developer_company = serializers.CharField(max_length=30, required=False)


class APIErrorResponseSerializer(serializers.Serializer):
    description = serializers.CharField()
    code = serializers.CharField()
    exceptionName = serializers.CharField()
    exceptionMessage = serializers.CharField()
