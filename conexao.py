import sqlite3
from sqlite3 import Error

def conectar():
  try:
    global conn, c
    conn = sqlite3.connect("banco.db", timeout = 10)
    c = conn.cursor()
    c.execute("""create table if not exists 'usuario'(id_user integer primary key autoincrement not null,
    nome text,
    tel_usuario text,
    nascimento date,
    email text,
    senha text)""")
    
    c.execute ("""create table if not exists 'agendamento'(cod_agen integer primary key autoincrement not null,
    data_agen text)""")
    
    c.execute ("""create table if not exists 'compromisso'(cod_compromisso integer primary key autoincrement not null,
    nome text,
    local text,
    horario time,
    descricao text,
    dia int,
    mes int)""")
    
    c.execute ("""create table if not exists 'metas'(cod_metas integer primary key autoincrement not null,
    nome_metas text,
    objetivos text,
    limite_meta date)""")
    
    c.execute ("""create table if not exists 'atividade'(cod_atividades id integer primary key not null,
    nome_atividade text,
    tipo_atividade text,
    prazo_atividade date)""")
    
    c.execute("""create table if not exists 'calendario'(cod_calen id integer primary key not null,
    dia_calen int,
    mes_calen int,
    ano_calen int,
    horario_calen time)""")
    
  except Error as e:
    print ('Não foi possivel devido a:', e)
    
conectar()

def vertab():
  result = c.fetchall()
  for i in result:
    print (i, sepp = ',')
    