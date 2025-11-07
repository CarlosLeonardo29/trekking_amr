import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('trekking_amr')
    use_sim_time = LaunchConfiguration('use_sim_time', default='False')

    return LaunchDescription([
        # Transformação entre base_link e lidar_link_1 - LaserScan
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='chassi_to_lidar_1_broadcaster',
            arguments=['0.0', '0.0', '0.0', '0', '0', '0', 'lidar_link', 'lidar_link_1'],
            output='screen'
        ),

        # Transformação entre base_link e imu_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='chassi_to_imu_broadcaster',
            arguments=['0.0', '0.0', '0.05', '0', '0', '0', 'base_link', 'imu_link'],
            output='screen'
        ),
    ])
