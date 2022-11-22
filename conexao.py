from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import customtkinter as ctk
from tkcalendar import Calendar, DateEntry
import sqlite3
from sqlite3 import Error
import os

#Método de conectar ao banco de dados
def conectar():
  global conn, c
  conn = sqlite3.connect("banco.db")
  c = conn.cursor()

#método para fechar conexão
def endconect():
  conn.commit()
  conn.close()

#tabela usuario
def tabuser():
  c.execute("""create table if not exists 'usuario'(id_usuario integer primary key not null,
  nome TEXT not null,
  nascimento date,
  email TEXT not null unique,
  senha TEXT not null)""")

#tabela agendamento
def tabagend():
  c.execute ("""create table if not exists 'agendamento'(cod_agen integer primary key not null,
  data_agen text,
  id_user int,
  cod_comp int,
  foreign key (id_user) references usuario(id_usuario),
  foreign key (cod_comp) references compromisso(cod_compromisso))""")

#tabela compromisso
def tabcomp():
  c.execute ("""create table if not exists 'compromisso'(cod_compromisso id integer primary key not null,
  nome text not null,
  local text,
  horario time,
  descricao text,
  dia int,
  mes int)""")

#tabela metas
def tabmeta():
  c.execute ("""create table if not exists 'metas'(cod_metas id integer primary key not null,
  nome_metas text,
  objetivos text,
  limite_meta date,
  cod_comp int,
  foreign key (cod_comp) references compromisso(cod_compromisso))""")

#tabela atividades
def tabatv():
  c.execute ("""create table if not exists 'atividade'(cod_atividades id integer primary key not null,
  nome_atividade text,
  tipo_atividade text,
  prazo_atividade date,
  cod_comp int,
  foreign key (cod_comp) references compromisso(cod_compromisso))""")

#tabela calendario
def tabcalen():
  c.execute("""create table if not exists 'calendario'(cod_calen id integer primary key not null,
  dia_calen int,
  mes_calen int,
  ano_calen int,
  horario_calen time,
  cod_agen int,
  cod_comp int,
  id_user int,
  foreign key (cod_agen) references agendamento(cod_agen),
  foreign key (cod_comp) references compromisso(cod_compromisso),
  foreign key (id_user) references usuario(id_usuario))""")

def conectarFK():
  try:
    c.execute()
  except:
    pass

def vertab():
  result = c.fetchall()
  for i in result:
    print (i, sep = ',')

def criarusuario():
  try:
    res = c.execute("select email from usuario where email = (?)", (email.get(),))
    if res.fetchone():
      custompop('Esse email já está sendo usado')
    else:
      c.execute("""INSERT INTO usuario (nome, nascimento, email, senha) VALUES (?,?,?,?);""", (str(nome.get()), str(datanscm.get()), str(email.get()), str(senha.get())))
    res.fetchall()
    print (res)
  except Error as e:
    print (e)

def autenticaremail():
  res = c.execute("select email from usuario where email = (?)", (email.get(),))
  if res.fetchone():
    print('email existe')
  else:
    custompop('Esse email não está cadastrado, por favor insira um email válido.')    

def autenticarsenha():
  res = c.execute("select email from usuario where senha = (?)", (senha.get(),))
  if res.fetchone():
    print('senha existe, parabens')
  else:
    custompop('Senha incorreta, tente novamente.')

def deletaruser():
  res = c.execute("delete from usuario where email = (?)", (email.get(),))