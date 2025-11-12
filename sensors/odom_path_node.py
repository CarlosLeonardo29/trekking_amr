import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseArray, Pose
import csv
import os

class OdomPathFiltered(Node):
    def __init__(self):
        super().__init__('odom_path_node')

        # Publica apenas PoseArray no tópico /odom_path
        self.arr_pub = self.create_publisher(PoseArray, '/odom_path', 10)

        # Assina odometria
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        # PoseArray inicial
        self.pose_array = PoseArray()
        self.pose_array.header.frame_id = 'odom'

        self.last_x = None
        self.last_y = None

        # Arquivos CSV
        self.odom_file = '/home/westbots/dev_ws/src/trekking_amr/extras/odom.csv'
        self.odom_path_file = '/home/westbots/dev_ws/src/trekking_amr/extras/odom_path.csv'

        # Cabeçalho CSV
        if not os.path.exists(self.odom_file):
            with open(self.odom_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['time', 'x', 'y', 'z', 'qx', 'qy', 'qz', 'qw'])

        if not os.path.exists(self.odom_path_file):
            with open(self.odom_path_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['time', 'x', 'y', 'z', 'qx', 'qy', 'qz', 'qw'])

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        # Salva odometria no CSV
        self.save_odom_csv(msg)

        # Primeira pose: sempre salva no PoseArray
        if self.last_x is None:
            self.save_pose(msg)
            self.last_x = x
            self.last_y = y
            return

        # Salva PoseArray apenas se posição mudou
        if x != self.last_x or y != self.last_y:
            self.save_pose(msg)
            self.last_x = x
            self.last_y = y

    def save_pose(self, msg):
        # Cria o Pose simples
        p = Pose()
        p.position = msg.pose.pose.position
        p.orientation = msg.pose.pose.orientation

        # Adiciona ao PoseArray
        self.pose_array.poses.append(p)

        # Atualiza timestamp
        self.pose_array.header.stamp = self.get_clock().now().to_msg()

        # Publica PoseArray
        self.arr_pub.publish(self.pose_array)

        # Salva no CSV
        self.save_posearray_csv(p)

    def save_odom_csv(self, msg):
        t = self.get_clock().now().to_msg()
        p = msg.pose.pose.position
        o = msg.pose.pose.orientation
        with open(self.odom_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([t.sec + t.nanosec * 1e-9, p.x, p.y, p.z, o.x, o.y, o.z, o.w])

    def save_posearray_csv(self, pose):
        t = self.get_clock().now().to_msg()
        p = pose.position
        o = pose.orientation
        with open(self.odom_path_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([t.sec + t.nanosec * 1e-9, p.x, p.y, p.z, o.x, o.y, o.z, o.w])


def main():
    rclpy.init()
    rclpy.spin(OdomPathFiltered())
    rclpy.shutdown()


if __name__ == '__main__':
    main()
