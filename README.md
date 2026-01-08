# mypkg — コマンド実行ログROS2パッケージ
![test](https://github.com/Aestas72/mypkg/actions/workflows/test.yml/badge.svg)

`mypkg`は、ROS2上でシェルコマンドを定期的に実行し、その実行結果をトピック通信で配信・表示するパッケージです。

システム状態確認(ディスク使用量やプロセス状態など)をROS2ノードとして扱えるため，監視ノードやログ収集ノードと組み合わせて利用できます。

---

## 機能概要

- 任意のシェルコマンドを一定周期で実行
- 実行結果(終了コード・標準出力・標準エラー出力)をトピックで配信
- 別ノードで結果を受信し，ログとして表示

---

## ノード

### talker
指定したシェルコマンドを一定周期で実行し，
実行結果をROS2トピックとしてpublishします。

ロボットや計算機の状態をROS2ネットワーク上に共有する用途を想定しています。

### listener
`talker`がpublishしたトピックをsubscribeし，
受信した実行結果を標準出力に表示します。

動作確認や簡易モニタとして利用できます。

---

## トピック

`/command_result`(`std_msgs/msg/String`)  
実行したコマンドの標準出力・標準エラー・終了コードを
文字列として送信します。

---

## 使い方
```bash
#ノードの起動(launch ファイル使用)
$ ros2 launch mypkg talk_listen.launch.py
```

## 実行例
```bash
========================================
Command: df -h
Return code: 0
STDOUT:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G   64G  893G   7% /

STDERR:

========================================
```

## 動作環境
- ROS2 Jazzy
- Ubuntu 24.04
- GitHub Actions(ubuntu-latest)でテスト済み

## 権利関係・ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されています。
- © 2025 Natsuhi Shimada

## 謝辞
本パッケージの作成にあたり，以下の講義資料を参考にしました。
- [robosys2025（CC-BY-SA 4.0 by Ryuichi Ueda）](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
