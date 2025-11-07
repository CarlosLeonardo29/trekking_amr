import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import time
import board
import busio

from adafruit_bno08x import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_GAME_ROTATION_VECTOR,
)
from adafruit_bno08x.i2c import BNO08X_I2C

class BNO085Node(Node):
    def __init__(self):
        super().__init__('bno085_node')

        self.imu_pub = self.create_publisher(Imu, 'imu/data', 10)
        self.timer = self.create_timer(0.1, self.publish_imu_data)  

        self.init_sensor()

    def init_sensor(self):
        try:
            i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
            self.bno = BNO08X_I2C(i2c)
            self.bno.enable_feature(BNO_REPORT_ACCELEROMETER)
            self.bno.enable_feature(BNO_REPORT_GYROSCOPE)
            self.bno.enable_feature(BNO_REPORT_GAME_ROTATION_VECTOR)
            self.get_logger().info('BNO085 inicializado com sucesso.')
        except Exception as e:
            self.get_logger().error(f'Erro ao inicializar o BNO085: {e}')

    def publish_imu_data(self):
        try:
            msg = Imu()
            
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'imu_link'

            # Dados do acelerômetro (m/s^2)
            ax, ay, az = self.bno.acceleration
            msg.linear_acceleration.x = ax
            msg.linear_acceleration.y = ay
            msg.linear_acceleration.z = az

            # Dados do giroscópio (rad/s)
            gx, gy, gz = self.bno.gyro
            msg.angular_velocity.x = gx
            msg.angular_velocity.y = gy
            msg.angular_velocity.z = gz

            # Dados do vetor de rotação (quaternion)
            qx, qy, qz, qw = self.bno.game_quaternion
            msg.orientation.x = qx
            msg.orientation.y = qy
            msg.orientation.z = qz
            msg.orientation.w = qw

            # Covariâncias (valores pequenos não-nulos)
            msg.orientation_covariance[0] = 0.001
            msg.orientation_covariance[4] = 0.001
            msg.orientation_covariance[8] = 0.001

            msg.angular_velocity_covariance[0] = 0.001
            msg.angular_velocity_covariance[4] = 0.001
            msg.angular_velocity_covariance[8] = 0.001

            msg.linear_acceleration_covariance[0] = 0.001
            msg.linear_acceleration_covariance[4] = 0.001
            msg.linear_acceleration_covariance[8] = 0.001

            self.imu_pub.publish(msg)

        except Exception as e:
            self.get_logger().error(f'Erro ao ler/publicar dados do IMU: {e}')
            self.init_sensor()

def main(args=None):
    rclpy.init(args=args)
    node = BNO085Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
