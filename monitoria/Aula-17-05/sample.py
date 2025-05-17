import mysql.connector
from mysql.connector import Error

def conectar():
  try:
    return mysql.connector.connect(
      host='localhost',
      user='brunomgomes',
      password='Monitoria123@',
      database='game_db'
    )
  except Error as e:
    print(f'Erro ao se conectar {e}')
    return None

conn = conectar()

def inserir_personagem(conn):
  # Pedir as informações para o usuário
  nome = input('Qual nome do personagem: ')
  classe = input('Qual a classe: ')
  # Tratar os inputs 
  try:
    nivel = int(input('Qual o nível: '))
  except:
    print('O nível deve ser um número inteiro')
    return
  
  cursor = conn.cursor()
  cursor.execute('''INSERT INTO personagens(nome, classe, nivel) VALUES (%s, %s, %s)''',
                  (nome, classe, nivel)
                )
  conn.commit()

inserir_personagem(conn)