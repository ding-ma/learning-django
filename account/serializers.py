from rest_framework import serializers
from account.models import Account
from tutorials.serializers import TutorialSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        # registered_tutorials = TutorialSerializer(many=True)
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'date_joined',
            'last_login',
            'is_admin',
            'is_active',
            'is_staff',
            'is_superuser'
            # 'registered_tutorials'
        )
