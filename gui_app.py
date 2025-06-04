import tkinter as tk
from tkinter import messagebox, filedialog, ttk # ttk para widgets mais modernos
import database
import analysis

# Importações específicas para Matplotlib no Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk # <--- Corrigido aqui
import matplotlib.pyplot as plt # Ainda é bom ter para limpar plots ou ajustes gerais

class DataEduApp:
    def __init__(self, master):
        self.master = master
        master.title("DataEdu Analyzer")

        # --- Frames para organizar a interface ---
        self.controls_frame = tk.Frame(master)
        self.controls_frame.pack(pady=10)

        self.results_frame = tk.Frame(master)
        self.results_frame.pack(pady=10)

        self.chart_frame = tk.Frame(master, borderwidth=2, relief="groove") # Frame para o gráfico
        self.chart_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # --- Controles (Buttons) ---
        self.btn_load_csv = tk.Button(self.controls_frame, text="Carregar CSV", command=self.load_csv_data)
        self.btn_load_csv.pack(side=tk.LEFT, padx=5)

        self.btn_show_analysis = tk.Button(self.controls_frame, text="Mostrar Análise (Texto)", command=self.display_analysis_text)
        self.btn_show_analysis.pack(side=tk.LEFT, padx=5)

        self.btn_show_chart_medias = tk.Button(self.controls_frame, text="Mostrar Gráfico Médias", command=self.display_medias_chart)
        self.btn_show_chart_medias.pack(side=tk.LEFT, padx=5)

        self.btn_show_chart_histograma = tk.Button(self.controls_frame, text="Mostrar Histograma", command=self.display_histogram_chart)
        self.btn_show_chart_histograma.pack(side=tk.LEFT, padx=5)

        # Campo para selecionar disciplina para histograma
        self.disciplina_label = tk.Label(self.controls_frame, text="Disciplina:")
        self.disciplina_label.pack(side=tk.LEFT, padx=5)
        self.disciplina_entry = tk.Entry(self.controls_frame)
        self.disciplina_entry.pack(side=tk.LEFT, padx=5)


        # --- Área de texto para exibir resultados textuais ---
        self.results_text = tk.Text(self.results_frame, height=10, width=80, wrap=tk.WORD)
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.text_scrollbar = tk.Scrollbar(self.results_frame, command=self.results_text.yview)
        self.text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_text.config(yscrollcommand=self.text_scrollbar.set)

        # Variáveis para armazenar o Canvas e a Toolbar do Matplotlib
        self.canvas = None
        self.toolbar = None


    def load_csv_data(self):
        filepath = filedialog.askopenfilename(
            title="Selecione o arquivo CSV",
            filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*"))
        )
        if filepath:
            database.load_data_from_csv(filepath)
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
            self.display_analysis_text() # Atualiza a análise textual após carregar
        else:
            messagebox.showwarning("Atenção", "Nenhum arquivo selecionado.")

    def display_analysis_text(self):
        self.results_text.delete(1.0, tk.END) # Limpa a área de texto

        alunos = database.get_all_alunos_with_notas()
        if alunos:
            df = analysis.get_dataframe_from_alunos(alunos)
            if not df.empty:
                self.results_text.insert(tk.END, f"Média Geral da Turma: {analysis.calcular_media_turma_geral(df):.2f}\n\n")

                medias_disciplina = analysis.calcular_medias_disciplina(df)
                self.results_text.insert(tk.END, "Médias por Disciplina:\n")
                for disc, media in medias_disciplina.items():
                    self.results_text.insert(tk.END, f"  {disc}: {media:.2f}\n")
                    moda = analysis.calcular_moda_disciplina(df, disc)
                    desvio = analysis.calcular_desvio_padrao_disciplina(df, disc)
                    self.results_text.insert(tk.END, f"    Moda: {moda}, Desvio Padrão: {desvio:.2f}\n")
            else:
                self.results_text.insert(tk.END, "Nenhum dado de nota para analisar.")
        else:
            self.results_text.insert(tk.END, "Nenhum aluno cadastrado para análise.")


    def _clear_chart_frame(self):
        """Limpa o frame onde o gráfico é exibido."""
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        self.canvas = None
        self.toolbar = None


    def _display_chart(self, fig):
        """Função auxiliar para exibir um gráfico (Figure) no frame."""
        self._clear_chart_frame() # Limpa qualquer gráfico anterior

        if fig:
            self.canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
            self.canvas_widget = self.canvas.get_tk_widget()
            self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            self.canvas.draw() # Desenha o gráfico

            # Adiciona a barra de ferramentas (zoom, pan, save, etc.)
            self.toolbar = NavigationToolbar2Tk(self.canvas, self.chart_frame) # <--- Corrigido aqui
            self.toolbar.update()
            self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        else:
            messagebox.showwarning("Gráfico", "Não foi possível gerar o gráfico, dados insuficientes ou disciplina inválida.")


    def display_medias_chart(self):
        alunos = database.get_all_alunos_with_notas()
        if alunos:
            df = analysis.get_dataframe_from_alunos(alunos)
            if not df.empty:
                medias_disciplina = analysis.calcular_medias_disciplina(df)
                fig = analysis.gerar_grafico_medias_disciplina(medias_disciplina)
                self._display_chart(fig)
            else:
                messagebox.showinfo("Gráfico", "Nenhum dado de nota para gerar o gráfico de médias.")
        else:
            messagebox.showinfo("Gráfico", "Nenhum aluno cadastrado para gerar gráficos.")

    def display_histogram_chart(self):
        disciplina = self.disciplina_entry.get().strip() # Pega a disciplina do campo de entrada
        if not disciplina:
            messagebox.showwarning("Entrada Inválida", "Por favor, digite o nome da disciplina para o histograma.")
            return

        alunos = database.get_all_alunos_with_notas()
        if alunos:
            df = analysis.get_dataframe_from_alunos(alunos)
            if not df.empty:
                fig = analysis.gerar_histograma_notas(df, disciplina)
                self._display_chart(fig)
            else:
                messagebox.showinfo("Gráfico", f"Nenhum dado de nota para gerar o histograma para '{disciplina}'.")
        else:
            messagebox.showinfo("Gráfico", "Nenhum aluno cadastrado para gerar gráficos.")


# Não precisamos do if __name__ == "__main__": aqui, pois main.py fará a inicialização