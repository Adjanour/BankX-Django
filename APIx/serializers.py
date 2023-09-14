from rest_framework import serializers
from Accounts.models import Account,User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id','account_number','account_type','user_id')
        many = True