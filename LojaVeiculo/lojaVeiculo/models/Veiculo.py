from lojaVeiculo.models import *
class Veiculo(models.Model):
    Veiculo = models.CharField(null=False, max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    cor = models.CharField(null=False, max_length=100)
    descricao = models.CharField(null=False, max_length=100)
    ano = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}'.format(self. Veiculo)