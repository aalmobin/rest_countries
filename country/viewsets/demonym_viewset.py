from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from country.models import Demonym
from country.selectors import DemonymSelector
from country.serializers import DemonymSerializer


class DemonymViewSet(viewsets.ViewSet):
    http_method_names = ["get", "post", "delete", "put", "patch"]
    model = Demonym
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        instance = DemonymSelector.retrieve(pk)
        serializer = DemonymSerializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        instances = DemonymSelector.list({})
        serializer = DemonymSerializer(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
