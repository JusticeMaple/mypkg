# mypkg
![test](https://github.com/JusticeMaple/mypkg/actions/workflows/test.yml/badge.svg)

## ブランチlesson10について

*こちらのブランチのプログラムは数学的なプログラムです。

## リポジトリの概要

* talker.py : パブリッシャーの役割を持つ

* listener.py : サブスクライバーの役割を持つ

## 使用前の準備
# インストール方法

* ご自身の環境で以下を入力

```
$ https://github.com/JusticeMaple/mypkg.git

```
#ビルド方法
```
$ cd ~/ros2_ws
$ colcon build
```
## 「talker.py」,「listener.py」の機能について
* talker.pyで1ずつ加算されていく数を、listener.pyで表示する。

## 使用例
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/tei/.ros/log/2023-12-17-22-55-11-639875-JusticeZWY-37104
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [37105]
[INFO] [listener-2]: process started with pid [37107]
[listener-2] [INFO] [1702821312.336951071] [listener]: Listen: 0
[listener-2] [INFO] [1702821312.829435447] [listener]: Listen: 1
[listener-2] [INFO] [1702821313.328767545] [listener]: Listen: 2
[listener-2] [INFO] [1702821313.829203116] [listener]: Listen: 3
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

* このプログラムは、森巧尚著作　“Python1年生 第2版 体験してわかる！会話でまなべる！プログラミングのしくみ”を参考にしています。

* © 2023 Yunyuan_Zheng
