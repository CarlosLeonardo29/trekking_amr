from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    trekking_dir = get_package_share_directory('trekking_amr')
    sick_dir = get_package_share_directory('sick_scan_xd')

    return LaunchDescription([
        # Frames do robô
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(trekking_dir, 'launch', 'robot.launch.py')
            )
        ),

        # IMU
        Node(
            package='trekking_amr',
            executable='bno085_node',
            name='bno085_node',
            output='screen'
        ),

        # Odometria
        Node(
            package='trekking_amr',
            executable='odom_node',
            name='odom_node',
            output='screen'
        ),

        # LiDAR SICK
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(sick_dir, 'launch', 'sick_picoscan.launch.py')
            )
        ),

        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),
    ])
