class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.notas = {} # {disciplina: [nota1, nota2, ...]}

    def adicionar_nota(self, disciplina, nota):
        if disciplina not in self.notas:
            self.notas[disciplina] = []
        self.notas[disciplina].append(nota)

    def calcular_media_geral(self):
        todas_as_notas = [nota for notas_disc in self.notas.values() for nota in notas_disc]
        return sum(todas_as_notas) / len(todas_as_notas) if todas_as_notas else 0

    def __str__(self):
        return f"Matrícula: {self.matricula}, Nome: {self.nome}"

class Disciplina:
    def __init__(self, nome_disciplina):
        self.nome = nome_disciplina

    def __str__(self):
        return self.nome