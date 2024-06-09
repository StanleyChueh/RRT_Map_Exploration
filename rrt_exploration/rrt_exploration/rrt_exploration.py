#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid
import random

class RRTExploration(Node):
    def __init__(self):
        super().__init__('rrt_exploration')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription_ = self.create_subscription(
            OccupancyGrid,
            'map',
            self.map_callback,
            10)
        self.subscription_  # prevent unused variable warning
        self.map_data = None

    def map_callback(self, msg):
        self.map_data = msg

    def explore(self):
        if self.map_data is None:
            self.get_logger().info('Waiting for map data...')
            return

        # Implement RRT exploration logic here
        self.get_logger().info('Performing RRT exploration step...')
        # Example: move randomly for demonstration
        twist = Twist()
        twist.linear.x = 0.5 * random.uniform(-1, 1)
        twist.angular.z = 0.5 * random.uniform(-1, 1)
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = RRTExploration()
    try:
        while rclpy.ok():
            rclpy.spin_once(node)
            node.explore()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

