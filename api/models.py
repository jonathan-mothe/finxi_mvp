from django.db import models
from django.contrib.auth import get_user_model


class Demanda(models.Model):
    descricao = models.TextField(max_length=500, verbose_name='Descrição da peça', blank=False)
    
    #   endereço
    cep = models.CharField(max_length=9, blank=True)
    numero = models.CharField(max_length=5, blank=True)
    logradouro = models.CharField(max_length=230, blank=True)
    bairro = models.CharField(max_length=230, blank=True)

    anunciante = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    #   contato
    email = models.EmailField(max_length=45, blank=True)
    telefone = models.CharField(max_length=14, blank=True)
    
    status = models.BooleanField(
        max_length=1,
        choices=[
            (False, 'Aberto'),
            (True, 'Finalizado')
        ],
        default=False
    )

    def __str__(self):
        return str(self.anunciante)
