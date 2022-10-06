import random
import time

class usuario:
  def __init__(self):
    self.nome = None
    self.nasc = None
    self.email = None
    self.__senha = None
    self.numero = None
    
  def cadastrar(self):
    print('')
    print('\033[1;41mCADASTRO\033[m')
    print('')
    self.nome = input('Insira seu nome: ')
    time.sleep(0.5)
    self.nasc = input('Insira sua data de nascimento: ')
    time.sleep(0.5)   
    self.email = input('Digite seu email: ')
    time.sleep(0.5)
    self.numero = int(input('Digite seu número de telefone: '))
    time.sleep(0.5)
    self.__senha = input('Crie uma senha: ')
    print('Você efetuou seu cadastro!\n')

  def login(self):
    print('')
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
    edit = input('Deseja editar as informações conta?: ')
    if edit=='nao':
      pass
    elif edit=='sim':
      q = input('O que gostaria de alterar?: ')
      if q=='email': 
         self.email = input('Insira seu novo email: ')
      elif q=='senha':
        self.__senha = input('Insira sua nova senha: ')
      elif q=='telefone':
        self.numero = int(input('Digite seu novo número de telefone: '))
      else:
        self.nasc = input('Insira sua data de nascimento:')
        
  def realizarLogout(self):
    out = input('Deseja realizar Logout?: ')
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