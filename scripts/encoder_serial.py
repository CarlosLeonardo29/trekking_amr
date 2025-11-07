import serial
import time
import math

# === CONFIGURAÇÃO DA SERIAL ===
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)
print("🔌 Conectado à serial:", ser.port)

pulsos = 0

try:
    while True:
        line = ser.readline().decode(errors='ignore').strip()
        if line == '1':  # cada '1' indica uma borda de subida
            pulsos += 1
            print(f"🛞 Pulsos: {pulsos:5d}")
            pulsos = 0

except KeyboardInterrupt:
    print("\nEncerrando leitura serial...")
finally:
    ser.close()
