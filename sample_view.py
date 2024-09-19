from global_search_filter import GlobalSearchFilter

class SampleModelViewSet(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()  # Your own model
    serializer_class = SampleSerializer   # Your own serializer
    filter_backends = [GlobalSearchFilter]  # Import GlobalSearchFilter
    search_fields = ['name', 'description']  # Fields to search

# Customize the search fields as per your requirement
