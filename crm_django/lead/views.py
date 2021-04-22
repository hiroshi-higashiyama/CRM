from django.shortcuts import render

from rest_framework import viewsets

from .models import Lead
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    # 作成したUserがデータを取得できるようオーバーライド
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    # postするときcreated_byは入力必須であるため、リクエストユーザーをセットしてセーブするようにオーバーライド
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

