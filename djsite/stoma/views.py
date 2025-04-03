from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from datetime import datetime
import dateutil.parser
import logging
from pymongo import MongoClient
# settings.py
from djsite.settings import DB_LOGIN
from djsite.settings import DB_PASS

# client = MongoClient(f'mongodb://{DB_LOGIN}:{DB_PASS}@5.35.99.228:27017')
client = MongoClient("localhost", port=27017)
db = client['products-db']

logger = logging.getLogger(__name__)


class InitialiseDBAPIView(APIView):
    def post(self, request):
        print(request.data)
        patient_id = UserData.objects.filter(name=request.data["patient"]).values("id")[0]["id"]
        doctor_id = Doctor.objects.filter(name=request.data["doctor"]).values("id")[0]["id"]
        clinic_id = Clinic.objects.filter(name=request.data["clinic"]).values("id")[0]["id"]

        add_time = dateutil.parser.parse(request.data["add_time"])
        start_time = dateutil.parser.parse(request.data["start_time"])
        end_time = dateutil.parser.parse(request.data["end_time"])

        time_now = datetime.strptime("14.08.2024 13:34:23", "%d.%m.%Y %H:%M:%S")

        days_count = (time_now - start_time).days

        if request.data["cancel_time"] != "NULL":
            cancel_time = dateutil.parser.parse(request.data["cancel_time"])
            Patient.objects.create(add_time=add_time, start_time=start_time,
                                   end_time=end_time, cancel_time=cancel_time, clinic_id=clinic_id, doctor_id=doctor_id,
                                   patient_id=patient_id, days_count=days_count)
        else:
            Patient.objects.create(add_time=add_time, start_time=start_time,
                                   end_time=end_time, clinic_id=clinic_id, doctor_id=doctor_id,
                                   patient_id=patient_id, days_count=days_count)

        return Response("okk")


class PatientsAPIView(generics.ListAPIView):

    queryset = Patient.objects.filter(id=71)
    serializer_class = IndexSerializer


class AuthPatientAPIView(generics.ListAPIView):
    serializer_class = IndexSerializer

    def get_queryset(self):
        patient_phone = self.kwargs['patient_phone']
        patient_pass = self.kwargs['patient_pass']

        try:
            patient_id = AuthUsers.objects.filter(login=patient_phone, password=patient_pass).values()[0]["id"]

            # Логгирование
            logger.info(f"Received request with phone: {patient_phone}, pass: {patient_pass}")

            if patient_id == 1:
                return Patient.objects.filter(patient_id=patient_id)
            else:
                logger.warning(f"Unauthorized access attempt for phone: {patient_phone}")
                return Response("Wrong dst")
        except IndexError:
            logger.error(f"No user found for phone: {patient_phone}")
            return None

    def log_request(self, message):
        logger.info(message)

    def log_error(self, message):
        logger.error(message)


class PatientDetailAPIView(generics.ListAPIView):
    serializer_class = IndexSerializer

    def get_queryset(self):
        patient_phone = self.kwargs['patient_phone']
        try:
            patient_id = AuthUsers.objects.filter(login=patient_phone).values()[0]["id"]
            if patient_id == 1:
                return Patient.objects.filter(patient_id=patient_id)
            else:
                return None
        except IndexError:
            return None


class TestMongoAPIView(APIView):
    def get(self, request):
        data = db.products
        products_raw = list(data.find({}))
        products = []
        for product in products_raw:
            product['id'] = str(product.pop('_id'))
            products.append(product)
        print(type(products))
        print(products)
        return Response({"data": products})
