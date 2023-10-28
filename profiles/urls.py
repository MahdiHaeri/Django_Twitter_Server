from django.urls import path
from profiles import views

urlpatterns = [
    path('bios/', views.BioView.as_view(), name='bios'),
    path('bios/<int:bio_id>/', views.BioDetailsView.as_view(), name='bio_details')
]
