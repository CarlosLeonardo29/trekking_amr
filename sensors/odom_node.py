#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import serial
import time
import math

def quaternion_to_yaw(qx, qy, qz, qw):
    """Converte um quaternion em ângulo yaw (rad)."""
    siny_cosp = 2.0 * (qw * qz + qx * qy)
    cosy_cosp = 1.0 - 2.0 * (qy * qy + qz * qz)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    return yaw

class OdometryIMUSubscriber(Node):
    def __init__(self):
        super().__init__('odometry_imu_subscriber')

        # Publishers
        self.publisher_ = self.create_publisher(Odometry, 'odom', 10)
        self.tf_broadcaster = TransformBroadcaster(self)

        # Timer de alta frequência (50 Hz)
        self.timer_period = 0.02
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        # Estado da IMU
        self.imu_quaternion = None  # só vamos considerar depois da primeira leitura
        self.imu_ready = False

        # Subscriber do IMU
        self.create_subscription(Imu, 'imu/data', self.imu_callback, 10)

        # === Serial Encoder ===
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)
            self.get_logger().info(f"🔌 Conectado à serial: {self.ser.port}")
        except serial.SerialException as e:
            self.get_logger().error(f"Erro ao abrir porta serial: {e}")
            self.ser = None

        # Estado inicial
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.last_time = self.get_clock().now().nanoseconds * 1e-9
        self.pulse_count = 0

        # Armazena último yaw para calcular velocidade angular
        self.last_yaw = None

        self.get_logger().info('Nó de Odometria inicializado com sucesso.')

    def imu_callback(self, msg: Imu):
        """Atualiza o quaternion da IMU e inicializa yaw inicial se ainda não estiver pronto."""
        self.imu_quaternion = (
            msg.orientation.x,
            msg.orientation.y,
            msg.orientation.z,
            msg.orientation.w
        )

        if not self.imu_ready:
            qx, qy, qz, qw = self.imu_quaternion
            yaw = quaternion_to_yaw(qx, qy, qz, qw)
            self.last_yaw = yaw
            self.imu_ready = True
            self.get_logger().info(f"✅ IMU inicializada: yaw inicial = {math.degrees(yaw):.2f}°")


    def read_encoder_pulses(self):
        """Conta pulsos recebidos via serial (não bloqueante)."""
        if not self.ser:
            return

        line = self.ser.readline().decode(errors='ignore').strip()
        if line == '1':
            self.pulse_count += 1

    def compute_linear_velocity(self, dt):
        """Calcula velocidade linear com base nos pulsos."""
        D = 0.13 
        C = math.pi * D
        PPR = 4
        distance_per_pulse = C / PPR
        vx = (self.pulse_count * distance_per_pulse) / dt
        self.pulse_count = 0
        return vx

    def timer_callback(self):
        """Atualiza pose e publica odometria e TF."""
        if not self.imu_ready:
            # Ainda não temos dados válidos do IMU — espera a primeira leitura
            return
        
        self.read_encoder_pulses()

        current_time = self.get_clock().now().nanoseconds * 1e-9
        dt = current_time - self.last_time
        if dt <= 0:
            return
        self.last_time = current_time

        vx = self.compute_linear_velocity(dt)
        qx, qy, qz, qw = self.imu_quaternion
        yaw = quaternion_to_yaw(qx, qy, qz, qw)

        # Velocidade angular (derivada do yaw)
        wz = (yaw - self.last_yaw) / dt
        if wz > math.pi:
            wz -= 2 * math.pi
        elif wz < -math.pi:
            wz += 2 * math.pi
        self.last_yaw = yaw

        # Atualiza posição no plano XY de acordo com yaw
        self.x += vx * math.cos(yaw) * dt
        self.y += vx * math.sin(yaw) * dt

        # Publica odometria e TF
        self.publish_odometry(self.x, self.y, self.z, vx, wz, qx, qy, qz, qw)
        self.publish_transform(self.x, self.y, self.z, qx, qy, qz, qw)

    def publish_odometry(self, x, y, z, vx, wz, qx, qy, qz, qw):
        """Publica mensagem de Odometry."""
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'odom'
        msg.child_frame_id = 'base_link'

        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        msg.pose.pose.position.z = z
        msg.pose.pose.orientation.x = qx
        msg.pose.pose.orientation.y = qy
        msg.pose.pose.orientation.z = qz
        msg.pose.pose.orientation.w = qw

        msg.twist.twist.linear.x = vx
        msg.twist.twist.angular.z = wz
        self.publisher_.publish(msg)

    def publish_transform(self, x, y, z, qx, qy, qz, qw):
        """Publica a transformação odom → base_link."""
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'

        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = z
        t.transform.rotation.x = qx
        t.transform.rotation.y = qy
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw

        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = OdometryIMUSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node.ser:
            node.ser.close()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
