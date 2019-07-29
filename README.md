# magma.py
[Magma Calculator](http://magma.maths.usyd.edu.au/calc/)をコマンドラインから実行するツール

## Usage

```sh
$ python magma.py [-v] FILE
```

`-v` オプションをつけると計算時間などの情報も表示します。

使用例：

```
$ echo print(DihedralGroup(4)); > source.magma
$ python magma.py source.magma

Permutation group acting on a set of cardinality 4
Order = 8 = 2^3
   (1, 2, 3, 4)
   (1, 4)(2, 3)
```
