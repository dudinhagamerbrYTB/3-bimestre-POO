import os
import time

def linhas():
  print('-'*30)

def limpar():
  return os.system('cls' if os.name == 'nt' else 'clear')

def ponto():
  print('.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)

def menuCL():
  print()
  print(' -- << \033[1;34mMENU\033[m >> --')
  print('|  [\033[1;36m1\033[m]\033[1;34m CADASTRO\033[m  |')
  print('|  [\033[1;36m2\033[m]\033[1;34m LOGIN\033[m     |')
  print('|  [\033[1;36m0\033[m]\033[1;34m SAIR\033[m      |')
  print('________________')

def menuER():
  limpar()
  print()
  print('    -- << \033[1;34mMENU\033[m >> --')
  print('|  [\033[1;36m1\033[m]\033[1;34m PERFILl\033[m         |')
  print('|  [\033[1;36m2\033[m]\033[1;34m AGENDAMENTO\033[m     |')
  print('|  [\033[1;36m0\033[m]\033[1;34m SAIR\033[m            |')
  print('________________')

def menuELL():
  limpar()
  print()
  print('    -- << \033[1;34mMENU\033[m >> --')
  print('|  [\033[1;36m1\033[m]\033[1;34m EDITAR PERFILl\033[m  |')
  print('|  [\033[1;36m2\033[m]\033[1;34m CONTATOS\033[m        |')
  print('|  [\033[1;36m3\033[m]\033[1;34m VOLTAR\033[m          |')
  print('|  [\033[1;36m0\033[m]\033[1;34m SAIR\033[m            |')

