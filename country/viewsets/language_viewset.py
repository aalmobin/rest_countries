from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from country.models import Language
from country.selectors import LanguageSelector
from country.serializers import LanguageSerializer


class LanguageViewSet(viewsets.ViewSet):
    http_method_names = ["get", "post", "delete", "put", "patch"]
    model = Language
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        instance = LanguageSelector.retrieve(pk)
        serializer = LanguageSerializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        instances = LanguageSelector.list({})
        serializer = LanguageSerializer(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
