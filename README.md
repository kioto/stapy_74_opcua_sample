# stapy_74_opcua_sample

みんなのPython勉強会 #74の発表「PythonによるOPC-UAの利用」で使用したOPC-UAサンプルプログラム。

2021/10/13(水) 19:00 〜 21:00<br>
[みんなのPython勉強会#74](https://startpython.connpass.com/event/224564/)

以下の手順で、必要なパッケージをインストールしておくこと。

```
pip install -r requirements.txt
```

## 1. Simple OPC-UA Server/Client


シンプルなOPC-UAのサーバ/クライアントプログラム。

２つのターミナルから、それぞれコマンドを実行する。

```
# Terminal 1：サーバ
python simple_server.py
```

```
# Terminal 2：クライアント
python simple_client.py
```

サーバプログラムはCtrl+Cで終了する（以下に続くサンプルも同様）。

## 2. 名前空間リストの表示

OPC-UAサーバが持つ、名前空間リストを表示するクライアントプログラム。

２つのターミナルから、それぞれコマンドを実行する。

```
# Terminal 1：サーバ
python simple_server.py
```

```
# Terminal 2：クライアント
python print_namespace_list.py
```

## 3. ノード一覧の表示

OPC-UAサーバが持つ、全てのノードを表示するクライアントプログラム。

２つのターミナルから、それぞれコマンドを実行する。

```
# Terminal 1：サーバ
python simple_server.py
```

```
# Terminal 2：クライアント
python print_nodes.py
```

## 4. OPC-UA method Server/Client


OPC-UAのメソッド呼び出し機能を使用した、サーバ/クライアントプログラム。

２つのターミナルから、それぞれコマンドを実行する。

```
# Terminal 1：サーバ
python method_server.py
```

```
# Terminal 2：クライアント
python method_server.py
```

以上
