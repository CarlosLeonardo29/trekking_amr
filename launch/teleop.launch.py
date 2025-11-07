from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Nó - Leitura Controle PS4
        Node(
            package="joy",
            executable="joy_node",
            name="joy_node",
            output="screen"
        ),

        # Nó - Conversão /joy -> /cmd_vel
        Node(
            package="teleop_twist_joy",
            executable="teleop_node",
            name="teleop_twist_joy_node",
            parameters=["/home/westbots/dev_ws/src/trekking_amr/config/ps4.config.yaml"],
            output="screen"
        )
    ])
