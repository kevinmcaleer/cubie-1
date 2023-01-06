#!/usr/bin/env python3
# My first Node!

import rclpy
from rclpy.node import Node

def main(args=None):
    """ 
    
    Runs the main loop of code, rclpy.spin() will continue to execute 
    until you terminate the loop
    Press CTRL + C to terminate rclpy.spin().

    """
    rclpy.init(args=args)
    node = Node("py_test")
    node.get_logger().info("Hello ROS2")
    rclpy.spin(node)
    rclpy.shutdown()

# Run the main loop
if __name__ == "__main__":
    main()