import os
import serial
import subprocess

 # Abre a porta serial
ser = serial.Serial('COM4', 9600)  # Substitua 'COMx' pelo nome da porta do Arduino

while True:
    data = ser.readline().decode().strip()
    if data == "alerta":
        # Navegue até o diretório onde o programa está localizado
        programa_dir = r'C:\Users\anjos\projetos\mensage-arduino\projetos\testdecomunicacao\test\comunic.py'
        os.system('python ' + programa_dir)
        
        # Execute o programa
        os.system("python comunic.py")