from django.urls import path
from .views import CodeReviewAPIView, index

urlpatterns = [
    path("", index, name="home"),
    path("review-code/", CodeReviewAPIView.as_view(), name="review-code"),
]