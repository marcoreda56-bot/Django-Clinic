from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView
from .views import (
    RegisterViewSet, DoctorListViewSet, DoctorSlotViewSet,
    DoctorAvailabilityViewSet, AppointmentViewSet, SpecialtyViewSet,
    DoctorProfileViewSet, UserViewSet, VerifyOTPView, PatientProfileViewSet
)
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(BaseTokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'doctors', DoctorListViewSet, basename='doctors')
router.register(r'slots', DoctorSlotViewSet, basename='slots')
router.register(r'availabilities', DoctorAvailabilityViewSet, basename='availabilities')
router.register(r'appointments', AppointmentViewSet, basename='appointments')
router.register(r'specialties', SpecialtyViewSet, basename='specialties')
router.register(r'users', UserViewSet, basename='user')
router.register(r'doctor-profiles', DoctorProfileViewSet, basename='doctor-profile')
router.register(r'patient-profiles', PatientProfileViewSet, basename='patient-profile')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
]