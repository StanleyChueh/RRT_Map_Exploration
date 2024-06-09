from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rrt_exploration',
            executable='rrt_exploration',
            name='rrt_exploration',
            output='screen',
            parameters=[{
                # Add any parameters you might need here
            }],
        ),
    ])

