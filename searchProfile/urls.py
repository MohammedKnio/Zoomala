
from .views import SearchProfileView
from django.urls import path


urlpatterns = [
    path('', SearchProfileView.as_view(), name="searchProfile"),
]
