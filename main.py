from flask import Flask, render_template,request, redirect, url_for
#Instanciando o objeto Flask a variavel app
app = Flask(__name__)

lista_produtos = [
    {'id': 1, 'nome': 'Camisa ', 'preco': 50.00},
    {'id': 2, 'nome': 'Regata', 'preco': 120.00},
    {'id': 3, 'nome': 'Calça Jeans', 'preco': 30.00},
    {'id': 4, 'nome': 'Bermuda', 'preco': 250.00}
]

#Criacao de ROTAS (routes)
#Para criar mais de uma rota para o mesmo caminho basta deixas juntas
# funcao render_template e usada para renderizar pagina html
@app.route('/')
@app.route('/home')
def home():
# E Possivel passar variaveis com descontrucao para a pagina que sta sendo rendenrizada 
  return render_template('index.html',titulo ="Home Page")


@app.route('/sobre')
def sobre():
  return render_template('sobre.html',titulo ="Sobre")

@app.route('/contatos')
def contatos():
  return render_template('contatos.html', titulo="Contatos")

#Criacao de rota dinamica passando uma variavel '/rota/<tipo_variavel:variavel>'
@app.route('/contato/<int:num>')
def verNumero(num):
  return f'O numero do Contato e {num}'

#Rota para exibir os produtos da lista , mandando a lista de produtos para a renderizacao do template
@app.route('/produtos')
def listar_produtos():
  return render_template('produtos.html', titulo="Lista de Produtos", produtos=lista_produtos)

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


# Cria uma rota para caminhos inexistentes 
# Manipulador de erro 404 (Página não encontrada)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error_code=404, error_message="Página não encontrada."), 404

# Manipulador de erro 500 (Erro interno do servidor)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html', error_code=500, error_message="Erro interno no servidor. Tente novamente mais tarde."), 500

#Funcao para executar o flask 
if __name__ == "__main__":
    app.run(debug=True)