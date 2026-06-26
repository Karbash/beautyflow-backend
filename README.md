# BeautyFlow API

Backend em Flask para gerenciar pacientes e estatísticas de pele.

## Descrição

Este projeto fornece uma API simples para cadastrar, listar, editar, excluir pacientes e gerar estatísticas de tipos de pele usando SQLite.

## Instalação

1. Navegue até a pasta do backend:
   ```bash
   cd backend-api
   ```

2. Crie e ative um ambiente virtual Python:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Inicialização

1. Execute a API:
   ```bash
   python app.py
   ```

2. Por padrão, a aplicação roda em:
   ```
   http://localhost:5000
   ```

## Endpoints principais

- `GET /pacientes` - lista pacientes
- `POST /pacientes` - cadastra um paciente
- `PUT /pacientes/<id>` - atualiza um paciente
- `DELETE /pacientes/<id>` - exclui um paciente
- `GET /estatisticas` - retorna estatísticas de tipos de pele

## Observações

- O banco de dados SQLite fica em `backend-api/database.db`.
- A documentação Swagger pode ser carregada caso a extensão ou ferramentas suportem `swagger.yaml`.
