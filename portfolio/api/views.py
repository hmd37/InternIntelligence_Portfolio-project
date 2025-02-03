from rest_framework import generics
from .models import Project, Skill, Achievement, Contact
from .serializers import (
    ProjectSerializer,
    SkillSerializer,
    AchievementSerializer,
    ContactSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated



class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Project Views
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# Skill Views
class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


# Achievement Views
class AchievementListCreateView(generics.ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class AchievementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


# Contact Views
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
