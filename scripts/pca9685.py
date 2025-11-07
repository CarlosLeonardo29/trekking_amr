import board
import busio
from adafruit_pca9685 import PCA9685
import time

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)

# Ajuste da Frequência do Cristal
pca.reference_clock_speed = round(25000000 * (112 / 100)) 
print(pca.reference_clock_speed)

pca.frequency = 100
time.sleep(0.1)

duty = int(65535 * 0.15)
pca.channels[0].duty_cycle = duty
