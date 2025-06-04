import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Importação para uso no Tkinter
from matplotlib.figure import Figure # Adicione esta linha
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk # <--- Corrigido aqui


def get_dataframe_from_alunos(alunos):
    data = []
    for aluno in alunos:
        row = {'Matricula': aluno.matricula, 'Nome': aluno.nome}
        for disciplina, notas in aluno.notas.items():
            if notas:
                row[disciplina] = notas[0]
            else:
                row[disciplina] = np.nan
        data.append(row)
    df = pd.DataFrame(data)
    return df

def calcular_medias_disciplina(df):
    medias = {}
    for col in df.columns:
        if col not in ['Matricula', 'Nome']:
            medias[col] = df[col].mean()
    return medias

def calcular_media_turma_geral(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    if not numeric_cols.empty:
        return df[numeric_cols].stack().mean()
    return 0

def calcular_moda_disciplina(df, disciplina):
    if disciplina in df.columns:
        notas_validas = df[disciplina].dropna()
        if not notas_validas.empty:
            contagem = Counter(notas_validas)
            moda = contagem.most_common(1)[0][0]
            return moda
    return "N/A"

def calcular_desvio_padrao_disciplina(df, disciplina):
    if disciplina in df.columns:
        notas_validas = df[disciplina].dropna()
        if not notas_validas.empty:
            return notas_validas.std()
    return "N/A"

# --- FUNÇÃO MODIFICADA: Retorna o objeto Figure ---
def gerar_grafico_medias_disciplina(medias_disciplina):
    if not medias_disciplina:
        print("Não há dados para gerar gráfico de médias por disciplina.")
        return None # Retorna None se não houver dados

    disciplinas = list(medias_disciplina.keys())
    medias = list(medias_disciplina.values())

    # Cria um objeto Figure e um Axes (eixo de plotagem)
    fig = Figure(figsize=(10, 6), dpi=100) # dpi define a qualidade da imagem
    ax = fig.add_subplot(111) # 111 significa 1 linha, 1 coluna, primeiro gráfico

    ax.bar(disciplinas, medias, color='skyblue')
    ax.set_xlabel('Disciplinas')
    ax.set_ylabel('Média das Notas')
    ax.set_title('Média das Notas por Disciplina')
    ax.set_ylim(0, 10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    fig.tight_layout() # Ajusta o layout da figura

    # Não salva nem mostra aqui, apenas retorna a figura
    return fig

# --- FUNÇÃO MODIFICADA: Retorna o objeto Figure ---
def gerar_histograma_notas(df, disciplina):
    if disciplina in df.columns:
        notas = df[disciplina].dropna()
        if not notas.empty:
            fig = Figure(figsize=(8, 5), dpi=100)
            ax = fig.add_subplot(111)

            ax.hist(notas, bins=range(0, 11), edgecolor='black', alpha=0.7)
            ax.set_xlabel('Notas')
            ax.set_ylabel('Frequência')
            ax.set_title(f'Histograma de Notas para {disciplina}')
            ax.set_xticks(range(0, 11))
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            fig.tight_layout()

            return fig # Retorna a figura
        else:
            print(f"Não há notas para gerar histograma para a disciplina {disciplina}.")
            return None
    else:
        print(f"Disciplina '{disciplina}' não encontrada no DataFrame.")
        return None
