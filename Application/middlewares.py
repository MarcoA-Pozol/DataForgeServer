from django.http import JsonResponse
import magic

class UploadDataValidationMiddleware:
    """
        Middleware: Validates the provided data by the user files being uploaded to be treated, checking for the files size and type as the extension.
        Besides, it checks automatically if the view is in the list of the allowed views that require this process, if not, then it just skip the validation process and let the view/request to continue with their natural workflow.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_views = ["first_view", "another_view"] # Views where the middleware should be executed.

    def __call__(self, request):
        """
            Validate file uploads provided by the user to be managed by the application.
        """
        # Get the view function name
        view_func = getattr(request.resolver_match, "func", None)
        view_name = getattr(view_func, "__name__", None)
        
        if not view_name in self.allowed_views:
            print("\n🚀 UploadedDataValidationMiddleware: Not neccesary uploaded data file validation for this view / request.\n")
            return self.get_response(request)
        else:
            if request.FILES:
                for file in request.FILES.values():
                    mime_type = magic.from_buffer(file.read(2048), mime=True) 
                    allowed_types = {"application/pdf", "application/vnd.ms-excel", "text/csv"}

                    if mime_type not in allowed_types:
                        return JsonResponse({"error": "Invalid file format!"}, status=400)
                    
                    if file.size > 5 * 1024 * 1024: # 5MB file size limit.
                        return JsonResponse({"error": "File is too large to be processed!"}, status=400)
                    
        return self.get_response(request)
        
        