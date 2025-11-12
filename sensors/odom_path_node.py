import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseArray, Pose

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

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        # Primeira pose: sempre salva
        if self.last_x is None:
            self.save_pose(msg)
            self.last_x = x
            self.last_y = y
            return

        # Salva somente se posição mudou
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

def main():
    rclpy.init()
    rclpy.spin(OdomPathFiltered())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
