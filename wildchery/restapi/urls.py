from django.urls import include, path

# from .views import UserProfileListCreateView, userProfileDetailView
from .views import *


urlpatterns = [
    path('', api_root),
    # Profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
    # Category
    path("all-categories", CategoryListView.as_view(), name="all-categories"),
    path("new-category", CategoryCreateView.as_view(), name="new-category"),
    path("category/<int:pk>", CategoryDetailView.as_view(), name="category"),
    # SubCategory
    path("all-subcategories", SubCategoryListView.as_view(), name="all-subcategories"),
    path("new-subcategories", SubCategoryCreateView.as_view(), name="new-subcategory"),
    path("subcategory/<int:pk>", SubCategoryDetailView.as_view(), name="subcategory"),
]

