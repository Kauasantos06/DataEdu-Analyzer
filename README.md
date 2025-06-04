DataEdu Analyzer
Ferramenta de Análise Simplificada de Desempenho Acadêmico
Descrição
O DataEdu Analyzer é um projeto de extensão desenvolvido em Python com o objetivo de auxiliar educadores na gestão e análise de dados de desempenho acadêmico. A ferramenta transforma dados brutos de notas em informações claras e visuais, facilitando a identificação de padrões, desafios e oportunidades de melhoria no processo de aprendizagem.

Objetivo
O principal objetivo do DataEdu Analyzer é prover uma solução tecnológica acessível que capacite professores a tomar decisões pedagógicas mais informadas, contribuindo para a melhoria contínua da qualidade da educação.

Alinhamento com ODS 4: Educação de Qualidade
Este projeto está diretamente alinhado com o Objetivo de Desenvolvimento Sustentável (ODS) 4 da ONU: Educação de Qualidade. Ao oferecer uma ferramenta que permite a análise detalhada do desempenho dos alunos, o DataEdu Analyzer contribui para:

Melhorar a gestão de dados educacionais: Fornecendo uma maneira eficiente de organizar e processar informações acadêmicas.

Apoiar a tomada de decisão pedagógica: Capacitando educadores com insights baseados em dados para personalizar o ensino e identificar lacunas de aprendizado.

Promover uma educação mais equitativa e de qualidade: Ao facilitar a identificação de necessidades específicas de alunos, permitindo intervenções direcionadas.

Funcionalidades
O DataEdu Analyzer oferece as seguintes funcionalidades principais através de sua interface gráfica:

Carregamento de Dados CSV: Importa dados de alunos e suas notas a partir de arquivos CSV.

Análise Textual Detalhada: Exibe um resumo textual com métricas como média geral da turma, médias por disciplina, moda e desvio padrão.

Geração de Gráficos de Médias por Disciplina: Cria e exibe um gráfico de barras interativo mostrando as médias de notas por disciplina.

Geração de Histograma de Notas: Gera um histograma da distribuição de notas para uma disciplina específica, permitindo visualizar a concentração de notas.

Interação com o Gráfico: Permite zoom, pan, redimensionamento e salvamento dos gráficos diretamente da GUI.

Tecnologias Utilizadas
Python 3.x: Linguagem de programação principal.

Tkinter: Para a construção da Interface Gráfica do Usuário (GUI).

SQLite: Banco de dados leve para persistência dos dados de alunos e notas.

Pandas: Biblioteca para manipulação e análise de dados.

Matplotlib: Para a geração e visualização de gráficos.

NumPy: Para operações numéricas e estatísticas.

Estrutura do Projeto
dataedu_analyzer/
├── main.py                # Ponto de entrada da aplicação GUI
├── gui_app.py             # Lógica da Interface Gráfica do Usuário (Tkinter)
├── database.py            # Funções para interação com o banco de dados SQLite
├── models.py              # Definição das classes (Aluno, Disciplina)
├── analysis.py            # Funções para cálculos estatísticos e geração de gráficos
├── data.csv               # Exemplo de arquivo de dados para importação
└── README.md              # Este arquivo de documentação

Como Executar o Projeto
Siga os passos abaixo para configurar e executar o DataEdu Analyzer em seu ambiente.

Pré-requisitos
Python 3.x instalado.

1. Instalação do Ambiente Virtual
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

Navegue até o diretório raiz do projeto (dataedu_analyzer/) no seu terminal e execute:

python -m venv venv

2. Ativar o Ambiente Virtual
No Windows (Prompt de Comando ou PowerShell):

.\venv\Scripts\activate

No Linux ou macOS (Bash/Zsh):

source venv/bin/activate

Você verá (venv) no início da linha de comando, indicando que o ambiente está ativo.

3. Instalação das Dependências
Com o ambiente virtual ativo, instale as bibliotecas necessárias:

pip install pandas matplotlib

4. Preparação dos Dados (Opcional, mas recomendado para teste)
Crie um arquivo data.csv no diretório raiz do projeto com o seguinte conteúdo de exemplo:

matricula,nome,Matematica,Portugues,Programacao
1001,Maria Silva,8.5,7.0,9.0
1002,João Santos,6.0,8.0,7.5
1003,Ana Costa,9.0,9.5,8.0
1004,Pedro Rocha,7.0,6.5,7.0

Você pode adicionar mais alunos, disciplinas e notas conforme desejar.

5. Execução da Aplicação
Com o ambiente virtual ativo, execute o arquivo principal:

python main.py

A janela da interface gráfica do DataEdu Analyzer será aberta. Você pode então usar o botão "Carregar CSV" para importar os dados do seu data.csv e explorar as funcionalidades de análise e visualização.

Trabalhos Futuros
Para futuras iterações, o DataEdu Analyzer poderia ser aprimorado com as seguintes funcionalidades:

Gerenciamento Completo de Alunos e Notas: Adicionar funcionalidades de edição e exclusão de alunos e notas diretamente pela GUI.

Relatórios Personalizados: Permitir que o usuário defina critérios específicos para a geração de relatórios (ex: alunos abaixo da média, desempenho por período).

Visualizações Avançadas: Implementar outros tipos de gráficos, como gráficos de linha para acompanhar o progresso do aluno ao longo do tempo.

Exportação de Relatórios: Opções para exportar as análises textuais e os gráficos gerados em diferentes formatos (PDF, Excel).

Multi-usuário: Implementar um sistema de autenticação para múltiplos professores.

Autor
[Kauã Santos] - [https://github.com/Kauasantos06]
