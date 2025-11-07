import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    slam_param_file = LaunchConfiguration(
        'slam_param_file',
        default='/home/westbots/dev_ws/src/trekking_amr/config/mapper_params_online_async.yaml'
    )
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    base_frame   = LaunchConfiguration('base_frame',   default='base_link')
    odom_frame   = LaunchConfiguration('odom_frame',   default='odom')
    scan_topic   = LaunchConfiguration('scan_topic',   default='/scan_fullframe')

    # Nó do SLAM Toolbox
    slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox_node',
        output='screen',
        parameters=[
            slam_param_file,
            {
                'use_sim_time': use_sim_time,
                'base_frame':   base_frame,
                'odom_frame':   odom_frame,
                'scan_topic':   scan_topic,
            }
        ],
    )

    return LaunchDescription([
        # DeclareLaunchArguments para permitir overrides em tempo de launch
        DeclareLaunchArgument(
            'slam_param_file',
            default_value=slam_param_file,
            description='Path to the SLAM parameters file'
        ),
        DeclareLaunchArgument(
            'use_sim_time',
            default_value=use_sim_time,
            description='Use simulation time'
        ),
        DeclareLaunchArgument(
            'base_frame',
            default_value=base_frame,
            description='Base frame for SLAM (e.g. base_link)'
        ),
        DeclareLaunchArgument(
            'odom_frame',
            default_value=odom_frame,
            description='Odom frame for SLAM (e.g. odom)'
        ),
        DeclareLaunchArgument(
            'scan_topic',
            default_value=scan_topic,
            description='LaserScan topic (e.g. /scan_fullframe)'
        ),
        slam_toolbox_node,
    ])
