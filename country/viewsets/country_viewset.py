from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from country.models import Country
from country.selectors import CountrySelector
from country.serializers import CountrySerializer


class CountryViewSet(viewsets.ViewSet):
    http_method_names = ["get", "post", "delete", "put", "patch"]
    model = Country
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        instance = CountrySelector.retrieve(pk)
        serializer = CountrySerializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        instances = CountrySelector.list({})
        serializer = CountrySerializer(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
