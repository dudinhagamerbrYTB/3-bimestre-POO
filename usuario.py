import random
import time

class Usuario:
  def __init__(self):
    self.nome = None
    self.nasc = None
    self.email = None
    self.__senha = None
    self.numero = None
    
  def cadastrar(self):
    print()
    print('\033[1;41mCADASTRO\033[m')
    print()
    linhas()
    
    self.nome = Nome()
    time.sleep(0.5)   
    self.email = Email()
    time.sleep(0.5)
    self.nasc = Data()
    time.sleep(0.5)
    self.numero = Tel()
    time.sleep(0.5)
    self.__senha = Senha()
    
    print('\033[1;40mVocê efetuou seu cadastro!\033[m\n')
    linhas()
    
    logins = open('logins.txt', 'w+')
    logins.write(f'{self.nome}-{self.email}-{self.__senha}-{self.nasc}- {self.numero}')
    logins.close()

  
  def login(self):
    while True:
      limpar()
      print('')
      print('\033[1;44mLOGIN\033[m')
      print('')      
      logar = open('logins.txt', 'r')
      for linha in logar.readlines():
        valor = linha.split('-')
        self.email = input('Insira seu email:')
        if self.email == '':
          print('\033[1;31mErro! Entrada vazia.\033[m')
          time.sleep(1)
        elif self.email == valor[1]:
          self.senha = input('Insira sua senha:')
          if self.senha =='':
            print('\033[1;31mErro! Entrada vazia.\033[m') 
            time.sleep(1)
          elif self.senha == valor[2]:
            print('\033[1;40mLogin efetuado!\033[m\n')
            global inlog
            inlog = True
            linhas()
            time.sleep(1)
            break
          else:
            print('Senha incorreta!')
            return
        else:
          print('Email não correspondente!')
          return
      break
      logar.close()
    
  def editarConta(self):
    while True:
      edit = input('Deseja editar as informações conta?: ')
      if edit=='nao':
        break
      elif edit=='sim':
        q = input('O que gostaria de alterar?: ')
        if q=='email': 
           self.email = Email()
        elif q=='nome':
          self.nome = Nome()
        elif q=='senha':
          self.__senha = Senha()
        elif q=='telefone':
          self.numero = Tel()
        elif q=='nascimento':
          self.nasc = Data()

  def realizarLogout(self):
    out = input('Deseja realizar Logout?: ')
    if out=='sim':
      limpar()
    elif out=='nao':
      pass

  def visualizarPerfil(self):
    print('\033[1;45mPERFIL DE USUÁRIO\033[m\n')
    infos = open('logins.txt', 'r')
    for linha in infos.readlines():
      infos = linha.split('-')
      print('Nome:', infos[0], '\nEmail:', infos[1], '\nData de nascimento:', infos[3], '\nTelefone:', infos[4], '\n')
    mostrar_senha = input('Deseja visualizar sua senha?: ')
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
    print('\033[1;45mCONTATOS\033[m\n')
    while True:
      add = input('Deseja adicionar alguma contato?:')
      if add=='nao':
        break
      elif add=='sim':
        ncont = input('Insira o nome do contato:')
        numcont = input('Insira o número do contato:')
        contatos.append(ncont, numcont)
        print(contatos)