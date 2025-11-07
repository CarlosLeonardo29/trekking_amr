#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

saidas_pwm = {
    'JETSON_ORIN_NANO': [15, 32, 33],
}

output_pins = saidas_pwm.get(GPIO.model, None)

if output_pins is None:
    raise Exception('PWM not supported')

output_pin = output_pins[0]

def main():
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    saida_pwm = GPIO.PWM(output_pin, 100)
    duty = 15
    saida_pwm.start(duty)

    print("PWM running. Press CTRL+C to exit.")
    try:
        while True:
            time.sleep(0.5)
            
            duty = duty + 0.1

            if duty >= 20:
                duty = 15

            print(duty)

            saida_pwm.ChangeDutyCycle(duty)
    finally:
        saida_pwm.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
