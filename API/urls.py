from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from API.views import UserViewSet, UserUsernamesAPIView, UserAuthenticationAPIView, UserRegisteringAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define API schema (Documentation)
schema_view = get_schema_view(
    openapi.Info(
        title="DataForge API",
        default_version="v1",
        description="DataForge API documentation for users, contributors and much more about.",
        terms_of_service="https://github.com/MarcoA-Pozol/DataForgeServer.git",
        contact=openapi.Contact(email="marcoantoniopozolnarciso@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny], # Anyone on the internet can get acess to the API documentation when server´s running.
    authentication_classes=[],  # Disable session authentication in Swagger
)

# ViewSet based routers
router = DefaultRouter()
router.register('users', UserViewSet, 'api-users')
# router.register('path', AnotherViewSet, 'path-name')
# router.register('path', AnotherViewSet, 'path-name')

# Routes
urlpatterns = [
    # Endpoints
    path('users/', include(router.urls)),
    path('users-usernames/', UserUsernamesAPIView.as_view(), name='api-users-usernames'),
<<<<<<< HEAD
    # Authentication
    path('user-registering/', UserRegisteringAPIView.as_view(), name='api-user-registering'),
    path('users-authentication/', UserAuthenticationAPIView.as_view(), name='api-user-authentication'),
    # JWT Authentication Token Pair Generation and Refresh Token
=======
    # JWT Token Pair Generation and Refresh Token
>>>>>>> 229fb7cdcad77f191b3b7b45a710077f1b748c68
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    # API documentation with swagger and redoc
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='redoc-docs'),
]
