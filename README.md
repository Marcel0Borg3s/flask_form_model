
# 🧾 Formulário Flask - v0

Projeto simples em Flask com um formulário HTML estilizado em CSS, que coleta dados e os processa em uma função Python.

## 🚀 Funcionalidades

- Frontend com formulário HTML e CSS personalizado
- Backend em Python com Flask
- Processamento de dados do formulário no `main.py`
- Pronto para deploy no Render.com

---

## 🏗️ Estrutura do Projeto

```
Flask_v0/
│
├── static/
│   ├── img/
│   │   └── octocat.png
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── obrigado.html
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/flask-v0.git
cd flask-v0
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate     # No Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode o app:

```bash
python app.py
```

Acesse em [http://localhost:5000](http://localhost:5000).

---

## 🌐 Deploy gratuito no Render.com

1. Crie uma conta gratuita no [Render.com](https://render.com).
2. Conecte seu GitHub.
3. Crie um novo Web Service com:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3.x

Pronto! O app estará online 🎉

---

## 📬 Contato

Feito por [Marcelo Borges, marcelosbgs@gmail.com]


