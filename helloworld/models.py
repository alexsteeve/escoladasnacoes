from django.db import models


class Escolaridade(models.Model):

    nome = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    def __str__(self):
        return self.nome

    objetos = models.Manager()


class Estudante(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    matricula = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=255,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    celular = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    dataNascimento = models.DateField(
        null=False,
        blank=False
    )

    batismo = models.BooleanField(
        null=False,
        blank=False
    )

#    escolaridade = models.IntegerField(
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula

    objetos = models.Manager()


class Curso(models.Model):

    nome = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    def __str__(self):
        return self.nome

    objetos = models.Manager()

class Materia(models.Model):

    nome = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    livro1 = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    livro2 = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    objetos = models.Manager()

class CursoPeriodo(models.Model):

    ano = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    semestre = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    local = models.CharField(
        null=False,
        blank=False,
        max_length=255
    )

    diaSemana = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        default='Domingo'
    )

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.curso.nome

    objetos = models.Manager()


class CursoPeriodoEstudante(models.Model):

    aprovacao = models.BooleanField(
        null=False,
        blank=False
    )

    presencas = models.BooleanField(
        null=False,
        blank=False
    )

    financeiro = models.BooleanField(
        null=False,
        blank=False
    )

    provas = models.BooleanField(
        null=False,
        blank=False
    )

    trabalhos = models.BooleanField(
        null=False,
        blank=False
    )

    cursoPeriodo = models.ForeignKey(CursoPeriodo, on_delete=models.CASCADE)

    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)

    objetos = models.Manager()