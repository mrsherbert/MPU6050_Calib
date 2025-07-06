#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

// Guardar as variaveis recebidas aceleração e giro
int16_t ax, ay, az, gx, gy, gz;

// Valores coeficientes angulares da calibração do MPU6050
float alf_ax = 0.9235, alf_ay = 0.9578, alf_az = 1.0046; // coeficiente angular

// Ofssets de calibração ax, ay, az e gz
float ax_offset = 0.0478, ay_offset = 0.0457, az_offset = 0.0389; // coeficiente linear

// Angulos de rolagem, ancoragem e ginagem
float pitch = 0.0, roll = 0.0, yaw = 0.0;

// Variveis de tempo
unsigned long lastTime;
float dt;

void setup() {
  // Conexão serial e MPU6060
  Wire.begin();
  Serial.begin(9600);
  mpu.initialize();

  // Verifica status de conexão MPU6050
  if (!mpu.testConnection()) {
    Serial.println("Problema de comunicação com MPU6050");
    while (1);
  }

  // Guarda o ultimo tempo registrado
  lastTime = millis();
}

void loop() {
  // Valores recebidos do sensor MPU6050
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  // Converte valores pelo fundo de escala e calibrar
  float ax_g = (ax / 16384.0) * alf_ax + ax_offset;
  float ay_g = (ay / 16384.0) * alf_ay + ay_offset;
  float az_g = (az / 16384.0) * alf_az + az_offset;
  float gz_g = gz / 131;

  // Variação de tempo
  unsigned long now = millis();
  float dt = (now - lastTime) / 1000.0;
  lastTime = now;

  // Calcular ângulos a partir do acelerômetro (em graus)
  roll = atan2( ay_g, sqrt(ax_g * ax_g + az_g * az_g)) * 180 / PI;
  pitch = atan2( -ax_g, sqrt(ay_g * ay_g + az_g * az_g)) * 180 / PI;
  //yaw = yaw + alf_yaw * gz_g * dt;

/*
  // Receber valores de aceleração para
  // Exibir Ax, Ay e Az calibrados e Gz
  Serial.print("Ax: ");
  Serial.print(ax_g, 2);
  Serial.print(" | Ay: ");
  Serial.print(ay_g, 2);
  Serial.print(" | Az: ");
  Serial.println(az_g, 2);
  //Serial.print(" | gz: ");
  //Serial.println(gz_g, 2);

  // Exibir dados
  Serial.print("Roll:");
  Serial.print(roll);
  Serial.print(",");
  Serial.print("Pitch:");
  Serial.println(pitch);
*/
  Serial.print("Ax: ");
  Serial.print(ax_g, 2);
  Serial.print(" | Ay: ");
  Serial.print(ay_g, 2);
  Serial.print(" | Az: ");
  Serial.println(az_g, 2);

  delay(20);
}

