# GlobalSearchFilter for MongoEngine & Django Rest Framework

## Overview
The default search filter backend in Django Rest Framework doesn’t work seamlessly with MongoEngine. To address this, I’ve developed a **GlobalSearchFilter**, a custom filter backend that allows flexible searching across specified fields in MongoEngine-based models.

This filter is designed to be customizable per view and can be used globally for any Django Rest Framework ViewSet.

## Key Features:
- **Flexible Search:** Enables search functionality across multiple fields with `icontains` query filtering.
- **Customizable Per View:** Easily specify the fields to be searched for each view.
- **MongoEngine Compatible:** Works with MongoEngine models and `Q` objects.
  
## How To Use
1. Add `GlobalSearchFilter` to your Django project:

```bash
from rest_framework.filters import BaseFilterBackend
from mongoengine import Q


class GlobalSearchFilter(BaseFilterBackend):
    """
    A custom search filter backend that applies search based on specified fields.
    Can be used globally and customized per view.
    """

    def filter_queryset(self, request, queryset, view):
        search_query = request.query_params.get('search', None)

        if not search_query:
            return queryset

        search_fields = getattr(view, 'search_fields', [])

        if not search_fields:
            return queryset

        queries = Q()
        for field in search_fields:
            if field:
                queries |= Q(**{f"{field}__icontains": search_query})

        return queryset.filter(queries)
```

2. Add `GlobalSearchFilter` to your Django project:
```
from global_search_filter import GlobalSearchFilter
from your_app import SampleModel

class SampleModelViewSet(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()  # Your own model
    serializer_class = SampleSerializer   # Your own serializer
    filter_backends = [GlobalSearchFilter]  # Import GlobalSearchFilter
    search_fields = ['name', 'description']  # Fields to search

# Customize the search fields as per your requirement

```
