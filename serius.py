import os
import serial
import subprocess

 # Abre a porta serial
ser = serial.Serial('COM4', 115200)  # Substitua 'COMx' pelo nome da porta do Arduino

while True:
    data = ser.readline().decode().strip()
    if data == "alerta":
        print('alerta')
        # Navegue até o diretório onde o programa está localizado
        #programa_dir = r'comunic.py'
        #os.system('python' + programa_dir)
        
        # Execute o programa
        os.system("python comunic.py")