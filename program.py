import requests
import json
import time
import serial

# constante para limitar a quantidade de requisições a serem feitas
NUMERO_REQUISICOES = 3

# link do banco de dados realtime com firebase
link = "https://cardio-sensor-default-rtdb.firebaseio.com/"

# abrir a porta serial para comunicação com arduino
ser = serial.Serial('COM4', 9600)  

cont = 0
# while cont < NUMERO_REQUISICOES :
while True:
    frequencia = ser.readline().decode().strip() #frequencia lida no serial do arduino
    timestamp = f'{time.time()}'  ## para retirar o ponto flutuante

    print(f'frequencia lida: {frequencia}')
    
    if frequencia:
        # Criar uma estrutura do tipo cardio
        dados = {
            'frequencia' : f'{frequencia}',
            'timestamp' : timestamp
        }
        # faz uma requisição post para o firebase com o link e passando o dado do tipo cardio para o firebase persistir em núvem (guardar)
        requisicao = requests.post(f'{link}/cardio/.json', data=json.dumps(dados))

        print(f'REQUISICAO\n {requisicao}')

    time.sleep(2)
    cont += 1  

""" 
    referencias:
        Link documento REST API Firebase:
        https://firebase.google.com/docs/reference/rest/database

        código de referencia:
        https://www.hashtagtreinamentos.com/rest-api-do-firebase-no-python
"""