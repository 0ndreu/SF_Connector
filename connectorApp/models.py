from django.db import models


class Vacancy(models.Model):
    STATE = (
        (1, 'ACTIVE'),
        (2, 'ARCHIVE')
    )
    id = models.IntegerField(null=False, primary_key=True)
    title = models.CharField(max_length=256, null=False)
    state = models.CharField(max_length=20, null=False)
    owner = models.IntegerField(null=True)

    def __str__(self):
        return self.title
