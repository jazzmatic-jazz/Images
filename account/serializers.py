from rest_framework import serializers
from .models import UserManager, User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserRegistrationSerializer(serializers.ModelSerializer):
    #we are writing this coz we need to confirm password field in our
    # registration request
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2']

        extra_kwargs={
            'password':{'write_only': True}
        }
    # Validating Password and confirm password while registration

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('Passwords does not match')
                
        return attrs

        
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'name']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255 ,style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255 ,style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password','password2']

    # now validate the password

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        # to access only the context from the views
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError('Passwords does not match')

        #need user as we dont have it in serializer,
        # we sending user here from the views.py in the context
        user.set_password(password)                
        user.save()
        return attrs
