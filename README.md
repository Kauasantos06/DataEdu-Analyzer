## DataEdu Analyzer

## Descrição do Projeto

O DataEdu Analyzer é um projeto de extensão inovador, desenvolvido em Python, que visa transformar a maneira como educadores interagem com os dados de desempenho acadêmico. Nossa ferramenta foi criada para auxiliar professores na gestão e análise eficiente das notas dos alunos, convertendo dados brutos em informações claras e visuais. Isso facilita a identificação de padrões de aprendizado, desafios específicos e oportunidades para aprimorar o processo educacional.

## Objetivo Principal

Nosso objetivo primordial com o DataEdu Analyzer é fornecer uma solução tecnológica acessível e intuitiva que capacite os professores a tomar decisões pedagógicas mais informadas. Ao fazer isso, buscamos contribuir ativamente para a melhoria contínua da qualidade da educação, tornando o ensino mais adaptado e eficaz para cada aluno.

## Alinhamento com ODS 4: Educação de Qualidade

Este projeto está profundamente alinhado com o Objetivo de Desenvolvimento Sustentável (ODS) 4 da ONU: Educação de Qualidade. Ao oferecer uma ferramenta que permite a análise detalhada do desempenho dos alunos, o DataEdu Analyzer contribui significativamente para:

Melhorar a gestão de dados educacionais: Fornecendo uma maneira eficiente e organizada de processar e armazenar informações acadêmicas.

Apoiar a tomada de decisão pedagógica: Capacitando educadores com insights baseados em dados, essenciais para personalizar o ensino e identificar lacunas de aprendizado.

Promover uma educação mais equitativa e de qualidade: Ao facilitar a identificação de necessidades específicas de alunos, permitindo intervenções direcionadas e personalizadas.

## Funcionalidades Chave
O DataEdu Analyzer oferece um conjunto robusto de funcionalidades, acessíveis através de sua interface gráfica amigável:

Carregamento de Dados CSV: Importe facilmente dados de alunos e suas respectivas notas a partir de arquivos CSV.

Análise Textual Detalhada: Visualize um resumo textual com métricas essenciais como a média geral da turma, médias por disciplina, moda e desvio padrão.

Geração de Gráficos de Médias por Disciplina: Crie e exiba um gráfico de barras interativo, proporcionando uma visão clara do desempenho médio em cada disciplina.

Geração de Histograma de Notas: Gere um histograma da distribuição de notas para uma disciplina específica, permitindo identificar a concentração de notas (seja em faixas baixas, médias ou altas).

Interação com o Gráfico: Desfrute de recursos como zoom, pan, redimensionamento e a capacidade de salvar os gráficos diretamente da GUI.

## Tecnologias Utilizadas
Este projeto foi construído utilizando um conjunto de tecnologias poderosas e amplamente reconhecidas no ecossistema Python:

Python 3.x: A linguagem de programação principal, escolhida por sua versatilidade e vasta comunidade.

Tkinter: Utilizado para a construção da Interface Gráfica do Usuário (GUI), garantindo uma experiência intuitiva.

SQLite: Um banco de dados leve e embarcado, ideal para a persistência dos dados de alunos e notas.

Pandas: Essencial para a manipulação e análise eficiente de grandes volumes de dados.

Matplotlib: A biblioteca padrão para a geração e visualização de gráficos de alta qualidade.

NumPy: Fundamental para operações numéricas e estatísticas de alto desempenho.

## Estrutura do Projeto
A organização do DataEdu Analyzer segue uma estrutura modular, facilitando a manutenção e a expansão:

dataedu_analyzer/
├── main.py                # Ponto de entrada principal da aplicação GUI
├── gui_app.py             # Lógica da Interface Gráfica do Usuário (Tkinter)
├── database.py            # Funções para interação com o banco de dados SQLite
├── models.py              # Definição das classes e modelos de dados (Aluno, Disciplina)
├── analysis.py            # Funções para cálculos estatísticos e geração de gráficos
├── data.csv               # Exemplo de arquivo de dados para importação (opcional)
└── README.md              # Este arquivo de documentação do projeto

## Como Executar o Projeto
Siga os passos abaixo para configurar e executar o DataEdu Analyzer em seu ambiente de desenvolvimento.

## Pré-requisitos
Certifique-se de ter o Python 3.x instalado em seu sistema.

1. Instalação do Ambiente Virtual
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outras instalações Python.

Navegue até o diretório raiz do projeto (dataedu_analyzer/) no seu terminal e execute:

python -m venv venv

2. Ativar o Ambiente Virtual
Após a criação, ative o ambiente virtual. Você verá (venv) no início da linha de comando, indicando que o ambiente está ativo.

No Windows (Prompt de Comando ou PowerShell):

.\venv\Scripts\activate

No Linux ou macOS (Bash/Zsh):

source venv/bin/activate

3. Instalação das Dependências
Com o ambiente virtual ativo, instale todas as bibliotecas necessárias para o projeto:

pip install pandas matplotlib

4. Preparação dos Dados (Opcional, mas recomendado para teste)
Para testar o sistema com dados iniciais, crie um arquivo data.csv no diretório raiz do projeto com o seguinte conteúdo de exemplo:

matricula,nome,Matematica,Portugues,Programacao
1001,Maria Silva,8.5,7.0,9.0
1002,João Santos,6.0,8.0,7.5
1003,Ana Costa,9.0,9.5,8.0
1004,Pedro Rocha,7.0,6.5,7.0

Sinta-se à vontade para adicionar mais alunos, disciplinas e notas conforme desejar.

5. Execução da Aplicação
Com o ambiente virtual ativo, execute o arquivo principal para iniciar a interface gráfica:

python main.py

A janela da interface gráfica do DataEdu Analyzer será aberta. A partir dela, você poderá usar o botão "Carregar CSV" para importar os dados e explorar todas as funcionalidades de análise e visualização.

Trabalhos Futuros
O DataEdu Analyzer é um protótipo com grande potencial de expansão. Para futuras iterações, consideramos as seguintes melhorias:

Gerenciamento Completo de Alunos e Notas: Adicionar funcionalidades de edição e exclusão de alunos e notas diretamente pela GUI.

Relatórios Personalizados: Permitir que o usuário defina critérios específicos para a geração de relatórios (ex: alunos abaixo da média, desempenho por período).

Visualizações Avançadas: Implementar outros tipos de gráficos, como gráficos de linha para acompanhar o progresso do aluno ao longo do tempo.

Exportação de Relatórios: Opções para exportar as análises textuais e os gráficos gerados em diferentes formatos (PDF, Excel).

Multi-usuário: Implementar um sistema de autenticação para múltiplos professores.

Autor
[Kauã Santos] - [https://www.linkedin.com/in/kau%C3%A3-santos-71214a32a/]
