# 🐍 Super Módulo Flask - Aula 02

Bem-vindo ao **Super Módulo Flask Aula 02**, um projeto de continuação em **Python** utilizando a biblioteca **Flask**. Nesta etapa, evoluímos o que foi feito na aula anterior, completando o **CRUD de Produtos**, adicionando **CRUD de Usuários**, implementando **Login com sessão** e aplicando **Bootstrap** em todas as páginas HTML para uma interface moderna e responsiva.

Projeto baseado na 2ª Aula do Prof. Robson – creditado mais abaixo no texto.

---

## 📚 Conteúdo da Aula

1. **Revisão da Aula Anterior**

   * Rotas estáticas e dinâmicas.
   * Início do CRUD de produtos.

2. **CRUD Completo de Produtos**

   * **Create** → Cadastro de produtos.
   * **Read** → Listagem dos produtos cadastrados.
   * **Update** → Edição de produtos existentes.
   * **Delete** → Exclusão de produtos.

3. **CRUD de Usuários**

   * Cadastro de novos usuários.
   * Listagem de usuários.
   * Edição e exclusão de usuários.
   * Todos os usuários são protegidos e só acessíveis após login.

4. **Introdução ao Bootstrap**

   * O que é o Bootstrap:
     Um framework front-end que facilita a criação de páginas responsivas e estilosas sem precisar escrever muito CSS.

   * Principais recursos usados no projeto:

     * Grid system (layout responsivo).
     * Botões estilizados.
     * Tabelas prontas para listagem de dados.
     * Formulários organizados e bonitos.

5. **Integração do Bootstrap com Flask**

   * Aplicação do Bootstrap em todas as páginas HTML da aplicação.
   * Exemplo de uso em formulários e tabelas.

6. **Login e Sessão**

   * Tela de login inicial antes de acessar a aplicação.
   * Validação de e-mail e senha dos usuários.
   * Uso de `session` para manter o usuário logado.
   * Logout para encerrar a sessão.
   * Proteção de todas as rotas importantes: produtos, usuários e gestores.
   * Barra de navegação só aparece quando o usuário está logado.

---

## 🚀 Tecnologias Utilizadas

* Python 3.x
* Flask
* HTML/CSS
* Bootstrap (via CDN)

---

## ▶️ Como Executar o Projeto

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/super-modulo-flask-aula02.git
cd super-modulo-flask-aula02
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install flask
```

4. Execute a aplicação:

```bash
python app.py
```

5. Abra no navegador:

```bash
http://127.0.0.1:5000
```

---

## 🎨 Como usar o Bootstrap via CDN

Para adicionar o Bootstrap às páginas HTML, insira o link CDN dentro da tag `<head>` do seu arquivo:

```html
<head>
    <meta charset="UTF-8">
    <title>Minha Página Flask</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="text-center">Minha Página com Bootstrap</h1>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
```

💡 Com isso, todas as suas páginas Flask podem aproveitar a **máxima responsividade e estilo** do Bootstrap.

---

## 🔒 Funcionalidades de Login e Sessão

* O login é a **primeira rota do site**, garantindo que o usuário esteja autenticado antes de acessar a aplicação.
* Após login bem-sucedido, o usuário é redirecionado para a home.
* Logout encerra a sessão, protegendo rotas como `/produtos` e `/usuarios`.
* A barra de navegação só aparece se o usuário estiver logado.
* Rotas protegidas incluem CRUD de produtos e usuários.

---

## 👨‍🏫 Créditos

Projeto desenvolvido a partir da aula do Prof. Robson – Escola Infinity Fortaleza/CE
👉 GitHub do Prof. Robson: [https://github.com/robson400](https://github.com/robson400)
