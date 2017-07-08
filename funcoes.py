import nomes_estabelecimentos
from pprint import pprint
from imp import reload
import json

dicInfra = {}
dicAdici = {}

# Monta lista com o nome dos estabelecimentos
def listar():
  print('[*] - DEBUG Funcao- listar')
  reload(nomes_estabelecimentos)
  lista = []
  X = nomes_estabelecimentos
  for i in dir(nomes_estabelecimentos):
    if ('__' not in i):
      a = getattr(nomes_estabelecimentos, i)
      for k in a:
        if k == 'nome_estabelecimento':
          lista.append(a[k])
  return lista

# Salva os dados no 'banco de dados'
def adiciona_dados(reqform):
  print('[*] - DEBUG Funcao- adiciona_dados')
  #pprint(reqform)
  f = open('nomes_estabelecimentos.py', 'a')
  # print(type(reqform))
  nome = reqform['nome_estabelecimento'].replace(' ', '')
  if nome != '':
    f.write(
      nome+" = {"
      "'nome_estabelecimento': '" +reqform['nome_estabelecimento']+"',"
      "'endereco_address': '"     +reqform['endereco_address']+"',"
      "'endereco_city': '"        +reqform['endereco_city']+"',"
      "'endereco_state': '"       +reqform['endereco_state']+"',"
      "'endereco_zip': '"         +reqform['endereco_zip']+"',"
      "'telefone': '"             +reqform['telefone']+"',"
      "'infraestrutura': " +' " '+   str(reqform['infraestrutura']) + ' " '+ ","
      "'adicionais': "    +' " '+   str(reqform['adicionais'])      + ' " '+ ","
      "'aberturaH': '"            +reqform['aberturaH']+"',"
      "'aberturaM': '"            +reqform['aberturaM']+"',"
      "'fechaH': '"               +reqform['fechaH']+"',"
      "'fechaM': '"               +reqform['fechaM']+"',"
      "'menorMovH': '"            +reqform['menorMovH']+"',"
      "'menorMovM': '"            +reqform['menorMovM']+"',"
      "'descricao': '"            +reqform['descricao']+"'"
      "} \n\n"
      )
  f.close()

# [GAMBIARRA] Dados iniciais do formulario
def dadosinit():
  print('[*] - DEBUG Funcao- dadosinit')
  reqform = {
    'nome_estabelecimento': '',
    'endereco_address': '',
    'endereco_city': '',
    'endereco_state': '',
    'endereco_zip': '',
    'telefone': '',
    'infraestrutura': '',
    'adicionais': '',
    'aberturaH': '',
    'aberturaM': '',
    'fechaH': '',
    'fechaM': '',
    'menorMovH': '',
    'menorMovM': '',
    'descricao': ''
  }
  return reqform

# Valida o formulario inserido com os dados iniciais
def valida_reqform(reqform, dadosinit):
  print('[*] - DEBUG Funcao- valida_reqform')
  infraestrutura = reqform.getlist('infraestrutura[]')
  adicionais = reqform.getlist('adicionais[]')
  #print(infraestrutura)
  #print(adicionais)
  reqform = reqform.to_dict()
  for key in dadosinit:
    #print(key)
    if key not in reqform:
      reqform[key] = ''
    if key == 'infraestrutura':
      reqform[key] = infraestrutura
    if key == 'adicionais':
      reqform[key] = adicionais

  return reqform

# Busca pelo nome o estebelecimento escolhido retorna obj
def buscaEstabelecimento(nome):
  print('[*] - DEBUG Funcao- buscaEstabelecimento')
  # print(nome)
  nome = nome.replace(' ', '')
  for i in dir(nomes_estabelecimentos):
    if nome in i:
      a = getattr(nomes_estabelecimentos, i)
      #print(type(a))
  return a

# Booleano se já tem o estabelecimento
def buscaSeJaTem(nome):
  print('[*] - DEBUG Funcao- buscaSeJaTem')
  nome = nome.replace(' ', '')
  if nome in dir(nomes_estabelecimentos):
    return True
  else:
    return False


def listarArrayCheckBox(listaString):
  print('[*] - DEBUG Funcao- listarArrayCheckBox')
  # print(listaString)
  if type(listaString) is str:
    listaString = listaString.replace("'", '"')
    listaString = json.loads(listaString)
    return listaString

# listaString = " ['ola', 'teste ei', '123', 'aaa'] "
# listaString = " ['Banheiro Familiar', 'Monitor infantil', ''] "
# dicInfra = {'Banheiro familiar': 0, 'Fraldário': 0, 'Espaço kids': 0, 'Monitor infantil': 0, 'Microondas': 0}
# [GAMBIARRA] Trata a string cadastrada no 'banco de dados' para dicionario
def tratarArrayCheckboxInfra(listaString):
  print('[*] - DEBUG Funcao- tratarArrayCheckboxInfra')
  dicInfra = {'Banheiro familiar': 0, 'Fraldário': 0, 'Espaço kids': 0, 'Monitor infantil': 0, 'Microondas': 0}
  # print(type(listaString))
  if type(listaString) is str:
    listaString = listaString.replace("'", '"')
    listaString = json.loads(listaString)
  for i in listaString:
    if i == '':
      listaString.remove('')
    if i in dicInfra:
      dicInfra[i] = 1
    else:
      dicInfra[i] =  0
  # print(dicInfra)
  return dicInfra

# [GAMBIARRA] Trata a string cadastrada no 'banco de dados' para dicionario
def tratarArrayCheckboxAdici(listaString):
  print('[*] - DEBUG Funcao- tratarArrayCheckboxAdici')
  dicAdici = {'Acessibilidade': 0, 'Estacionamento coberto': 0, 'Elevador': 0}
  # print(listaString)
  if type(listaString) is str:
    listaString = listaString.replace("'", '"')
    listaString = json.loads(listaString)
  for i in listaString:
    if i == '':
      listaString.remove('')
    if i in dicAdici:
      dicAdici[i] = 1
    else:
      dicAdici[i] =  0
  # print(dicAdici)
  return dicAdici

# [GAMBIARRA] Atribui a lista String para dicionario ao reqform
def chamaReqFormComListaCheckbox(reqform):
  print('[*] - DEBUG Funcao- chamaReqFormComListaCheckbox')
  reqform['infraestrutura'] = tratarArrayCheckboxInfra(reqform['infraestrutura'])
  # print(reqform['infraestrutura'])
  reqform['adicionais'] = tratarArrayCheckboxAdici(reqform['adicionais'])
  return reqform

# tratarArrayCheckbox(listaString)


