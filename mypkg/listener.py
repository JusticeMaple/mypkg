#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2023 Yunyuan_Zheng
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(Int16, 'countup', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info('Listen: %d' % msg.data)

    def run(self):
        rclpy.spin(self)

def main():
    rclpy.init()
    listener_node = ListenerNode()
    listener_node.run()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

