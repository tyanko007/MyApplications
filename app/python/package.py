# coding: utf-8

# 必要なパッケージのインポート
import numpy as np
import pandas as pd

def main():
    #リスト：複数データをまとめたもの
    def list():
        dies = [1,2,3,4,5,6] # 配列、パッケージは必要なし
        print(dies) # 配列そのものを表示
        print(dies[3]) # 中身を一つのみ抽出
        for i in dies: # 一つずつ全部抽出
            print(i)
    # アレイ：配列の要素をまとめたもの
    def np_array():
        kisu = np.array([1,3,5,7,9]) # リストを利用してアレイを宣言
        s = input("選んでください：奇数=0 or 偶数=1 >>")
        result = kisu + int(s)
        print(result) # 全ての要素に適用される

        print(kisu * 2) # 積も同じ

        # 行列も可能
        table = np.array([[1,2,3,4,5],[6,7,8,9,10]])
        print(table)
        print(table.shape) # 行列の要素数の検査
    # 等差数列の作成
    def np_arange():
        # 開始値=0, 終了値=100, 間隔=10
        arange1 = np.arange(start = 0, stop = 100, step = 10)
        print(arange1)
        # 開始値=0.1, 終了値=8.1, 間隔=0.9
        arange2 = np.arange(start = 0, stop = 8.1, step = 0.9)
        print(arange2)
    # 同じ値の複製、全てアレイの形となる
    def np_tile():
        # appleをいっぱい作成
        tile1 = np.tile("apple", 10)
        print(tile1)
        # 数値も可能
        tile2 = np.tile(77, 5)
        print(tile2)
        print("アレイなので全て78になる  >> " + str(tile2 + 1))
        # 0 ならば関数がある
        zeros1 = np.zeros(10)
        print(zeros1)
        # 0 の多次元配列もできちゃう
        zeros2 = np.zeros([3,3])
        print(zeros2)
        # 1 もできちゃう
        ones1 = np.ones(5)
        print(ones1)
    # スライシング：範囲指定
    def srising():
        sample = np.arange(start = 1, stop = 10, step = 1)
        print(sample)
        print(sample[0:3]) # この場合 0 ~ 3　の範囲内の値が抽出される
        sample2 = np.array([np.arange(start = 0.1, stop = 0.6, step = 0.1), np.arange(start = 6, stop = 11, step = 1)])
        print(sample2)
        print(sample2[0, 4]) #　この場合行列を示す。よって0行5列目の値を取得
        print(sample2[1, 2:4]) # この場合　1行 2~4列目の内の値を取得

    # 実行
    #list()
    #np_array()
    #np_arange()
    #np_tile()
    srising()

main()
