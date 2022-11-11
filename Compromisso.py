import calendar
compro = []

class Compromisso:
  
  def __init__(self):
    self.nome = None
    self.local = None
    self.dia = None
    self.mes = None
    self.horario = None
    self.desc = None

  def criarCompromisso(self):
    self.nome =  input('Título: ')
    print('')
    self.desc = input('Descrição: ')
    print('')
    self.local = input('Localização: ')
    print('')
    self.dia = int(input('Insira o dia do compromisso: '))
    print('')
    self.mes = input('Insira o mês do compromisso: ')
    print('')
    self.ano = int(input('Insira o ano do compromisso: '))
    print('')
    print(self.nome, '\n', self.local, '\n', self.desc, '\n', self.dia, self.mes, self.ano )
    file = open('comp.txt', 'w+')
    file.write(f'Dia {self.dia} de {self.mes}: {self.nome} {calendar.calendar(2022)}')

    
  def editarCompromisso(self):
    edit1 = input('Deseja editar as informações?: ')
    if edit1=='nao':
      pass
    elif edit1=='sim':
      q1 = input('O que gostaria de alterar?: ')
      if q1=='titulo':
        self.nome =  input('Título: ')
      elif q1=='descricao':
        self.desc =  input('Descrição: ')
      elif q1=='local':
        self.local =  input('Local: ')
      elif q1=='dia':
        self.dia =  input('Dia: ')
      elif q1=='mes':
        self.mes =  input('Mês: ')
      elif q1=='ano':
        self.ano =  input('Ano: ')

  def salvarCompromisso(self):
    print('', self.nome, '\n', self.local, '\n', self.desc, '\n', self.dia, 'de', self.mes, 'de', self.ano )
    save = input('Deseja salvar?: ')
    if save=='nao':
      comp = Compromisso()
      comp.editarCompromisso()
    elif save=='sim':
      compro = []
      compro.insert(0, self.nome)
      print(compro, 'salva')

  def cancelarCompromisso(self):
    cancel = input('Deseja excluir algum compromisso?: ')
    if cancel=='nao':
      pass
    elif cancel=='sim':
      n = input('Digite o nome do compromisso que deseja excluir: ')
      compro.pop(n)

  def padronizarCompromisso(self):
    pad = input('Deseja padronizar o compromisso?: ')
    if pad=='nao':
      pass
    elif pad=='sim':
      tpad = input('Insira a padronização [dia, mês, ano]: ')
      if tpad=='dia':
        self.dia = 'Todos os dias'
      elif tpad=='mes':
        self.mes = 'Todos os meses'
      elif tpad=='ano':
        self.ano = 'Todo os anos'