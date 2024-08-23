import psycopg2
from pyquery.query import *
from pyquery.connection import *

Connection = TConnection(user = "postgres", 
                                  password = "senha_banco_dados",
                                  host = "ip_banco_dados",
                                  port = "porta_banco_dados",
                                  database = "nome_banco_dados")                                  
Q1 = TQuery()
Q1.connection = Connection

input_login = str(input('[E]ntrar  [S]air: '))

if input_login == 'E':
    senha_digitada = str(input('Digite sua senha: '))
    Q1.sql.text = 'select senha from senhas'
    Q1.Open()
    senha_permitida = Q1.FieldByName('senha').AsString
    
    if senha_digitada == senha_permitida:
        print('Você entrou no sistema!')
    else:
        print('A senha está errada!')
else:
    print('Você saiu do sistema!')

#O código foi feito em python integrado ao postgresql. É uma função simples que valida se a senha que o usuário digitou para entrar no sistema, é a senha correta.
#A senha correta por sua vez fica armazenada no banco de dados, por meio do select.
