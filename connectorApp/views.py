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
        # a = [{"id": 5, "title": "Vacancy 1", "description": None, "state": "ARCHIVE", "owner": None},
        #      {"id": 4, "title": "Vacancy 2", "description": "Vacancy description long text", "state": "ACTIVE",
        #       "owner": 5631}]]
        url = 'http://A'
        vacancies = requests.get(url).json()
        for vacancy in vacancies:
            serializer = VacancySerializer(data=vacancy)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pass


# class AddNewVacancy(APIView):
#     """
#     Проверка новых вакансий и обновление уже имеющихся
#     """
#     url = 'A'
#     res = requests.get(url).json()
