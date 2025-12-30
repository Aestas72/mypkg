# mypkg — コマンド実行ログROS 2パッケージ
![test](https://github.com/Aestas72/mypkg/actions/workflows/test.yml/badge.svg)

`mypkg` は、ROS 2 上でシェルコマンドを定期的に実行し、その実行結果を
トピック通信で配信・記録するパッケージです。

コマンドを実行するノードと、実行結果を受信して表示するノードから構成されており、
ROS 2 の topic 通信の基本的な使い方を学ぶことができます。

---

## インストール方法

```bash
# リポジトリをクローン
$ git clone https://github.com/Aestas72/mypkg.git

# ワークスペースへ配置
$ mkdir -p ~/ros2_ws/src
$ mv mypkg ~/ros2_ws/src/

# ビルド
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
```

## 使い方
```bash
#ノードの起動（launch ファイル使用）
$ ros2 launch mypkg talk_listen.launch.py
```

## 実行例
```bash
========================================
Command: df -h
Return code: 0
STDOUT:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda        100G   20G   80G  20% /
...
STDERR:

========================================
```

## 動作環境
- ROS 2 Humble
- Python 3.10
- Ubuntu 22.04（WSL2 含む）
- GitHub Actions（ubuntu-latest）でテスト済み

## 権利関係・ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されています。
- © 2025 Natsuhi Shimada

## 謝辞
本パッケージの作成にあたり，以下の講義資料を参考にしました。
- [robosys2025（CC-BY-SA 4.0 by Ryuichi Ueda）](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)  
スライドを参考にしましたが、コードおよびREADMEの文章は自分で作成したものです。
