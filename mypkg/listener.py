#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2023 Yunyuan_Zheng
# SPDX-License-Identifier: BSD-3-Clause


import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node):
    def __init__(self, node_name='listener_node'):
        super().__init__(node_name)
        self.subscription = self.create_subscription(Int16, 'countup', self.callback, 10)

    def callback(self, msg):
        number = msg.data
        result = "even" if number % 2 == 0 else "odd"
        self.get_logger().info('Listen: %d, Result: %s' % (number, result))

def main(args=None):
    rclpy.init(args=args)
    listener_node = ListenerNode()
    rclpy.spin(listener_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

