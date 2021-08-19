from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BankDataSerializer, ProfileSerializer, UserSerializer,EnterpriseSerializer
from .models import BankData, Profile, Enterprise
from django.contrib.auth.models import User


class BankDataViewSet(ModelViewSet):
    queryset = BankData.objects.all()
    serializer_class = BankDataSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


