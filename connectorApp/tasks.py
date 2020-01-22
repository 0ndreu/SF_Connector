from sf_connector.celery import app
from connectorApp.models import Vacancy
import requests
from .serializers import VacancySerializer


@app.task
def patch_vacancies(self, request):
    """
    если вакансии нет в А, то меняется статус
    """
    # vacancies = [
    #     # {"id": 5, "title": "Vacancy 1", "description": None, "state": "ACTIVE", "owner": None},
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


@app.task
def post_vacancies(self, request):
    """
    Добавлени недостающих вакансий в БД
    """
    # vacancies = [{"id": 5, "title": "Vacancy 1", "description": None, "state": "ARCHIVE", "owner": None},
    #      {"id": 6, "title": "Vacancy 2", "description": "Vacancy description long text", "state": "ACTIVE",
    #       "owner": 5631}]
    url = 'http://A'
    vacancies = requests.get(url).json()
    for vacancy in vacancies:
        serializer = VacancySerializer(data=vacancy)
        if serializer.is_valid():
            serializer.save()