from django.utils import translation
from django.utils.deprecation import MiddlewareMixin

class UserLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user
        if user.is_authenticated and hasattr(user, 'language'):
            translation.activate(user.language)
            request.LANGUAGE_CODE = translation.get_language()
        else:
            result = "To translate to other language, it is neccesary to authenticate the user."
            print(result)
            translation.deactivate()