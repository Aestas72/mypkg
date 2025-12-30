#!/bin/bash
set -e

dir=/root
[ "$1" != "" ] && dir="$1"

# ROS 2 を必ず source
source /opt/ros/humble/setup.bash

cd $dir/ros2_ws
colcon build

# ワークスペースを source
source install/setup.bash

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

grep 'Listen: 10' /tmp/mypkg.log

