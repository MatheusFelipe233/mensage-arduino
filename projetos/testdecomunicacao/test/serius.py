import os
import serial

 # Abre a porta serial
ser = serial.Serial('COM4', 9600)  # Substitua 'COMx' pelo nome da porta do Arduino

while True:
    data = ser.readline().decode().strip()
    if data == "alerta":
        # Navegue até o diretório onde o programa está localizado
        programa_dir = "/Users/anjos/projetos/mensage-arduino/projetos/testdecomunicacao/test/serius.py"
        os.chdir(programa_dir)
        
        # Execute o programa
        os.system("python comunic.py")