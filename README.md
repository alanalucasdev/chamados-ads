# API de Chamados de Suporte — ADS/UFCA

Projeto desenvolvido no âmbito da disciplina de Programação Web, do curso de Análise e Desenvolvimento de Sistemas (ADS) da Universidade Federal do Cariri (UFCA), ministrada pelo professor Jayr Pereira.

## Identificação da Estudante

Curso: Análise e Desenvolvimento de Sistemas (ADS)
Instituição: Universidade Federal do Cariri (UFCA)
Disciplina: ADS0021 | PROGRAMAÇÃO PARA WEB - 2026.2
Professor: Prof. Dr. Jayr Alencar Pereira
Aluna: Alana Maria Brito Lucas

## Objetivo do Projeto

O projeto tem como finalidade desenvolver uma API REST em Python para o gerenciamento de chamados de suporte técnico, seguindo o conceito de um sistema Help Desk.

Ao longo das etapas da disciplina, serão implementadas funcionalidades para abertura, consulta, acompanhamento, atribuição e resolução de solicitações de atendimento.

Nesta primeira etapa, o objetivo é estabelecer a estrutura inicial da aplicação utilizando Flask, configurar o ambiente de desenvolvimento com o gerenciador de dependências `uv` e disponibilizar uma rota inicial para verificar o funcionamento da API.

## Tecnologias Utilizadas

- **Linguagem:** Python.
- **Framework Web:** Flask.
- **Gerenciador de ambiente e dependências:** uv.
- **Controle de versão:** Git e GitHub.

## Como Executar o Projeto

### Pré-requisitos

É necessário ter Python e o gerenciador `uv` instalados no ambiente de desenvolvimento.

Caso ainda não tenha o `uv`, sua instalação pode ser realizada com:

```bash
pip install uv
```

### 1. Clonar o repositório

```bash
git clone https://github.com/alanalucasdev/chamados-ads.git
```

Acesse a pasta do projeto:

```bash
cd chamados-ads
```

### 2. Instalar as dependências

Para configurar o ambiente virtual e instalar as dependências nas versões registradas no arquivo `uv.lock`, execute:

```bash
uv sync --locked
```

Esse procedimento garante que o ambiente seja configurado de acordo com as dependências especificadas no projeto.

### 3. Executar a aplicação

Para iniciar o servidor Flask em ambiente local, utilize:

```bash
uv run flask --app app run
```

**No GitHub Codespaces**, execute o seguinte comando para disponibilizar a aplicação na porta 5000:

```bash
uv run flask --app app run --host=0.0.0.0 --port=5000
```

Após iniciar a aplicação, o servidor estará disponível para receber requisições.

## Endpoint Disponível

Nesta primeira etapa, foi implementada a rota inicial da API, destinada à verificação do seu funcionamento.

| Método HTTP | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Retorna uma mensagem indicando que a API de chamados está em funcionamento. |

### Como acessar a rota inicial

Com a aplicação em execução, acesse pelo navegador:

```text
http://localhost:5000/
```

Também é possível realizar a requisição pelo terminal utilizando o comando:

```bash
curl -i http://localhost:5000/
```

### Resposta esperada

A API deverá retornar o código HTTP `200 OK`, com o cabeçalho `Content-Type: application/json` e o seguinte objeto JSON:

```json
{
  "mensagem": "API de chamados em funcionamento"
}
```

## Organização do Repositório

A estrutura inicial do projeto está organizada da seguinte forma:

```text
chamados-ads/
├── app.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

O ambiente virtual, armazenado na pasta `.venv/`, não deve ser enviado ao GitHub. Para isso, a pasta está incluída no arquivo `.gitignore`, juntamente com arquivos temporários como `__pycache__/`.

## Etapa de Desenvolvimento

**Semana 1 — Estruturação Inicial da API**

Nesta etapa, foi criada a aplicação Flask e implementada a rota `GET /`, responsável por retornar uma mensagem de confirmação do funcionamento da API.

Também foram configurados o ambiente de desenvolvimento, o gerenciamento de dependências com `uv` e o versionamento do projeto utilizando Git e GitHub, com a identificação da entrega por meio da tag `semana-01`.

---

**Universidade Federal do Cariri (UFCA)**  
**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Disciplina:** Programação Web  
**Professor:** Jayr Pereira