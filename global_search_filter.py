from rest_framework.filters import BaseFilterBackend
from mongoengine import Q


class GlobalSearchFilter(BaseFilterBackend):
    """
    A custom search filter backend that applies search based on specified fields.
    Can be used globally and customized per view.
    """

    def filter_queryset(self, request, queryset, view):
        # Retrieve the search query parameter
        search_query = request.query_params.get('search', None)

        if not search_query:
            return queryset

        # Get search fields from view or use an empty list if not provided
        search_fields = getattr(view, 'search_fields', [])

        if not search_fields:
            return queryset  # No fields to search on

        # Build the query using Q objects for each search field
        queries = Q()
        for field in search_fields:
            if field:  # Check if field is not empty
                queries |= Q(**{f"{field}__icontains": search_query})

        # Filter the queryset using the built query
        return queryset.filter(queries)