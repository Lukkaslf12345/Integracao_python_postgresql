import psycopg2
from pyquery.query import *
from pyquery.connection import *
from cryptography.fernet import Fernet

chave_secreta = Fernet.generate_key()
fernet = Fernet(chave_secreta)

def criptografar(senha):
    return fernet.encrypt(senha.encode()).decode()

def descriptografar(senha_criptografada):
    return fernet.decrypt(senha_criptografada.encode()).decode()
    
Connection = TConnection(user = "postgres", 
                                  password = "4devF0r!@bos#3000",
                                  host = "172.25.100.9",
                                  port = "5432",
                                  database = "bd_teste_nivelamento")                                  
Q1 = TQuery()
Q1.connection = Connection

Q2 = TQuery()
Q2.connection = Connection

login = input('Digite 1 para entrar e 2 para sair ')
codigo_usuario = 1

if login == '1':
    print('Você entrou no sistema!\n')
    resposta_nome = str(input(
    f'Agora precisamos de alguns dados pessoais.\n'
    f'Digite seu nome: '
    ))

    resposta_idade = str(input(
    f'Digite sua idade: '
    ))
  
    resposta_email = str(input(
    f'Digite seu e-mail: '
    ))

    resposta_senha = str(input(
     f'Agora crie uma senha. Se certifique que ela seja segura: '   
    ))

    print(f'\nBem vindo ao sistema {resposta_nome}. Preciso que você faça o login para autenticar a senha.'
    )
      
    entrada_email = str(input
    (f'Digite seu e-mail: '
     ))
     
    entrada_senha = str(input
    (f'Digite sua senha: '
     ))
    
    Q1.sql.text = f'select * from senha where codigo = {codigo_usuario}'  
    Q1.Open()
    senha_permitida = Q1.FieldByName('senha').AsString
    email_permitido = Q1.FieldByName('email').AsString
        
    if entrada_email == email_permitido and senha_permitida ==  entrada_senha:
        print(f'Você autenticou seu usuário!'
           )
    else:
        print('Seu usuário ou senha estão incorretos! Verifique!')   

else:
    print(f'Você saiu do sistema!'
    )
