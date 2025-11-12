import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
import csv
import os

class NavPlanSaver(Node):
    def __init__(self):
        super().__init__('nav_plan_saver')

        # Flag para salvar apenas a primeira rota
        self.saved_first_plan = False

        # Assina o tópico /plan (Nav2)
        self.plan_sub = self.create_subscription(
            Path,
            '/plan',
            self.plan_callback,
            10
        )

        # Caminho do CSV
        self.plan_file = '/home/westbots/dev_ws/src/trekking_amr/extras/nav_plan.csv'

        # Criar CSV com cabeçalho se não existir
        if not os.path.exists(self.plan_file):
            with open(self.plan_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['time', 'x', 'y', 'z', 'qx', 'qy', 'qz', 'qw'])

        self.get_logger().info(f"Salvando apenas a primeira trajetória do Nav2 (/plan) em: {self.plan_file}")

    def plan_callback(self, msg: Path):
        # Se já salvamos a primeira rota, ignora
        if self.saved_first_plan:
            return

        t = self.get_clock().now().to_msg()

        # Salva todas as poses do Path no CSV
        with open(self.plan_file, 'a', newline='') as f:
            writer = csv.writer(f)
            for pose_stamped in msg.poses:
                p = pose_stamped.pose.position
                o = pose_stamped.pose.orientation
                writer.writerow([
                    t.sec + t.nanosec * 1e-9,  # timestamp em segundos
                    p.x,
                    p.y,
                    p.z,
                    o.x,
                    o.y,
                    o.z,
                    o.w
                ])

        self.saved_first_plan = True  # marca que a primeira rota já foi salva
        self.get_logger().info("Primeira trajetória salva com sucesso!")

def main():
    rclpy.init()
    rclpy.spin(NavPlanSaver())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
