import datetime

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

