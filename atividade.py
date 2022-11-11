import datetime
from Compromisso import *
class atividade(Compromisso):
  
  def __init__(self):
    self.nome = None
    self.tipo = 'Atividade'
    self.prazo = None

  def ativTipo(self):
    print('Seu compromisso foi classificado como uma atividade.')
  
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
    self.tipo = 'metas'
    self.limite_meta = None
    self.duracao_meta = None

  def metaTipo(self):
    print('Seu compromisso foi classificado como uma meta.')

  def progressoMetas(self):
    self.objetivo_meta = int(input('Digite (em %) o progresso da sua meta:'))

  def duracaoMetas(self):
    duracao = int(input('Digite de quantos dias será a duração da sua meta:'))
    print(f'A duração da sua meta é: {duracao} dias')
    