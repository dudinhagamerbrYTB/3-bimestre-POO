import time

def Nome():
  while True:
    nome = input('Nome completo: ')
    print()
    if nome == '':
      print('\033[1;31mErro! Entrada vazia.\033[m')
      time.sleep(1)
      continue
    temp = ''.join(nome.split('  '))
    for i in temp:
      if i.isdigit():
        print('Digite um nome válido:')
        break
    else:
      return nome

def Data():
  while True:
    data = input('Data de nascimento: ')
    print()
    if data=='':
      break
    temp = ''.join(data.split('/'))
    if not temp.isnumeric():
      print('Insira uma data válida')
      continue 
    elif data.count('/') == 2 and data != '//':
      dia, mes, ano = data.split('/')
      if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2022:
        return data
      else:
        print('Data inválida')
    else:
      print('A data deve seguir o padrão dd/mm/aaaa')

def Email():
  while True:
    email = input('Email: ')
    print()
    if email == '':
      print('\033[1;31mErro! Entrada vazia.\033[m')
      time.sleep(1)
    elif '@' and '.com' in email:
      return email
    else:
      print('Email inválido!')

def Tel():
  while True:
    tel = input('Telefone: ')
    print()
    if tel=='':
      break
    elif not tel.isnumeric():
      print('Letras e caracteres especiais não são permitidos.')
      continue
    else:
      if 9 <= len(tel) <= 11:
        return tel
      else:
        print('Apenas 9-11 caracteres.')      

def Senha():
  while True:
    senha = input('Senha: ')
    print()
    if senha == '':
      print('\033[1;31mErro! Entrada vazia.\033[m')
      time.sleep(1)
      continue
    else:
      return senha