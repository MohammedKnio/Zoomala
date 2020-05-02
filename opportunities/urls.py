from django.urls import path
from .views import OpportunitiesListView


urlpatterns = [
    path('', OpportunitiesListView.as_view(), name='searchOpportunities' ),

]


app_name= "opportunities"