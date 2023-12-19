#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2023 Yunyuan_Zheng
# SPDX-License-Identifier: BSD-3-Clause

import os

os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '{severity} [{name}]: {message}'

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(Int16, 'countup', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info("Listen: %d, Result: %s" % (msg.data, "odd" if msg.data % 2 != 0 else "even"))

def main(args=None):
    rclpy.init(args=args)
    listener_node = ListenerNode()
    rclpy.spin(listener_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

