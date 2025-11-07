import time
import board
import busio
import adafruit_apds9960.apds9960

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_color = True

flag_waypoint = 0

while True:
    r, g, b, c = sensor.color_data
    
    if r + g + b >= 20000:
        flag_waypoint = 1
        print("Waypoint Detectado")
    else:
        flag_waypoint = 0
        print("Waypoint não Detectado")

    print(f"R={r}, G={g}, B={b}, C={c}")
    time.sleep(0.5)
