from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from country.models import Currency
from country.selectors import CurrencySelector
from country.serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ViewSet):
    http_method_names = ["get", "post", "delete", "put", "patch"]
    model = Currency
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        instance = CurrencySelector.retrieve(pk)
        serializer = CurrencySerializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        instances = CurrencySelector.list({})
        serializer = CurrencySerializer(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
