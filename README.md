# AtCoder ファイル自動振り分け環境ソフト

## 仕様

ファイル階層が以下のようになるように構成する。

comp_pro
|_AtCoder
||_ABC
||_ARC
||_AGC
||_Others
|_Sand (ここを追加、ここに書いたファイルがAtCoderに入る。)
|_ope (移動などの処理を行う)


## 使い方

### ファイルの名前の付け方。

Sandでコードを書くその時の命名規則として、

```
(コンテスト)(大何回か)-(何問題か).py
```

と表記する。

```
ABC193-A.py
```

とすれば、
AtCoder/ABC/ABC193/A.py

に格納される。


### opeの使い方
comp_proのディレクトリにおいて、

```
python ope/main.py 
```


で実行できる。