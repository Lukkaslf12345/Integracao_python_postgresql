import psycopg2
from pyquery.query import *
from pyquery.connection import *

Connection = TConnection(user = "postgres", 
                                  password = "senha_banco_dados",
                                  host = "ip_banco_dados",
                                  port = "porta_banco_dados",
                                  database = "base_banco_dados")                                  
Q1 = TQuery()
Q1.connection = Connection

input_login = str(input('[E]ntrar  [S]air: '))

if input_login == 'E':
    senha_digitada = str(input('Digite sua senha: '))
    Q1.sql.text = 'select senha from senha'
    Q1.Open()
    senha_permitida = Q1.FieldByName('senha').AsString
    
    if senha_digitada == senha_permitida:
        print('Você entrou no sistema!')
    else:
        print('A senha está errada!')
else:
    print('Você saiu do sistema!')

#Demonstração simples para armazenar senhas no banco de dados e valida-las no python.
