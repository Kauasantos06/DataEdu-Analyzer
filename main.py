# main.py
import database
import analysis
from models import Aluno
import os # Para verificar se o arquivo CSV existe
import tkinter as tk 
from gui_app import DataEduApp 

if __name__ == "__main__":
    database.create_tables()

    root = tk.Tk()
    root.geometry("1000x800") # Aumentei o tamanho da janela para acomodar o gráfico melhor
    root.resizable(True, True) # Permite redimensionar a janela

    app = DataEduApp(root)
    root.mainloop()

def menu():
    print("\n--- DataEdu Analyzer ---")
    print("1. Inserir Novo Aluno")
    print("2. Inserir Nota para Aluno")
    print("3. Carregar Dados de CSV")
    print("4. Visualizar Todos os Alunos e Notas")
    print("5. Análise de Dados da Turma")
    print("6. Gerar Gráficos")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    database.create_tables()

    while True:
        opcao = menu()

        if opcao == '1':
            matricula = input("Digite a matrícula do aluno: ")
            nome = input("Digite o nome do aluno: ")
            aluno = Aluno(matricula, nome)
            database.inserir_aluno(aluno)
        elif opcao == '2':
            matricula = input("Digite a matrícula do aluno: ")
            disciplina = input("Digite o nome da disciplina: ")
            try:
                valor_nota = float(input("Digite o valor da nota: "))
                database.inserir_nota(matricula, disciplina, valor_nota)
            except ValueError:
                print("Valor de nota inválido. Digite um número.")
        elif opcao == '3':
            filepath = input("Digite o caminho do arquivo CSV (ex: data.csv): ")
            if os.path.exists(filepath):
                database.load_data_from_csv(filepath)
            else:
                print(f"Arquivo '{filepath}' não encontrado. Certifique-se de que ele está no diretório correto.")
        elif opcao == '4':
            alunos = database.get_all_alunos_with_notas()
            if alunos:
                print("\n--- Alunos e Notas ---")
                for aluno in alunos:
                    print(f"\n{aluno}")
                    for disciplina, notas in aluno.notas.items():
                        print(f"  {disciplina}: {', '.join(map(str, notas))}")
            else:
                print("Nenhum aluno cadastrado ainda.")
        elif opcao == '5':
            alunos = database.get_all_alunos_with_notas()
            if alunos:
                df = analysis.get_dataframe_from_alunos(alunos)
                if not df.empty:
                    print("\n--- Análise de Dados da Turma ---")
                    print(f"Média Geral da Turma: {analysis.calcular_media_turma_geral(df):.2f}")

                    medias_disciplina = analysis.calcular_medias_disciplina(df)
                    print("\nMédias por Disciplina:")
                    for disc, media in medias_disciplina.items():
                        print(f"  {disc}: {media:.2f}")
                        moda = analysis.calcular_moda_disciplina(df, disc)
                        desvio = analysis.calcular_desvio_padrao_disciplina(df, disc)
                        print(f"    Moda: {moda}, Desvio Padrão: {desvio:.2f}")

                    # Você pode adicionar mais análises aqui, como aluno com maior/menor média geral.
                else:
                    print("Nenhum dado de nota para analisar.")
            else:
                print("Nenhum aluno cadastrado para análise.")
        elif opcao == '6':
            alunos = database.get_all_alunos_with_notas()
            if alunos:
                df = analysis.get_dataframe_from_alunos(alunos)
                if not df.empty:
                    medias_disciplina = analysis.calcular_medias_disciplina(df)
                    analysis.gerar_grafico_medias_disciplina(medias_disciplina)

                    # Pergunta ao usuário qual disciplina para o histograma
                    disciplinas_disponiveis = [col for col in df.columns if col not in ['Matricula', 'Nome']]
                    if disciplinas_disponiveis:
                        print("\nDisciplinas disponíveis para Histograma:", ", ".join(disciplinas_disponiveis))
                        disc_histograma = input("Digite o nome da disciplina para gerar o histograma: ")
                        analysis.gerar_histograma_notas(df, disc_histograma)
                    else:
                        print("Não há disciplinas com notas para gerar histogramas.")
                else:
                    print("Nenhum dado de nota para gerar gráficos.")
            else:
                print("Nenhum aluno cadastrado para gerar gráficos.")
        elif opcao == '0':
            print("Saindo do DataEdu Analyzer. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()