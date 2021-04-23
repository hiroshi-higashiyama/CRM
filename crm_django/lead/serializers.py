from rest_framework import serializers

from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'created_at',
            'modified_at',
        )

# fieldsの場合　This field is required 入力必須のエラー  read_only_fieldsに入れると必須回避
# フロントのformにある項目はfieldsでOK　ないのはread_only_fields、 viewsのオーバーライドで回避する