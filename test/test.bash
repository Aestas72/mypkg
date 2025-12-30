#!/bin/bash
# SPDX-FileCopyrightText: 2025 Natsuhi Shimada
# SPDX-License-Identifier: BSD-3-Clause

set -e

WORKSPACE=$1
[ -z "$WORKSPACE" ] && WORKSPACE=$GITHUB_WORKSPACE

cd "$WORKSPACE/src/mypkg"

colcon build --symlink-install

source install/setup.bash

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1

grep 'Listen: 10' /tmp/mypkg.log

