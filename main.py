from flask import Flask, render_template,request, redirect, url_for
#Instanciando o objeto Flask a variavel app
app = Flask(__name__)

lista_produtos = [
    {'id': 1, 'nome': 'Camisa ', 'preco': 50.00},
    {'id': 2, 'nome': 'Regata', 'preco': 120.00},
    {'id': 3, 'nome': 'Calça Jeans', 'preco': 30.00},
    {'id': 4, 'nome': 'Bermuda', 'preco': 250.00}
]

listagem_usuarios = [
    {'id': 1, 'senha': '123456', 'email': 'almirneto@uol.com'},
    ]


#-----------------------------------------------------------------------------
#Criacao de ROTAS (routes)
#Para criar mais de uma rota para o mesmo caminho basta deixas juntas
# funcao render_template e usada para renderizar pagina html
#-----------------------------------------------------------------------------

@app.route('/home')
def home():
# E Possivel passar variaveis com descontrucao para a pagina que sta sendo rendenrizada 
  return render_template('index.html',titulo ="Home Page")

#--------------------------------------------------------------------------------
#Criacao de rota para a pagina sobre
#--------------------------------------------------------------------------------
@app.route('/sobre')
def sobre():
  return render_template('sobre.html',titulo ="Sobre")

#--------------------------------------------------------------------------------
#Criacao de rota para a pagina contatos
#--------------------------------------------------------------------------------
@app.route('/contatos')
def contatos():
  return render_template('contatos.html', titulo="Contatos")


#--------------------------------------------------------------------------------
#Criacao de rota para a pagina produtos
#Rota para exibir os produtos da lista , mandando a lista de produtos para a renderizacao do template
#--------------------------------------------------------------------------------
@app.route('/produtos')
def listar_produtos():
  return render_template('produtos.html', titulo="Lista de Produtos", produtos=lista_produtos)

#--------------------------------------------------------------------------------
#Criacao de rota para cadastrar produtos  
# Formulario para cadastrar produtos
# Suporta métodos GET (exibir formulário) e POST (enviar formulário)
#--------------------------------------------------------------------------------
@app.route('/produtos/cadastro', methods=['GET', 'POST'])
def cadastrar_produtos():
  if request.method == 'POST':
    novoProduto = {
      # Funcao para preencher o id com o numero maior de id que tiver dentro da lista e caso nao encontre nenhum coloca como default =0
      "id":max([p["id"] for p in lista_produtos],default=0) + 1,
      "nome": request.form["nome"],
      "preco": float(request.form["preco"])
    }
    lista_produtos.append(novoProduto)
    return redirect (url_for('listar_produtos'))
  
  return render_template('cadastrar_produto.html', titulo="Cadastrar Produto")

#--------------------------------------------------------------------------------
#Criacao de rota para editar produtos
# Formulario para editar produtos
# Suporta métodos GET (exibir formulário) e POST (enviar formulário)
#--------------------------------------------------------------------------------
@app.route('/produtos/editar/<int:id>', methods=['GET','POST'])
def editar_produto(id):
  produtoNovo = None
  for produto in lista_produtos:
    if produto["id"] == id:
      produtoNovo = produto
      break  
  if produtoNovo is None:
    return render_template(page_not_found)
  if request.method =='POST':
    produtoNovo["nome"] = request.form['nome']
    produtoNovo["preco"] = float(request.form['preco'])
    return redirect(url_for('listar_produtos'))
  return render_template('editar_produto.html', produto = produtoNovo, titulo="Editar Produto")

#--------------------------------------------------------------------------------
#Criacao de rota para deletar produtos
# Tem como parametro o id do produto a ser deletado
#--------------------------------------------------------------------------------
@app.route('/produtos/deletar/<int:id>')
def deletar_produto(id):
  produtoDeletado = None
  for produto in lista_produtos:
    if produto["id"] == id:
      produtoDeletado = produto
      break
  if produtoDeletado is None:
    return render_template(page_not_found)
  lista_produtos.remove(produtoDeletado)
  return redirect(url_for('listar_produtos'))


#--------------------------------------------------------------------------------
#Criacao de rota para a pagina login
#--------------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def login():
  loginErro = None
  usuario = None
  if request.method == 'POST':
    # Pega os dados enviados pelo formulário
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Procura na lista de usuários se existe algum com esse email e senha
    for user in listagem_usuarios:
      if user["email"] == email and user["senha"] == senha:
        usuario = user   # Se encontrou, guarda o usuário
        break         # Para o loop (não precisa continuar procurando)

  # Se encontrou o usuário, redireciona para a home
    if usuario:
      return redirect(url_for('home'))
    else:
  
      # Se não encontrou, mostra mensagem de erro
      loginErro = "E-mail ou senha incorretos."

  # Se for GET ou se o login falhar, renderiza a página de login
  return render_template('login.html', titulo="Login", loginErro=loginErro)


@app.route('/produtos/pesquisar', methods=['GET'])
def pesquisar_produto():
    query = request.args.get('q', '').lower()  # pega o texto do input
    if query:
        resultados = [p for p in lista_produtos if query in p['nome'].lower()]
    else:
        return redirect(url_for('listar_produtos'))  # Redireciona para a lista

    return render_template('produto.html', titulo=f"Resultados para '{query}'", produtos=resultados)


#--------------------------------------------------------------------------------
# Cria uma rota para caminhos inexistentes 
# Manipulador de erro 404 (Página não encontrada)
#--------------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error_code=404, error_message="Página não encontrada."), 404

#--------------------------------------------------------------------------------
# Cria uma rota para erros internos do servidor
# Manipulador de erro 500 (Erro interno do servidor)
#--------------------------------------------------------------------------------
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html', error_code=500, error_message="Erro interno no servidor. Tente novamente mais tarde."), 500


#--------------------------------------------------------------------------------
#Funcao para executar o flask 
#--------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)