#! /usr/bin/env python3

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
import yaml
import math

waypoints_file = '/home/westbots/dev_ws/src/trekking_amr/config/waypoints.yaml'

def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx * dx + dy * dy)

def main():
    rclpy.init()
    navigator = BasicNavigator()

    # Carregar waypoints do arquivo YAML
    with open(waypoints_file, 'r') as file:
        waypoints = yaml.safe_load(file)

    def create_pose(transform):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = navigator.get_clock().now().to_msg()
        pose.pose.position.x = transform["position"]["x"]
        pose.pose.position.y = transform["position"]["y"]
        pose.pose.position.z = transform["position"]["z"]
        pose.pose.orientation.x = transform["orientation"]["x"]
        pose.pose.orientation.y = transform["orientation"]["y"]
        pose.pose.orientation.z = transform["orientation"]["z"]
        pose.pose.orientation.w = transform["orientation"]["w"]
        return pose

    goal_poses = list(map(create_pose, waypoints["waypoints"]))

    navigator.waitUntilNav2Active(localizer="smoother_server")
    print('Nav2 active!')

    for i, goal_pose in enumerate(goal_poses):
        print(f'\n[Waypoint {i + 1}/{len(goal_poses)}] Enviando objetivo...')
        navigator.goToPose(goal_pose)

        nav_start = navigator.get_clock().now()

        last_pos = None
        last_move_time = nav_start

        while not navigator.isTaskComplete():
            feedback = navigator.getFeedback()
            now = navigator.get_clock().now()

            # Timeout geral
            if now - nav_start > Duration(seconds=300):
                print(f'Tempo total excedido no waypoint {i + 1}, pulando...')
                navigator.cancelTask()
                break

            # Verificar se está travado por 10 segundos
            if feedback and feedback.current_pose:
                current_pos = feedback.current_pose.pose.position
                if last_pos is None:
                    last_pos = current_pos
                else:
                    if distance(current_pos, last_pos) > 0.05:
                        last_move_time = now
                        last_pos = current_pos
                    elif now - last_move_time > Duration(seconds=6):
                        print(f'Robô travado por mais de 6s no waypoint {i + 1}, pulando...')
                        navigator.cancelTask()
                        break

                print(f'   - Indo para ({goal_pose.pose.position.x:.2f}, {goal_pose.pose.position.y:.2f}) | Atual: ({current_pos.x:.2f}, {current_pos.y:.2f})')

        result = navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print(f'Waypoint {i + 1} alcançado!')
        elif result == TaskResult.CANCELED:
            print(f'Waypoint {i + 1} cancelado.')
        elif result == TaskResult.FAILED:
            print(f'Waypoint {i + 1} falhou. Pulando para o próximo.')
        else:
            print(f'Status desconhecido em waypoint {i + 1}. Pulando...')

    print('\nTodos os waypoints processados!')
    exit(0)

if __name__ == '__main__':
    main()
