from django.db import models
from usuarios.models import Usuario

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True)
    data_cadastro = models.DateField(auto_now_add = True)
    emprestado = models.BooleanField(default = False)
    
    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome

class Emprestimos(models.Model):
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateField(blank = True, null = True)
    data_devolucao = models.DateField(blank = True, null = True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Emprestimo'

    def __str__(self) -> str:
        return f"{self.nome_emprestado} | {self.livro}"