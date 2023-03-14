from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from .models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import *

# UserProfile Model
class UserProfileListCreateView(ListCreateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]


# Category Model
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


# SubCategory Model
class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubCategoryCreateView(CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        category = self.request.category
        serializer.save(category=category)


class SubCategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAdminUser]


# API_ROOT
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'profiles': reverse('all-profiles', request=request, format=format),
        'categories': reverse('all-categories', request=request, format=format),
    })

