from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests

from .models import *
from .serializers import *


class VacancyList(APIView):
    """
    Вывод всех синхронизированных вакансий, включая фильтры по статусу и владельцу
    """
    def get(self, request):
        state = request.GET.get('state')
        owner = request.GET.get('owner')
        queryset = Vacancy.objects.all()
        if state is not None:
            queryset = Vacancy.objects.filter(state=str(state).upper())
        if owner is not None:
            queryset = Vacancy.objects.filter(owner=str(owner).upper())

        serializer = VacancySerializer(queryset, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # vacancies = [{"id": 5, "title": "Vacancy 1", "description": None, "state": "ARCHIVE", "owner": None},
        #      {"id": 6, "title": "Vacancy 2", "description": "Vacancy description long text", "state": "ACTIVE",
        #       "owner": 5631}]
        url = 'http://A'
        vacancies = requests.get(url).json()
        for vacancy in vacancies:
            serializer = VacancySerializer(data=vacancy)
            if serializer.is_valid():
                serializer.save()

    def patch(self, request):
        url = 'http://A'
        vacancies = requests.get(url).json()

        my_vac = Vacancy.objects.all()
        for i in vacancies:
            vac = my_vac.get(id=i['id'])
            vac.state = i['state']
            serializer = VacancySerializer(vac, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

