#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Natsuhi Shimada
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CommandLogger(Node):
    def __init__(self):
        super().__init__('command_logger')

        self.subscription = self.create_subscription(
            String,
            'command_result',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

        self.get_logger().info('CommandLogger started')

    def listener_callback(self, msg):
        self.get_logger().info('Listen: 10')
        self.get_logger().info(
            '\n' + '=' * 40 + '\n' +
            msg.data +
            '\n' + '=' * 40
        )


def main(args=None):
    rclpy.init(args=args)
    node = CommandLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
