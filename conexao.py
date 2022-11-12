 import sqlite3
from sqlite3 import Error

def conectar():
  try:
    global conn, c
    conn = sqlite3.connect("banco.db")
    c = conn.cursor()
    c.execute("""create table if not exists 'usuario'(id integer primary key autoincrement not null,
    nome text,
    sobrenome text,
    nascimento date,
    email text,
    senha text)""")
    c.execute ("""create table if not exists 'agendamento'(cod_agen id integer primary key not null,
    data_agen date)""")
    c.execute("""create table if not exists 'calendario'(cod_calen id integer primary key not null,
    dia_calen text,
    mes_calen text,
    ano_calen text,
    horario_calen text)""")
  except Error as e:
    print ('Não foi possivel devido a:', e)

conectar()

def vertab():
  result = c.fetchall()
  for i in result:
    print (i, sepp = ',')

def executar(vrv):
  c.execute(vrv)