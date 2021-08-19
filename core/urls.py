from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import UserViewSet, BankDataViewSet, ProfileViewSet, CompanyViewSet
from authentication.token import MyTokenObtainPairView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bank_data', BankDataViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'company', CompanyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('djoser.urls.base')),
    # path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
]
