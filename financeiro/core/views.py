from rest_framework import generics
from .models import Transacao
from .serializers import TransacaoSerializer

class TransacaoListCreate(generics.ListCreateAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
