 Inventário de Jogos
API REST desenvolvida em Python utilizando Flask para gerenciar um inventário de jogos.
Descrição
Esta aplicação permite realizar operações de **CRUD (Create, Read, Update, Delete)** em um banco de dados SQLite, armazenando informações sobre jogos como nome, gênero, plataforma, quantidade e preço.
Tecnologias utilizadas
* Python 3
* Flask
* SQLite
Estrutura do projeto

```
inventario-jogos/
│
├── app.py          # API principal
├── init_db.py      # Script de criação do banco
├── jogos.db        # Banco de dados (gerado automaticamente)
└── README.md
```
 Instalação
1. Criar ambiente virtual

```bash
python -m venv venv
```
 2. Ativar ambiente virtual
Windows (PowerShell):
```bash
venv\Scripts\Activate
```
**Linux/Mac:**
```bash
source venv/bin/activate
```
---
3. Instalar dependências
```bash
pip install flask
```
 Inicializar o banco de dados
```bash
python init_db.py
```
 Executar a aplicação

```bash
python app.py
```
A API estará disponível em:

```
http://127.0.0.1:5000
```
Rotas da API

 GET - Listar todos os jogos

```bash
curl http://127.0.0.1:5000/jogos
```
 GET - Buscar jogo por ID

```bash
curl http://127.0.0.1:5000/jogos/1
```
 POST - Criar novo jogo

```bash
curl -X POST http://127.0.0.1:5000/jogos \
-H "Content-Type: application/json" \
-d '{
  "nome": "God of War",
  "genero": "Ação",
  "plataforma": "PlayStation",
  "quantidade": 10,
  "preco": 199.90
}'
```
 PUT - Atualizar jogo
```bash
curl -X PUT http://127.0.0.1:5000/jogos/1 \
-H "Content-Type: application/json" \
-d '{
  "nome": "God of War Ragnarok",
  "genero": "Ação",
  "plataforma": "PlayStation",
  "quantidade": 5,
  "preco": 249.90
}'
```
DELETE - Remover jogo

```bash
curl -X DELETE http://127.0.0.1:5000/jogos/1
```
## 📊 Estrutura do banco

Tabela: `jogos`

| Campo      | Tipo         |
| ---------- | ------------ |
| id         | INTEGER (PK) |
| nome       | TEXT         |
| genero     | TEXT         |
| plataforma | TEXT         |
| quantidade | INTEGER      |
| preco      | REAL         |
## ✅ Critérios atendidos
* ✔ CRUD completo
* ✔ Uso de SQL (SELECT, INSERT, UPDATE, DELETE)
* ✔ Padrão REST
* ✔ Retorno em JSON
* ✔ Organização de código
* ✔ Script de inicialização do banco
## 🚀 Melhorias futuras

* Filtros por gênero ou plataforma
* Ordenação de resultados
* Interface web
* Autenticação de usuários

Projeto para fins acadêmicos
