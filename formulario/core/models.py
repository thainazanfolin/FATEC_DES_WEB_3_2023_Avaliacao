from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)


