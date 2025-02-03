from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    SkillListCreateView,
    SkillRetrieveUpdateDestroyView,
    AchievementListCreateView,
    AchievementRetrieveUpdateDestroyView,
    ContactListCreateView,
    ContactRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Projects
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),

    # Skills
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillRetrieveUpdateDestroyView.as_view(), name='skill-detail'),

    # Achievements
    path('achievements/', AchievementListCreateView.as_view(), name='achievement-list-create'),
    path('achievements/<int:pk>/', AchievementRetrieveUpdateDestroyView.as_view(), name='achievement-detail'),

    # Contacts
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(), name='contact-detail'),
]
