from rest_framework import serializers

from .models import Client, Note

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'name',
            'contact_person',
            'email',
            'phone',
            'website',
            'created_at',
            'modified_at',
        )

# fieldsの場合　This field is required 入力必須のエラー  read_only_fieldsに入れると必須回避
# フロントのformにある項目はfieldsでOK　ないのはread_only_fields、 viewsのオーバーライドで回避する

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'name',
            'body',
        )