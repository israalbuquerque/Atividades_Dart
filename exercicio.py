import os
from dotenv import load_dotenv

load_dotenv()
senha = os.getenv("senha")

senha_digitada = input("Digite sua senha: ")

if senha_digitada == senha:
    print("Senha correta!")
else:
    print('Senha incorreta!!')

# print('Olá, meu nome é israel!')
# print('Teste para tentar subir, sem estar errado.')
# print('essa alteracao para erro')
# print('Corricao de erro')
# print('Novo commit erro')




# usar o env e gitegnore

#caso uma senyha seja enviada pelo git o que devo fazer
#

