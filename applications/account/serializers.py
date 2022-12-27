from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=6, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm']

    def validate(self,attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('wrong password!')
        return attrs

    def validate_email(self,email):
        if User.objects.filter(email=email).exist():
            raise serializers.ValidationError('this email already exist!')
        return email

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)
    def validate(self, attrs):
        pass1 = attrs.get('new_password')
        pass2 = attrs.pop('new_password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('password doesnt match!')
        return attrs
    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data('new_password')
        user.set_password('password')
        user.save()
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self,email):
        if not User.objects.filter(email=email).exist():
            raise serializers.ValidationError('this email not exist!')
        return email

    def send_code(self):
        email = self.validated_data('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_confirmation_code(email, user.activation_code)

class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True,min_length=6)
    code = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exist():
            raise serializers.ValidationError('user is not register!')
        return email

    def validate_code(self,code):
        if not User.objects.filter(activation_code=code).exist():
            raise serializers.ValidationError('wrong code!')
        return code

    def validate(self,attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('wrong passwords')
        return attrs
    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()









