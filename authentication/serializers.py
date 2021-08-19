from django.contrib.auth.models import User, Group, Permission
from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, ValidationError
from .models import Profile, BankData, Enterprise


class PermissionsSerializer(ModelSerializer):

    class Meta:
        model = Permission
        fields = ['id', 'name']


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'name']


class BankDataSerializer(ModelSerializer):

    class Meta:
        model = BankData
        fields = ['id', 'profile', 'agencia', 'conta', 'digito']


class EnterpriseSerializer(ModelSerializer):

    class Meta:
        model = Enterprise
        fields = ['id', 'profile', 'name']


class ProfileSerializer(ModelSerializer):
    bank_data = BankDataSerializer(many=False, read_only=True)
    company = EnterpriseSerializer(
        many=False,
        read_only=True,
     )

    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'cpf', 'birth_date', 'company', 'bank_data']


class UserSerializer(ModelSerializer):
    groups = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    user_permissions = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    profile = ProfileSerializer(many=False, read_only=True)

    password = CharField(max_length=32, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password','groups', 'user_permissions', 'profile']

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise ValidationError({'email':('email already exists')})
        if User.objects.filter(username=username).exists():
            raise ValidationError({'username': ('username already exists')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

