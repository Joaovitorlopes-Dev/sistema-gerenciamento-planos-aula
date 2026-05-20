# 📚 Gerenciador de Planos de Aula

Sistema web moderno para criação e gerenciamento de planos de aula, desenvolvido com React, Flask e SQLite.

---

# 🚀 Tecnologias Utilizadas

## Frontend
- React
- Vite
- Axios
- React Icons
- CSS3

## Backend
- Flask
- Flask SQLAlchemy
- Flask CORS
- SQLite

---

# 🎯 Funcionalidades

✅ Criar planos de aula  
✅ Listar planos  
✅ Editar planos  
✅ Deletar planos  
✅ Buscar planos por título  
✅ Interface moderna em Dark Mode  
✅ Integração Frontend + Backend  
✅ API REST com Flask  
✅ Banco de dados SQLite  

---

# 📂 Estrutura do Projeto

```bash
backend/
frontend/
```

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/Joaovitorlopes-Dev/sistema-gerenciamento-planos-aula
```

---

## 2️⃣ Entrar na pasta do projeto

```bash
cd sistema-gerenciamento-planos-aula
```

---

# 📦 Configurando o Backend (Flask)

## 3️⃣ Entrar na pasta backend

```bash
cd backend
```

---

## 4️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

---

## 5️⃣ Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 6️⃣ Instalar dependências do backend

```bash
pip install flask flask_sqlalchemy flask_cors python-dotenv openai
```

---

## 7️⃣ Executar o backend

```bash
python app.py
```

Se tudo der certo aparecerá algo parecido com:

```bash
Running on http://127.0.0.1:5000
```

⚠️ IMPORTANTE:
Deixe esse terminal aberto.

---

# 💻 Configurando o Frontend (React + Vite)

## 8️⃣ Abrir um NOVO terminal

---

## 9️⃣ Entrar na pasta frontend

```bash
cd frontend
```

---

## 🔟 Instalar dependências do frontend

```bash
npm install
```

---

## 1️⃣1️⃣ Executar frontend

```bash
npm run dev
```

Se tudo der certo aparecerá:

```bash
Local: http://localhost:5173
```

---

# 🌐 Abrir o Projeto

Abra no navegador:

```bash
http://localhost:5173
```

---

# 🔌 Endpoints da API

## Listar planos

```http
GET /lesson-plans
```

---

## Buscar plano por ID

```http
GET /lesson-plans/:id
```

---

## Criar plano

```http
POST /lesson-plans
```

---

## Atualizar plano

```http
PUT /lesson-plans/:id
```

---

## Remover plano

```http
DELETE /lesson-plans/:id
```

---

# 🗄️ Banco de Dados

O sistema utiliza SQLite.

O banco é criado automaticamente ao iniciar o backend.

Arquivo:

```bash
database.db
```

---

# 🖥️ Interface

O sistema possui:
- Dark Mode
- Cards modernos
- Sidebar
- Busca em tempo real
- CRUD completo

---

# ✅ IMPORTANTE

Para o sistema funcionar corretamente:

- O backend deve estar rodando
- O frontend deve estar rodando
- Os dois terminais precisam permanecer abertos durante o uso do sistema

---

# 👨‍💻 Desenvolvedor

João Vitor Lopes

- Estudante de Sistemas de Informação
- Desenvolvedor Full Stack
- Python | React | JavaScript

---

# 📌 Melhorias Futuras

- Smart Assist com IA
- Filtros avançados
- Paginação
- Docker
- Deploy
- Autenticação