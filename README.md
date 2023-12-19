# mypkg
![test](https://github.com/JusticeMaple/mypkg/actions/workflows/test.yml/badge.svg)

## ブランチmainについて

* こちらのブランチのプログラムは数学的なプログラムです。数が加算されると同時に、その数が偶数か奇数かを判定し、その情報を表示するものです。

# 1.1ver : 表示がさらに見やすくなった

* rclpy モジュールのログのフォーマットは、環境変数 RCUTILS_CONSOLE_OUTPUT_FORMAT を設定することで変更しました。

## 機能概要

- `talker.py`: ROS2ノードで、1から順に数を加算して`countup` トピックにパブリッシュします。
- `listener.py`: ROS2ノードで、`countup` トピックの数をサブスクライブし、受信した数が奇数か偶数かを判定して表示します。


## 使用前の準備
# インストール方法

* ご自身の環境で以下を入力

```
$ git clone https://github.com/JusticeMaple/mypkg.git
```
# ビルド方法
```
$ cd ~/ros2_ws
$ git switch -f main
$ colcon build
```
## 「talker.py」,「listener.py」の機能について
* talker.pyで1ずつ加算されていく数を、listener.pyで表示する。

## 使用例
```
$ cd ~/ros2_ws
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/tei/.ros/log/2023-12-19-20-00-31-119551-JusticeZWY-2651
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [2652]
[INFO] [listener-2]: process started with pid [2654]
[talker-1] INFO [talker]: Publishing: 1
[listener-2] INFO [listener]: Listen: 1, Result: odd
[talker-1] INFO [talker]: Publishing: 2
[listener-2] INFO [listener]: Listen: 2, Result: even
[talker-1] INFO [talker]: Publishing: 3
[listener-2] INFO [listener]: Listen: 3, Result: odd
・・・
```
## ノードとトピック
![2023-01-10 (5)](https://user-images.githubusercontent.com/115678618/211739868-ae299d5b-54cb-4f40-8130-aae515fd8d83.png)

/talkerのノードから1ずつ加算されたnの数値がトピックである/chatterで/listnerに送っている。

## 必要なソフトウェア

* Python
    * テスト済み: 3.7〜3.10

## テスト環境

* GitHub Actions

* Ubuntu 22.04.2 LTS

* Python 3.7 ～ 3.10


## ライセンス

* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  * [ryuichiueda/my_slides robosys_2023](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

* このプログラムは、森巧尚著作　“Python2年生 第2版 体験してわかる！会話でまなべる！プログラミングのしくみ”を参考にしています。

* © 2023 Yunyuan_Zheng
