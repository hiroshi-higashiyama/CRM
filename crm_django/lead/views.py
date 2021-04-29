from django.shortcuts import render

from rest_framework import viewsets

from team.models import Team

from .models import Lead
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(member__in=[self.request.user]).first()

        return self.queryset.filter(team=team)


"""
リクエストしたUserが自身のデータだけ取得できるようオーバーライド
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

postするときcreated_byは入力必須であるため、リクエストユーザーをセットしてセーブするようにオーバーライド
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

first()を使う理由
filterはリストを取得するのでfirstで指定する
"""