# impacta_mlops
MBA DSA_31_2025 - IMPACTA - Aulas de MLOps - Running ML in Production Environments 

# Projeto MLOps – Previsão de Preço de Diamantes

Este repositório faz parte da disciplina **MLOps – Running ML in Production
Environments**.
O objetivo do projeto é mostrar, passo a passo, como evoluir de um fluxo manual em
notebooks para um projeto de Machine Learning organizado, reprodutível e pronto para
automação, seguindo boas práticas de MLOps.

---

## Contexto até aqui

Na **Aula 1**,

 trabalhamos com um fluxo típico de ciência de dados:

- EDA em notebook
- Treino e inferência manual
- Uso inicial do MLflow para registrar experimentos
  
Esse fluxo funciona, mas não escala e não é fácil de repetir.
Na **Aula 2**, o foco foi **organizar o projeto e estruturar o ciclo de dados**,
preparando o terreno para automação e evolução do pipeline nas próximas aulas.

---

## O que foi feito na Aula 2

Nesta etapa, o projeto passou por uma reorganização importante:

- Criação de um repositório GitHub
- Estruturação do projeto em pastas claras
- Separação da lógica de dados em um módulo Python
- Criação de um ponto único para carregar e dividir os dados
- Integração do notebook com o código do projeto
  
O notebook deixou de ser responsável por toda a lógica de dados e passou a **consumir
funções reutilizáveis**.

---

## O que foi feito na Aula 3

Na Aula 3, o projeto evoluiu do preparo de dados para um **pipeline completo de modelagem**.

Foram implementados:

- separação da lógica de modelagem em módulos Python
- pipeline de pré-processamento e treino com scikit-learn
- script de treino executável via linha de comando
- avaliação padronizada de métricas de regressão
- experiment tracking completo com MLflow
- versionamento de modelos no MLflow Model Registry
- testes automatizados com pytest
  
A partir deste ponto, o modelo deixa de depender do notebook e passa a ser tratado
como um **artefato versionado e rastreável**.

---

## Estrutura atual do projeto

```text
impacta_mlops/
│
├── notebooks/
│ └── eda_diamonds.ipynb
│
├── src/
│ ├── data.py
│ ├── model.py
│ ├── __init__.py
│ └── evaluate.py
│
├── app/
│
├── tests/
│ ├── test_data.py
│ ├── __init__.py
│ ├── test_model.py
│ └── test_train.py
│
├── models/
│ └── diamond_price_model.joblib
│
├── requirements.txt
├── train.py
├── pytest.ini
├── main.py
├── README.md
└── .gitignore
```

---

## Módulo de dados

O arquivo `src/data.py` centraliza a lógica relacionada aos dados:

- carregamento do dataset `diamonds` do seaborn
- separação de features e target
- divisão em treino e teste
  
Isso garante que todos usem **o mesmo processo de preparação**, evitando inconsistências
entre notebooks e scripts.

---

## Uso no notebook

O notebook agora utiliza diretamente o módulo de dados:

```python

from src.data import train_test_split_diamonds
X_train, X_test, y_train, y_test = train_test_split_diamonds()
```

Com isso:

- a lógica de dados fica centralizada
- o notebook fica mais simples
- o código se torna reutilizável
- o projeto começa a ganhar reprodutibilidade

---

## Ambiente de desenvolvimento

Recomenda-se o uso de ambiente virtual.

Criar e ativar o ambiente:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Instalar dependências:
```bash
pip install -r requirements.txt
```

---

### – Pipeline de treino

O treino do modelo é executado via script Python, sem dependência de notebook.
Execução padrão:

```bash
python train.py
```

É possível ajustar hiperparâmetros via linha de comando:

```bash
python train.py --max_depth 3
```

Durante o treino, são registrados no MLflow:

parâmetros
métricas
artefatos
modelo treinado

Isso permite comparar experimentos e versionar modelos de forma consistente.

---

### Testes automatizados
O projeto possui testes básicos para garantir

---

Execução dos testes:

```bash
pytest
```

Os testes cobrem:
carregamento e split dos dados
construção do pipeline de modelagem
execução completa do script de treino
Esses testes ajudam a garantir que refatorações não quebrem o fluxo principal.