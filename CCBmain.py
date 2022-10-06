file = open('comp.txt', 'w+')
import random
import time
import datetime
import calendar
import os
compro = []
contatos = {}

class usuario:
  def __init__(self):
    self.nome = None
    self.nasc = None
    self.email = None
    self.__senha = None
    self.numero = None
    
  def cadastrar(self):
    print('\033[1;41mCADASTRO\033[m')
    print('')
    self.nome = input('Insira seu nome: ')
    time.sleep(0.5)
    self.nasc = input('Insira sua data de nascimento:')
    time.sleep(0.5)   
    self.email = input('Digite seu email: ')
    time.sleep(0.5)
    self.numero = int(input('Digite seu número de telefone: '))
    time.sleep(0.5)
    self.__senha = input('Crie uma senha: ')
    print('Você efetuou seu cadastro!\n')

  def login(self):
    print('\033[1;44mLOGIN\033[m')
    print('')
    e = input('Insira seu email: ')
    while e!=self.email:
      e = input('Email inválido, tente novamente: ')
    if e==self.email:
      print('')
    s = input('Insira sua senha: ')
    if s!=self.__senha:
      if s==self.__senha:
        print('')
      for i in range(4):
        s = input('Senha inválida, tente novamente: ')
        if s==self.__senha:
          print('A senha inserida está correta. ')
          print('')
          break
        if i==3:
          print('A senha foi inserida incorretamente muitas vezes, enviamos um código de verificação para seu número de telefone')
          cod = random.randint(10000, 50000)
          print(cod)
          c = int(input('Digite o código enviado ao seu número de telefone: '))
          if c!=cod:
            print('O código inserido é inválido, a conta não poderá ser acessada.')
          elif c==cod:
            s2 = input('Deseja alterar sua senha? ')
            if s2=='sim':
              self.__senha = input('Insira sua nova senha: ')
              print('Senha atualizada')
            elif s2=='nao':
              print('Impossível acesso à conta')
    elif s==self.__senha:
      print('')
  
  def editarConta(self):
    edit = input('Deseja editar as informações conta?:')
    if edit=='nao':
      pass
    elif edit=='sim':
      q = input('O que gostaria de alterar?:')
      if q=='email': 
         self.email = input('Insira seu novo email:')
      elif q=='senha':
        self.__senha = input('Insira sua nova senha:')
      elif q=='telefone':
        self.numero = int(input('Digite seu novo número de telefone: '))
      else:
        self.nasc = input('Insira sua data de nascimento:')
        
  def realizarLogout(self):
    out = input('Deseja realizar Logout?:')
    if out=='sim':
      print('')
    elif out=='nao':
      pass

  def visualizarPerfil(self):
    print('')
    exibirInfo = input('Deseja visualizar seu perfil? ')
    if exibirInfo == 'sim':
      print('Nome:', self.nome)
      print('E-mail atual:', self.email)
      print('Número cadastrado:', self.numero)
      mostrar_senha = input('Deseja visualizar sua senha? ')
      if mostrar_senha == 'sim':
        cod1 = random.randint(10000, 50000)
        print(cod1)
        cod_mostrarSenha = int(input('Insira o código enviado ao seu e-mail. '))
        if cod_mostrarSenha!=cod1:
          print('O código inserido é inválido. A senha não pode ser visualizada.')
        elif cod_mostrarSenha==cod1:
          print('Senha:', self.__senha)
      if mostrar_senha == 'nao':
        print('Informações necessárias já visualizadas.')
        print('')

  def listarContatos(self):
    add = input('Deseja adicionar alguma contato?:')
    if add=='nao':
      pass
    elif add=='sim':
      ncont = input('Insira o nome do contato:')
      numcont = input('Insira o número do contato:')
      contatos = {ncont: numcont}
      print(contatos)
    

class agendamento:
  def __init__(self):
    self.momento = None

  def criarAgen(self):
    print('\033[1;41mCADASTRO DE EVENTO\033[m')
    c = input('Deseja agendar um evento?:',)
    print()
    if c=='nao':
      pass
    elif c=='sim':
      self.momento = datetime.datetime.now()
      print('Momento do agendamento:', self.momento)



