# Model
from . models import UserLog
# Responses
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
# Requests
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsSuperuser
# Pagination
from rest_framework.pagination import PageNumberPagination
# Serializers
from . serializers import UserLogSerializer
Files
# Files
import csv
import tempfile

# Paginator class
class CustomPaginator(PageNumberPagination):
    page_size = 50 # Rows per page
    page_size_query_param = 'page_size'
    max_page_size=100

class GetUsersLogsAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    paginator = CustomPaginator()
    response_type = request.GET.get('response_type')
    
    
    def get(self, request):
        model = UserLog
        page = request.GET.get('page')
        
        # Fetch every row from database (neccesity for performance improvement wether saving it in cache with Redis and obtain from, or use another way like a normal SQL query fetching the range of pagination depending the provided page)
        try:
            try:
                queryset = model.objects.all().order_by('id')
                paginated_data = paginator.paginate_queryset(queryset, request.GET.get('page'))
                serializer = UserLogSerializer(paginated_data, many)
            except Exception as e:
                return Response({'error':f'An error ocurred during fetching, paginating and serializing data from database: {e}'})
            
            if response_type == 'file':
                # Create a temporary csv file
                temp_file = tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False)
                writer = csv.writer(temp_file)
                # CSV header
                writer.writerow(['ID', 'User', 'Detail', 'Tag', 'CreatedAt']) 
                # Insert data on CSV
                for obj in queryset:
                    writer.writerow([obj.id, obj.name, obj.value])

                temp_file.seek(0)  # Go to start of file
                response = FileResponse(open(temp_file.name, 'rb'), as_attachment=True, filename='users_logs_export.csv')
                return response
            serializer = YourModelSerializer(paginated_data, many=True)
            response = paginator.get_paginated_response(serializer.data)
            return response     
        except Exception as e:
            return Response({'error':f'An unexpected error ocurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
