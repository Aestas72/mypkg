# mypkg — コマンド実行ログROS2パッケージ
![test](https://github.com/Aestas72/mypkg/actions/workflows/test.yml/badge.svg)

`mypkg` は、ROS2上でシェルコマンドを定期的に実行し、その実行結果を
トピック通信で配信・記録するパッケージです。

---

## ノード構成

- **talker**: 指定コマンドを定期実行し、結果を `command_result` トピックに送信  
- **listener**: `command_result` トピックを購読し、実行結果を標準出力に表示

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
- ROS2 Jazzy
- Ubuntu 24.04
- GitHub Actions（ubuntu-latest）でテスト済み

## 権利関係・ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されています。
- © 2025 Natsuhi Shimada

## 謝辞
本パッケージの作成にあたり，以下の講義資料を参考にしました。
- [robosys2025（CC-BY-SA 4.0 by Ryuichi Ueda）](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
