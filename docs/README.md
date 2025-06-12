# 🛍️ Django E-commerce | Projeto Educacional

Este é um projeto simples de e-commerce construído com **Django 5**, desenvolvido com fins **educacionais**.  
Inclui funcionalidades como carrinho de compras, listagem de produtos, checkout e integração com PayPal (na versão pessoal do autor).

---

## 🖼️ Interface do Projeto

<div align="center">

### 🏠 Página da Loja

![Home](./docs/home.png)

---

### 🏠 Página da Checkout

![Home](./docs/checkout.png)

### 🛒 Carrinho de Compras

![Carrinho](./docs/carrinho.png)

</div>

---

## 🚀 Funcionalidades

- ✅ Página de listagem de produtos
- ✅ Botão "Adicionar ao carrinho"
- ✅ Alteração de quantidade
- ✅ Checkout com total atualizado
- ✅ Estrutura pronta para login, cadastro e pedidos
- 🧪 Integração PayPal (em desenvolvimento pessoal)

---

## 🧰 Tecnologias Utilizadas

- **Django 5.1.6**
- **Python 3.10+**
- **SQLite3** (default)
- **Bootstrap 5** (CSS)
- **JavaScript** (carrinho)
- **Pillow** (para imagens)

---

## 📦 Instalação Local

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/django-ecommerce.git
cd django-ecommerce

# Crie e ative o ambiente virtual
python -m venv venv
.\venv\Scripts\activate        # No Windows
# source venv/bin/activate     # No Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Migre o banco de dados
python manage.py migrate

# Rode o servidor
python manage.py runserver

---

---

## 👤 Autor

**Edésio Rodrigues**  
🔗 [LinkedIn](https://www.linkedin.com/in/devedesio-rodrigues/)
