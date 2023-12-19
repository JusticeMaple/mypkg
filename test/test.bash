#!/bin/bash
# SPDX-FileCopyrightText: © 2023 Yunyuan_Zheng
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# テスト実行
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# テスト結果の表示
if grep -q 'Listen: 5, Result: odd' /tmp/mypkg.log; then
  echo "Test Passed: Expected output found."
else
  echo "Test Failed: Expected output not found."
  exit 1  # テスト失敗時にスクリプトを終了する
fi

