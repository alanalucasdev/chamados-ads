
# API de Chamados de Suporte — ADS/UFCA

Projeto desenvolvido no âmbito da disciplina de Programação Web, do curso de Análise e Desenvolvimento de Sistemas (ADS) da Universidade Federal do Cariri (UFCA).

## Identificação da Estudante

- **Curso:** Análise e Desenvolvimento de Sistemas (ADS)
- **Instituição:** Universidade Federal do Cariri (UFCA)
- **Disciplina:** ADS0021 | PROGRAMAÇÃO PARA WEB - 2026.2
- **Professor:** Prof. Dr. Jayr Alencar Pereira
- **Aluna:** Alana Maria Brito Lucas

## Objetivo do Projeto

Desenvolver uma API REST em Python para o gerenciamento de chamados de suporte técnico, seguindo o conceito de um sistema Help Desk.

A aplicação permite cadastrar chamados, listar todos os registros e consultar um chamado específico pelo seu identificador.

Nesta etapa, os dados são armazenados temporariamente em memória, utilizando estruturas Python, sem necessidade de banco de dados.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework Web:** Flask
- **Gerenciador de ambiente e dependências:** uv
- **Controle de versão:** Git e GitHub

## Como Executar o Projeto

### Pré-requisitos

É necessário ter Python e o gerenciador `uv` instalados.

Caso ainda não tenha o `uv`, instale com:

```bash
pip install uv
```

### 1. Clonar o repositório

```bash
git clone https://github.com/alanalucasdev/chamados-ads.git
cd chamados-ads
```

### 2. Instalar as dependências

```bash
uv sync --locked
```

### 3. Executar a aplicação

```bash
uv run python app.py
```

O servidor Flask será iniciado no endereço:

```text
http://127.0.0.1:5000
```

## Endpoints da API

| Método HTTP | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verifica o funcionamento da API. |
| POST | `/chamados` | Cadastra um novo chamado. |
| GET | `/chamados` | Lista todos os chamados cadastrados. |
| GET | `/chamados/<id>` | Consulta um chamado pelo identificador. |

## Exemplos de utilização

### 1. Rota inicial — GET /

Endereço:

```text
http://127.0.0.1:5000/
```

Resposta esperada — HTTP 200:

```json
{
  "mensagem": "API de chamados em funcionamento"
}
```

### 2. Cadastrar chamado — POST /chamados

Endereço:

```text
http://127.0.0.1:5000/chamados
```

Exemplo de JSON enviado:

```json
{
  "titulo": "Impressora sem conexão",
  "descricao": "A impressora do laboratório não aparece na rede.",
  "solicitante": "Ana",
  "prioridade": "media"
}
```

Resposta esperada — HTTP 201:

```json
{
  "titulo": "Impressora sem conexão",
  "descricao": "A impressora do laboratório não aparece na rede.",
  "solicitante": "Ana",
  "prioridade": "media",
  "id": 1,
  "status": "aberto"
}
```

O identificador é gerado automaticamente pela aplicação, e o status inicial do chamado é definido como `aberto`.

### 3. Listar chamados — GET /chamados

Endereço:

```text
http://127.0.0.1:5000/chamados
```

Retorna um array JSON com todos os chamados cadastrados.

Quando não houver chamados, retorna:

```json
[]
```

### 4. Consultar chamado por identificador — GET /chamados/1

Endereço:

```text
http://127.0.0.1:5000/chamados/1
```

Quando o chamado existir, retorna seus dados com HTTP 200.

Quando não existir, retorna HTTP 404:

```json
{
  "mensagem": "Chamado não encontrado"
}
```

## Armazenamento dos Dados

Os chamados são armazenados temporariamente em uma lista Python durante a execução da aplicação.

Os dados podem ser perdidos quando o servidor é reiniciado. Esse comportamento é esperado nesta etapa do desenvolvimento.

## Organização do Repositório

```text
chamados-ads/
├── app.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

As pastas `.venv/` e `__pycache__/`, assim como arquivos temporários, são ignorados pelo Git por meio do arquivo `.gitignore`.

## Etapas de Desenvolvimento

**Semana 1 — Estruturação Inicial da API**

Criação da aplicação Flask, implementação da rota inicial GET /, configuração do ambiente de desenvolvimento e gerenciamento de dependências com uv.

Entrega identificada pela tag `semana-01`.

**Semana 2 — Cadastro, Listagem e Consulta de Chamados**

Implementação das funcionalidades de cadastro de chamados (POST /chamados), listagem (GET /chamados) e consulta por identificador (GET /chamados/<id>).

Os registros são armazenados em memória utilizando estruturas Python, com geração automática de identificadores e definição do status inicial como aberto.

Entrega identificada pela tag `semana-02`.

---

**Universidade Federal do Cariri (UFCA)**  
**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Disciplina:** Programação Web  
**Professor:** Jayr Alencar Pereira
