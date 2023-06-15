from django.test import TestCase, Client
from django.urls import reverse
from core.models import Professor
from core.models import Cadastro

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.professor = Professor.objects.create()

    def test_formulario_view(self):
        response = self.client.post(reverse('formulario'), {'nome', 'professor'})
        self.assertEqual(response.status_code, 302)  # redireciona

        cadastro = Cadastro.objects.first()
        self.assertEqual(cadastro.nome)
        self.assertEqual(cadastro.professor)

    def test_formulario_view_campos_vazios(self):
        response = self.client.post(reverse('formulario'), {'nome': '', 'professor': ''})
        self.assertEqual(response.status_code, 200)  # formulario renderizada novamente
        self.assertContains(response, "Este campo é obrigatório.")  #verifica se a mensagem de erro é exibida
        self.assertFalse(Cadastro.objects.exists())  # verifica se nenhum cadastro foi criado

