from django.core.exceptions import FieldError
from django.db.models import Q
from django.http import QueryDict


class BaseSelector:
    fields_map = {}

    @classmethod
    def dynamic_filter(cls, queryset, search_params, order_by=None, limit=None):
        query_conditions = []

        if isinstance(search_params, QueryDict):
            items = search_params.lists()
        else:
            items = search_params.items()

        if "limit" in search_params:
            try:
                limit = int(search_params.get("limit"))
            except (ValueError, TypeError):
                limit = None

        for key, values in items:
            if key == "limit":
                continue
            query_key = cls.fields_map.get(key)
            if query_key:
                if query_key.endswith("__in"):
                    query_conditions.append(Q(**{query_key: values}))
                else:
                    if isinstance(values, list):
                        query_conditions.append(Q(**{query_key: values[0]}))
                    else:
                        query_conditions.append(Q(**{query_key: values}))
        try:
            filtered_queryset = queryset.filter(*query_conditions)
            if order_by:
                filtered_queryset = filtered_queryset.order_by(*order_by)
            if limit:
                filtered_queryset = filtered_queryset[:limit]
            return filtered_queryset
        except FieldError as e:
            print(f"Invalid field error: {e}")
            raise
