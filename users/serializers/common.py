from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation, hashers

class UserSerializer(serializers.ModelSerializer):
    # Write only fields are onl used during de-serialization
    # password & password_confirmation will not be included in the serialized object when we query the user model
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        # 1. Remove password and password confirmation from the data dictionary
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        # 2. Compare password to password_confirmation, raise validation error if they don't match
        if password != password_confirmation:
            raise serializers.ValidationError({ 'password_confirmation': 'Passwords do not match.' })

        # 3. OPTIONAL use django's password validator method
        password_validation.validate_password(password)

        # 4. Hash the password, before adding it back onto the data dictionary
        data['password'] = hashers.make_password(password)

        # 5. Always return the data, manipulated or otherwise, at the end of the validate method
        return data


    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'is_staff', 'password', 'password_confirmation')
