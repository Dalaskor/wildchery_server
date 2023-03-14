from django.urls import include, path
from .views import *


urlpatterns = [
    path('', api_root),
    # Profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
    # Category
    path("all-categories", CategoryListView.as_view(), name="all-categories"),
    path("all-categories/<int:pk>", CategoryRetrieveView.as_view(), name="all-categories/index"),
    path("new-category", CategoryCreateView.as_view(), name="new-category"),
    path("category/<int:pk>", CategoryDetailView.as_view(), name="category"),
    # SubCategory
    path("all-subcategories", SubCategoryListView.as_view(), name="all-subcategories"),
    path("all-subcategories/<int:pk>", SubCategoryRetrieveView.as_view(), name="all-subcategories/index"),
    path("new-subcategory", SubCategoryCreateView.as_view(), name="new-subcategory"),
    path("subcategory/<int:pk>", SubCategoryDetailView.as_view(), name="subcategory"),
    # Product
    path("all-products", ProductListView.as_view(), name="all-products"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product"),
]

