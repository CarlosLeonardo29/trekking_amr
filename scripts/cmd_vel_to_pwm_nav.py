import board
import busio
from adafruit_pca9685 import PCA9685
import time

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)

# Ajuste da Frequência do Cristal
pca.reference_clock_speed = round(25000000 * (112 / 100)) 
print(pca.reference_clock_speed)

pca.frequency = 100
time.sleep(0.1)

def cmdvel_to_pwm(v, w, v_max=1.0, w_max=1.0, v_deadband=0.0):
    """
    Converte linear.x (v) e angular.z (w) em duty cycle para motor e servo.
    """
    # --- Motor ---
    if abs(v) < v_deadband:
        v = 0.0
    # pwm_motor = 0.15 + (v / v_max) * 0.05
    pwm_motor = 0.15 + (v / v_max) * 10
    pwm_motor = max(0.15, min(0.15505, pwm_motor))  # limita

    # --- Servo ---
    pwm_servo = 0.16 + (w / w_max) * 0.05
    pwm_servo = max(0.05, min(0.25, pwm_servo))  # limita

    # Converte para escala PCA9685
    duty_motor = int(65535 * pwm_motor)
    duty_servo = int(65535 * pwm_servo)

    return duty_motor, duty_servo

class CmdVelListener(Node):
    def __init__(self):
        super().__init__('cmdvel_listener')

        # cria subscriber para o tópico /cmd_vel
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg: Twist):
        self.v = msg.linear.x
        self.w = msg.angular.z
        
        print(f"linear.x = {self.v:.2f}, angular.z = {self.w:.2f}")
        duty_motor, duty_servo = cmdvel_to_pwm(self.v, -self.w, v_max=1.0, w_max=1.0)

        pca.channels[0].duty_cycle = duty_motor

        pca.channels[1].duty_cycle = duty_servo

        print("Motor:", duty_motor, "Servo:", duty_servo)

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelListener()
    rclpy.spin(node)          
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
