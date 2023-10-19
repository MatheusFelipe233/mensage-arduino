/*
 * Programa de teste de Display LCD 16 x 2Prof.
 * Matheus Felipe CDFA
 *10/07/2023
 */

#include <LiquidCrystal.h>

//Define os pinos que serão utilizados para ligação ao display
LiquidCrystal lcd(13, 12, 5, 4, 3, 2);
int alerta=0;

void setup() {
  Serial.begin(9600);  //Define a velocidade de comunicaçao seria em 115200bauds
  pinMode(10, INPUT);    // Configuração para detecção de derivações LO +
  pinMode(11, INPUT);    // Configuração para detecção de  leads off LO -

  //Define os parâmetros do LCD
  lcd.begin(16, 2);  // Define Colunas e Linhas
  lcd.clear();       // Limpa a tela do display
}
void loop() {

  if ((digitalRead(10) == 1) || (digitalRead(11) == 1)) {
    Serial.println('!');
  } else {
    // envia o valor da entrada analógica 0:
    Serial.println(analogRead(A0));
  }
  // Leitura de sensores ou execução de ações
  // Quando algo específico acontecer, envie um sinal
 
  alerta = analogRead(A0);
  Serial.print("batimento :");
  Serial.println(alerta);
 
  if (alerta>220) 
  {
    Serial.print("alerta :");
    Serial.println(alerta);

  }

  // Programa do display LCD 16x2
  lcd.setCursor(0, 0);            //Posiciona o cursor na Coluna 0 e Linha 0
  lcd.print("Eletrocardiogram");  // Mostra o texto escrito entre aspas
  lcd.setCursor(0, 1);            //Posiciona o cursor na Coluna 0 e Linha 1
  lcd.println(analogRead(A0));

  // Espere um pouco para evitar que os dados seriais saturem
  delay(2500);
}
