# JulioMiyahira - Estagiario Monitoramento STI TJMS

from flask import Flask, render_template, request, flash
import sys
import bd, funcoes
import pprint

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    lista = funcoes.listar()
    listaInfra = ['Banheiro familiar', 'Fraldário', 'Espaço kids', 'Monitor infantil', 'Microondas']
    listaAdici = ['Acessibilidade', 'Estacionamento coberto', 'Elevador']
    return render_template('index.html', lista=lista, listaInfra=listaInfra, listaAdici=listaAdici)

@app.route('/cadastro')
def cadastrar():
    # funcoes.dados(reqform)
    message = ''
    return render_template('cadastro.html', message=message)

@app.route('/empresa', methods=['POST'])
def empresa():
    reqform = funcoes.valida_reqform(request.form, funcoes.dadosinit())
    if funcoes.buscaSeJaTem(reqform['nome_estabelecimento']):
        # message = "Estabelecimento já cadastrado"
        # return render_template('cadastro.html', message=message)
        return 'Estabelecimento já cadastrado'
    else:
        funcoes.adiciona_dados(reqform)
        title = 'Cadastrado'
        reqform = funcoes.chamaReqFormComListaCheckbox(reqform)
        print(type(reqform['infraestrutura']))
        lista = ['banheiro', 'microondas', 'cozinha', 'monitores']
        return render_template('empresa.html', req=reqform, lista=lista, title=title)

@app.route('/buscar', methods=['POST'])
def buscar():
    req = request.form['estabelecimento']

    # infra = request.form['infraestrutura']

    # for i in infra:
    #     print(i)
    #print(req)
    
    if funcoes.buscaSeJaTem(req):
        req = funcoes.buscaEstabelecimento(req)
        # req = req['nome_estabelecimento']
        #print(type(req))
        req = funcoes.chamaReqFormComListaCheckbox(req)
        # print(req['infraestrutura'])
        # for i in req['infraestrutura']:
        #     print(i)
        title = req['nome_estabelecimento']
        # lista = ['banheiro', 'microondas', 'cozinha', 'monitores'] 
        return render_template('empresa.html', req=req, title=title)
    else:
        # flash('nao tem')
        return "nao tem cadastrado ainda"

@app.route('/login')
def login():
    #lista = correios.listar()
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():   
    nome        = request.form['name']
    sobrenome	= request.form['surname']
    email 		= request.form['email']
    senha 		= request.form['password']

    bd.cadastro(nome, sobrenome, email, senha)
    print('cadastrou')
    return render_template('foi.html', name=nome, surname=sobrenome, email=email, password=senha)
    #processed_text = text.upper()
    #return processed_text

@app.route('/login2', methods=['POST'])
def login2():   
    email 		= request.form['email']
    senha 		= request.form['password']

    bd.validalogin(email, senha)
    print('login')
    return render_template('foi.html', name=nome, surname=sobrenome, email=email, password=senha)
    #processed_text = text.upper()
    #return processed_text


# @app.route('/empresa')
# def index_emp():
#     #lista = correios.listar()
#     return render_template('empresa.html')

# @app.route('/empresa', methods=['POST'])
# def empresa():
#     nome_empresa 	= request.form['nome_empresa']
#     endereco 		= request.form['endereco']
#     cidade 		    = request.form['cidade']
#     telefone 		= request.form['telefone']


#     #bd.cadastraempresa(nome_empresa, endereco, cidade, telefone)
#     print('empresa')
#     return render_template('empresafoi.html', name=nome_empresa, endereco=endereco, cidade=cidade, telefone=telefone)
#     #processed_text = text.upper()
#     #return processed_text




if __name__ == '__main__':
    app.run(debug=True)
