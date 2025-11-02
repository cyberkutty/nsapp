from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Walkin
from .serializers import WalkinSerializer

class WalkinViewSet(viewsets.ModelViewSet):
    queryset = Walkin.objects.all()
    serializer_class = WalkinSerializer

# registration

from rest_framework import viewsets, filters
from .models import SheelaRegistration
from .serializers import SheelaRegistrationSerializer

class SheelaRegistrationViewSet(viewsets.ModelViewSet):
    queryset = SheelaRegistration.objects.all().order_by('-id')
    serializer_class = SheelaRegistrationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'course', 'staff_name', 'enquire_product']


# lead
from rest_framework import viewsets
from .models import Lead
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by('-id')
    serializer_class = LeadSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from django.core.mail import send_mail

@api_view(['POST'])
def send_otp(request):
    discount = request.data.get('discount')
    course = request.data.get('course')
    otp = str(random.randint(1000, 9999))

    # Send OTP to admin email
    send_mail(
        subject="Discount OTP Verification",
        message=f"OTP for approving discount ({discount}%) on {course} course: {otp}",
        from_email="yourapp@gmail.com",
        recipient_list=["admin@gmail.com"],  # Change to your admin email
        fail_silently=False,
    )

    return Response({"success": True, "otp": otp})



from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer

# Signup
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# Login
class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            return Response({
                "message": "Login successful",
                "username": user.username,
                "role": user.role,
                "subRole": user.subRole or ""
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)




#technicals attendance
from rest_framework import viewsets, filters
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().order_by('-date')
    serializer_class = AttendanceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['staff', 'student_name', 'product', 'type']  # Searchable fields




from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsAdminOrReadCreate

from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Seminar
from .serializers import SeminarSerializer

class SeminarViewSet(viewsets.ModelViewSet):
    queryset = Seminar.objects.all().order_by('-id')
    serializer_class = SeminarSerializer

    def get_permissions(self):
        if self.action in ['list', 'create', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]  

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.order_by('-created_at')
    serializer_class = ActivitySerializer
    permission_classes = [IsAdminOrReadCreate]

    def get_queryset(self):
        qs = super().get_queryset()
        month = self.request.query_params.get('month')
        approved_only = self.request.query_params.get('approved', '1')
        if approved_only in ('1','true','True'):
            qs = qs.filter(approved=True)
        if month:
            qs = qs.filter(month=month)
        return qs
    




from .models import PendingService
from .serializers import PendingServiceSerializer

class PendingServiceViewSet(viewsets.ModelViewSet):
    queryset = PendingService.objects.all()
    serializer_class = PendingServiceSerializer