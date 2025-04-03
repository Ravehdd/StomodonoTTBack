from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("api/v1/index/", InitialiseDBAPIView.as_view()),
    path("api/v1/data/", PatientsAPIView.as_view()),
    path("api/v1/login/<str:patient_phone>/<str:patient_pass>/", AuthPatientAPIView.as_view()),
    path("api/v1/getdata/<str:patient_phone>/", PatientDetailAPIView.as_view()),
    path("api/v1/test-mongo/", TestMongoAPIView.as_view())

]
