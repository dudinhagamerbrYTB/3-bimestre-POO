#Projeto integrador
#Grupo: Noragami
#Alunas: Maria Eduarda G. Dias, Elizabeth Vitória, Ana Souza Gibson

from agendamento import *
from atividade import *
from Compromisso import *
from calendario import *
from usuario import *
import random
import time
import datetime
import calendar
import os

file = open('comp.txt', 'w+')

compro = []
contatos = {}


def ponto():
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)


def CadLog():
    while True:
        print('\033[1;41mO QUE VOCÊ DESEJA FAZER?\033[m')
        CadLog = int(
            input(
                '\n 1. Cadastrar novo usuário \n 2. Login \n 3. Sair \nInsira: '
            ))
        if CadLog == 1:
            try:
                usu = usuario()
                usu.cadastrar()
                ponto()
                print('Atualizando dados...')
                ponto()
            except:
                pass
        elif CadLog == 2:
            usu.login()
            ExAg = int(
                input(
                    'O que você deseja fazer?: \n 1. Exibir perfil \n 2. Realizar agendamento \n'
                ))
            if ExAg == 1:
                usu.visualizarPerfil()
                EdLcLo = int(
                    input(
                        'O que você deseja fazer?: \n 1. Editar perfil \n 2. Listarcontatos \n 3. Logout'
                    ))
                if EdLcLo == 1:
                    usu.editarConta()
                elif EdLcLo == 2:
                    usu.listarContatos()
                elif EdLcLo == 3:
                    usu.realizarLogout()
            elif ExAg == 2:
                agen = agendamento()
                agen.criarAgen()
                comp = Compromisso()
                comp.criarCompromisso()
                comp.salvarCompromisso()
                comp.padronizarCompromisso()
                AM = input(
                    'Gostaria de classificar o seu compromoisso como atividade ou meta?:'
                )
                if AM == 'atividade':
                    ativ = atividade()
                    ativ.ativTipo()
                elif AM == 'meta':
                    meta = metas()
                    meta.metaTipo()
                else:
                    pass
        elif CadLog == 3:
            os.system('clear')
            break


CadLog()
