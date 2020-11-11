from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Clinic
from .serializers import ClinicSerializer

from django.contrib import messages
import csv,io

def db_clinics(request):
    
    template = "csv_upload.html"
    data = Clinic.objects.all()
    
    prompt = {
        'order'  : 'Order of the csv should be name, address,mobile, postcode,state,location,status,institution, type, rating, service, panel, image, hour',
        'clinic': data
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['db_clinics.csv']

    if not csv_file.name.endswidth('.csv'):
        messages.error(request, 'bukan csv')
    
    data_set = csv_file.read().decode('UTF-8')


    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            name=column[0],
            address=column[1],
            mobile=column[2],
            postcode=column[3],
            state=column[4],
            location=column[5],
            status=column[6],
            institution=column[7],
            jenis=column[8],
            rating=column[9],
            service=column[10],
            panel=column[11],
            image=column[12],
            hour=column[13]
        )
        context = {}
        return render(request, template, context)
 

class ClinicView(generics.RetrieveAPIView):
    queryset = Clinic.objects.all()

    def get(self,request, *args, **kwargs):
        queryset = self.get_queryset()
        serialzer = ClinicSerializer(queryset, many=True)
        return Response(serializer.data)