class Compromisso:
  
  def __init__(self):
    self.nome = None
    self.local = None
    self.dia = None
    self.mes = None
    self.horario = None
    self.desc = None

  def criarCompromisso(self):
    self.nome =  input('Título:')
    self.desc = input('Descrição:')
    self.local = input('Localização:')
    self.dia = int(input('Insira o dia do compromisso:'))
    self.mes = input('Insira o mês do compromisso:')
    self.ano = int(input('Insira o ano do compromisso:'))
    print(self.nome, '\n', self.local, '\n', self.desc, '\n', self.dia, self.mes, self.ano )
    file.write(f'Dia {self.dia} de {self.mes}: {self.nome} {calendar.calendar(2022)}')

    
  def editarCompromisso(self):
    edit1 = input('Deseja editar as informações conta?:')
    if edit1=='nao':
      pass
    elif edit1=='sim':
      q1 = input('O que gostaria de alterar?:')
      if q1=='titulo':
        self.nome =  input('Título:')
      elif q1=='descricao':
        self.desc =  input('Descrição:')
      elif q1=='local':
        self.local =  input('Local:')
      elif q1=='dia':
        self.dia =  input('Dia:')
      elif q1=='mes':
        self.mes =  input('Mês:')
      elif q1=='ano':
        self.ano =  input('Ano:')

  def salvarCompromisso(self):
    print('', self.nome, '\n', self.local, '\n', self.desc, '\n', self.dia, 'de', self.mes, 'de', self.ano )
    save = input('Deseja salvar?:')
    if save=='nao':
      comp = Compromisso()
      comp.editarCompromisso()
    elif save=='sim':
      compro = []
      compro.insert(0, self.nome)
      print(compro, 'salva')

  def cancelarCompromisso(self):
    cancel = input('Deseja excluir algum compromisso?:')
    if cancel=='nao':
      pass
    elif cancel=='sim':
      n = input('Digite o nome do compromisso que deseja excluir:')
      compro.pop(n)

  def padronizarCompromisso(self):
    pad = input('Deseja padronizar o compromisso?:')
    if pad=='nao':
      pass
    elif pad=='sim':
      tpad = input('Insira a padronização [dia, mês, ano]:')
      if tpad=='dia':
        self.dia = 'Todos os dias'
      elif tpad=='mes':
        self.mes = 'Todos os meses'
      elif tpad=='ano':
        self.ano = 'Todo os anos'

class atividade(Compromisso):
  
  def __init__(self):
    self.nome = None
    self.prazo = None

  def calcularPrazo(self):
    dia = datetime.date.now()
    calculo = dia - self.dia
    print('Você tem:', calculo, 'dias para concluir a atividade')

  def notificarPrazo(self, calculo):
    if calculo==1:
      print('Você tem apenas um dia para concluir sua atividade')
  
class metas(Compromisso):
  def __init__(self):
    self.nome_metas = None
    self.objetivo_meta = None
    self.limite_meta = None
    self.duracao_meta = None

  def progressoMetas(self):
    print('')

class calendario():
  def __init__(self):
    self.data = None

  def verifDispon(self):
    open = input('Deseja verificar seu calendário?:')
    if open=='sim':
      print(file)
    else:
      pass
      
  
def ponto():
  print('.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)

def CadLog():
  while True:
    CadLog = int(input('O que você deseja fazer?: \n 1. Cadastrar novo usuário \n 2. Login \n 3. Sair \n'))
    if CadLog==1:
      try:
        usu = usuario()
        usu.cadastrar()
        ponto()
        print('Atualizando dados...')
        ponto()
      except:
        print('Esse login não existe')
        pass
    elif CadLog==2:
        usu.login()
        ExAg = int(input('O que você deseja fazer?: \n 1. Exibir perfil \n 2. Realizar agendamento \n'))
        if ExAg==1:
          usu.visualizarPerfil()
          EdLcLo = int(input('O que você deseja fazer?: \n 1. Editar perfil \n 2. Listarcontatos \n 3. Logout'))
          if EdLcLo==1:
            usu.editarConta()
          elif EdLcLo==2:
            usu.listarContatos()
          elif EdLcLo==3:
            usu.realizarLogout()
        elif ExAg==2:
          agen = agendamento()
          agen.criarAgen()
          comp = Compromisso()
          comp.criarCompromisso()
          comp.salvarCompromisso()
          comp.padronizarCompromisso()
    elif CadLog==3:
      os.system('clear')
      break
        


CadLog()


