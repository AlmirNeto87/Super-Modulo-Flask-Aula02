#🐍 Super Módulo Flask - Aula 02

Bem-vindo ao **Super Módulo Flask Aula 02**, um projeto de continuação em **Python** utilizando a biblioteca **Flask**.
Nesta etapa, evoluímos o que foi feito na aula anterior, completando o **CRUD** de Produtos e aplicando **Bootstrap** em todas as páginas HTML para dar mais estilo e responsividade à aplicação.

Projeto Baseado na 2ª Aula do Prof. Robson – Creditado mais abaixo no texto.
---

#@📚 Conteúdo da Aula

1. **Revisão da Aula Anterior**
  -Rotas estáticas e dinâmicas.
  -Início do CRUD de produtos.

2. **CRUD Completo de Produtos**
  -Create → Cadastro de produtos.
  -Read → Listagem dos produtos cadastrados.
  -Update → Edição de produtos existentes.
  -Delete → Exclusão de produtos.

3. **Introdução ao Bootstrap**
  -O que é o Bootstrap:
Um framework front-end que facilita a criação de páginas responsivas e estilosas sem precisar escrever muito CSS.

  -Principais recursos usados no projeto:
    -Grid system (layout responsivo).
    -Botões estilizados.
    -Tabelas prontas para listagem de dados.
    -Formulários organizados e bonitos.

4. **Integração do Bootstrap com Flask**
  -Aplicação do Bootstrap em todas as páginas HTML da aplicação.
  -Exemplo de uso em formulários e tabelas.

---

##🚀 Tecnologias Utilizadas
  -Python 3.x
  -Flask
  -HTML/CSS
  -Bootstrap (via CDN)
  
---

##▶️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/super-modulo-flask-aula01.git
   cd super-modulo-flask-aula01
   
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
     python -m venv venv
     source venv/bin/activate   # Linux/Mac
     venv\Scripts\activate      # Windows

4. Instale as dependências:
   ```bash
   pip install flask

5. Execute a aplicação:
   ```bash
   python app.py

7. Abra no navegador:
   ```bash
   http://127.0.0.1:5000


##🎨 Como usar o Bootstrap via CDN

Para adicionar o Bootstrap às páginas HTML, basta inserir o link CDN dentro da tag <head> do seu arquivo:
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


#Com isso, todas as suas páginas Flask já podem aproveitar a mágica do Bootstrap 🎉.

##👨‍🏫 Créditos

Projeto desenvolvido a partir da aula do Prof. Robson – Escola Infinity Fortaleza/CE
👉 GitHub do Prof. Robson
