#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2023 Yunyuan_Zheng
# SPDX-License-Identifier: BSD-3-Clause

# talker.py

import os

os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '{severity} [{name}]: {message}'

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(Int16, 'countup', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = Int16()
        self.count += 1
        msg.data = self.count
        self.get_logger().info('Publishing: %d' % msg.data)
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    talker_node = TalkerNode()
    rclpy.spin(talker_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

