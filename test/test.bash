#!/bin/bash
# SPDX-FileCopyrightText: 2025 Natsuhi Shimada
# SPDX-License-Identifier: BSD-3-Clause

set -e

source /opt/ros/humble/setup.bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

colcon build --symlink-install

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log || true

grep 'Listen: 10' /tmp/mypkg.log

