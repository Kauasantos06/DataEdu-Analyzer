import sqlite3
from models import Aluno

DATABASE_NAME = 'dataedu.db'

def connect_db():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            matricula TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula_aluno TEXT,
            disciplina TEXT NOT NULL,
            valor REAL NOT NULL,
            FOREIGN KEY (matricula_aluno) REFERENCES alunos(matricula)
        )
    ''')
    conn.commit()
    conn.close()

def inserir_aluno(aluno):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO alunos (matricula, nome) VALUES (?, ?)",
                       (aluno.matricula, aluno.nome))
        conn.commit()
        print(f"Aluno {aluno.nome} inserido com sucesso.")
    except sqlite3.IntegrityError:
        print(f"Erro: Matrícula {aluno.matricula} já existe.")
    finally:
        conn.close()

def inserir_nota(matricula_aluno, disciplina, valor_nota):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notas (matricula_aluno, disciplina, valor) VALUES (?, ?, ?)",
                   (matricula_aluno, disciplina, valor_nota))
    conn.commit()
    conn.close()
    print(f"Nota {valor_nota} para {disciplina} do aluno {matricula_aluno} inserida.")

def get_all_alunos_with_notas():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT a.matricula, a.nome, n.disciplina, n.valor
        FROM alunos a
        LEFT JOIN notas n ON a.matricula = n.matricula_aluno
        ORDER BY a.nome, n.disciplina
    ''')
    rows = cursor.fetchall()
    conn.close()

    alunos_data = {}
    for row in rows:
        matricula, nome, disciplina, valor = row
        if matricula not in alunos_data:
            alunos_data[matricula] = Aluno(matricula, nome)
        if disciplina and valor is not None:
            alunos_data[matricula].adicionar_nota(disciplina, valor)
    return list(alunos_data.values())

def load_data_from_csv(filepath):
    import pandas as pd
    try:
        df = pd.read_csv(filepath)
        conn = connect_db()
        cursor = conn.cursor()
        for index, row in df.iterrows():
            matricula = str(row['matricula']) # Garante que matricula é string
            nome = str(row['nome'])

            try:
                cursor.execute("INSERT OR IGNORE INTO alunos (matricula, nome) VALUES (?, ?)", (matricula, nome))
                for col in df.columns:
                    if col not in ['matricula', 'nome'] and pd.notna(row[col]):
                        disciplina = col
                        nota = float(row[col])
                        cursor.execute("INSERT INTO notas (matricula_aluno, disciplina, valor) VALUES (?, ?, ?)",
                                       (matricula, disciplina, nota))
                conn.commit()
            except Exception as e:
                print(f"Erro ao inserir linha {index}: {e}")
                conn.rollback() # Reverte a transação em caso de erro
        conn.close()
        print(f"Dados carregados de {filepath} com sucesso.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filepath}' não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar CSV: {e}")
