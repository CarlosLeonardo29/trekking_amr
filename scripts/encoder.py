#!/usr/bin/env python3
import Jetson.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BOARD)

pin = 29
GPIO.setup(pin, GPIO.IN)

print("Lendo pino 29 (pressione Ctrl+C para sair)")

bordas_subida = 0
voltas = 0
estado_anterior = GPIO.input(pin)

try:
    while True:
        estado_atual = GPIO.input(pin)

        if estado_anterior == GPIO.LOW and estado_atual == GPIO.HIGH:
            bordas_subida += 1
            print(f"🟢 Borda de subida detectada! Total: {bordas_subida}")

            if bordas_subida % 4 == 0:
                voltas += 1
                print(f"🔵 Volta {voltas} detectada!")

        estado_anterior = estado_atual
        #time.sleep(0.005)  

except KeyboardInterrupt:
    print("\nEncerrando leitura...")
finally:
    GPIO.cleanup()
    print(f"\nTotal de bordas de subida: {bordas_subida}")
    print(f"Total de voltas: {voltas}")

    diametro_cm = 13.0
    circunferencia_m = math.pi * (diametro_cm / 100.0)
    distancia_m = voltas * circunferencia_m
    print(f"Distância percorrida: {distancia_m:.3f} m")
