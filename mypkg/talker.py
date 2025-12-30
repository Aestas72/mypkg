#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Natsuhi Shimada
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import subprocess


class CommandExecutor(Node):
    def __init__(self):
        super().__init__('command_executor')

        self.publisher_ = self.create_publisher(
            String,
            'command_result',
            10
        )

        self.declare_parameter('command', ['df', '-h'])
        self.command = self.get_parameter('command').get_parameter_value().string_array_value

        self.timer = self.create_timer(5.0, self.timer_callback)
        self.get_logger().info(
            f'CommandExecutor started. Command: {" ".join(self.command)}'
        )

    def timer_callback(self):
        msg = String()
        try:
            result = subprocess.run(
                self.command,
                capture_output=True,
                text=True,
                timeout=3.0
            )
            msg.data = (
                f'Command: {" ".join(self.command)}\n'
                f'Return code: {result.returncode}\n'
                f'STDOUT:\n{result.stdout}\n'
                f'STDERR:\n{result.stderr}'
            )
        except Exception as e:
            msg.data = f'Command execution failed: {e}'

        self.publisher_.publish(msg)
        self.get_logger().info('Published command result')


def main(args=None):
    rclpy.init(args=args)
    node = CommandExecutor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
