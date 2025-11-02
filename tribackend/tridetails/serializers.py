from rest_framework import serializers
from .models import PendingService, Walkin

class WalkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walkin
        fields = '__all__'

# registration
from rest_framework import serializers
from .models import SheelaRegistration

class SheelaRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SheelaRegistration
        fields = '__all__'

# lead
from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

# app/serializers.py
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role', 'subRole']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # ensure password is hashed
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)





# technical Attendance
from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'




from rest_framework import serializers
from .models import Activity
from .models import Seminar
from datetime import datetime



class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id','activity_type','auto_no','cost','phone_no','created_at','month','approved')
        read_only_fields = ('id','created_at','month','approved')

    def create(self, validated_data):
        # set month automatically as two-digit
        now = datetime.now()
        validated_data['month'] = str(now.month).zfill(2)
        return super().create(validated_data)
    




class PendingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingService
        fields = "__all__"