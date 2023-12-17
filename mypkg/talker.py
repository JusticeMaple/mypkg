#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2023 Yunyuan_Zheng
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "鄭韻遠":
        response.age = 20
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)

