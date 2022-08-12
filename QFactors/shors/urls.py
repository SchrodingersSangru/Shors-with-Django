from django.urls import path
from .views import FactorizationView

app_name = 'shors'


urlpatterns = [
    path('factors/', FactorizationView.as_view(), name = "factors"),
]



