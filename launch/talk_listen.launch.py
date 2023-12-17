#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2023 Yunyuan_Zheng
# SPDX-License-Identifier: BSD-3-Clause

import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    talker = launch_ros.actions.Node(
            package='mypkg',
            executable='talker',
            )
    listener = launch_ros.actions.Node(
            package='mypkg',
            executable='listener',
            output='screen',
            )

    return launch.LaunchDescription([talker, listener])
