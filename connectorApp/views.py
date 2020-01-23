from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests
from rest_framework import permissions

from .models import *
from .serializers import *


class VacancyList(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        """
        Вывод всех вакансий со всеми статусами
        """
        state = request.GET.get('state')
        owner = request.GET.get('owner')
        queryset = Vacancy.objects.exclude(state=u'ARCHIVE')
        if state is not None:
            queryset = Vacancy.objects.filter(state=str(state).upper())
        if owner is not None:
            queryset = Vacancy.objects.filter(owner=str(owner).upper())

        serializer = VacancySerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Добавлени недостающих вакансий в БД
        """
        # vacancies = [{"id": 8, "title": "Vacancy 1", "description": None, "state": "ARCHIVE", "owner": None},
        #      {"id": 6, "title": "Vacancy 2", "description": "Vacancy description long text", "state": "ACTIVE",
        #       "owner": 5631}]
        url = 'http://A'
        vacancies = requests.get(url).json()
        for vacancy in vacancies:
            serializer = VacancySerializer(data=vacancy)
            if serializer.is_valid():
                serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request):
        """
        если вакансии нет в А, то меняется статус
        """
        # vacancies = [
        #     {"id": 5, "title": "Vacancy 1", "description": None, "state": "ACTIVE", "owner": None},
        #              {"id": 6, "title": "Vacancy 2", "description": "Vacancy description long text", "state": "ACTIVE",
        #               "owner": 5631}]

        url = 'http://A'
        vacancies = requests.get(url).json()

        my_vac = Vacancy.objects.all()
        for i in my_vac:
            for j in vacancies:
                if i.id == j['id']:
                    # if i.state != j['state']:
                    i.state = j['state']
                    # else:
                    #     i.state = 'ARCHIVE'
                    serializer = VacancySerializer(i, data=request.data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                    break
                i.state = 'ARCHIVE'
                serializer = VacancySerializer(i, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
        return Response(status=status.HTTP_200_OK)
