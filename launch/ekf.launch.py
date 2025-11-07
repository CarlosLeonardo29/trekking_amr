import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('trekking_amr')
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[
                os.path.join(pkg_share, 'config', 'ekf.yaml'),
                {'use_sim_time': use_sim_time}
            ],
        )
    ])
