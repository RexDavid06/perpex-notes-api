from django.shortcuts import render
from .models import Note
from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

# Create your views here.
class NoteViewSet(ModelViewSet):
    queryset = Note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ users get access to only notes they made"""
        return Note.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        """ automatically sets the logged-in user as the owner"""
        serializer.save(owner=self.request.user)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key}, status=HTTP_201_CREATED
            )
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    


    






    






