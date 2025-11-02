from django.urls import path, include
from rest_framework import routers
from .views import (
    PendingServiceViewSet, WalkinViewSet, LeadViewSet,
    SheelaRegistrationViewSet, send_otp,
    UserViewSet, LoginViewSet,
    AttendanceViewSet, SeminarViewSet, ActivityViewSet
)

router = routers.DefaultRouter()
router.register(r'walkins', WalkinViewSet)
router.register(r'sheela-registrations', SheelaRegistrationViewSet, basename='sheela-registration')
router.register(r'leads', LeadViewSet)
router.register(r'users', UserViewSet, basename='user')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register('seminars', SeminarViewSet, basename='seminar')
router.register(r'pending-services', PendingServiceViewSet, basename='pending-service')

urlpatterns = [
    path('api/', include(router.urls)),
    path('send-otp/', send_otp, name='send-otp'),
    path('api/login/', LoginViewSet.as_view({'post': 'create'})),  # better for login
]
