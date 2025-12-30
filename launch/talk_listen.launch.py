#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Natsuhi Shimada
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
        name='command_executor',
        parameters=[{
            'command': ['df', '-h']
        }],
        output='screen'
    )

    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        name='command_logger',
        output='screen'
    )

    return launch.LaunchDescription([
        talker,
        listener
    ])
