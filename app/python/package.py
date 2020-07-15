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
    # データフレーム：pandasを利用した表の操作
    def pd_dataframe():
        numlist = np.arange(start=1, stop=6, step=1)
        dtframe = pd.DataFrame({
            'col1' : numlist,
            'col2' : numlist * 2,
            'col3' : ["A", "B", "C", "D", "E"]
        })
        print(dtframe)
    # ファイルデータの取り込み
    def read_file():
        charctor = pd.read_csv("sample.csv") # csvデータをデータフレームとして取り込む
        print(charctor)
    # データフレームの結合
    def join_dataframe():
        join1 = pd.DataFrame({
            'col1': np.arange(start=1,stop=11,step=1),
            'col2': np.arange(start=100,stop=0,step=-10),
            'col3': np.tile("banana",10)
        })

        join2 = pd.DataFrame({
            'col1': np.arange(start=10,stop=110,step=10),
            'col2': np.arange(start=10,stop=0,step=-1),
            'col3': np.tile("apple",10)
        })
        # 縦方向にデータフレームを結合
        vertical_join = pd.concat([join1,join2])
        # 横方向にデータフレームを結合
        horizon_join = pd.concat([join1,join2], axis=1)

        print("sample data 1")
        print(join1)
        print("sample data 2")
        print(join2)
        print("縦結合")
        print(vertical_join)
        print("横結合")
        print(horizon_join)

    # 列に対するデータフレームの操作
    def row_dataframe():
        list = np.arange(start=1, stop=6, step=1)
        sample = pd.DataFrame({
            'col1': list,
            'col2': list * 2,
            'col3': np.array(["A","B","C","D","E"])
        })
        print(sample)
        # 列名の指定
        print(sample.col2)
        # こっちの方法でも可能
        print(sample['col2'])
        # 複数列を抽出
        print(sample[['col2','col3']])
        # 特定列のみなくす
        print(sample.drop("col2", axis=1))

    # 行に対するデータフレームの操作
    def col_dataframe():
        horizon = "-------------------------------"
        list = np.arange(start=1, stop=6, step=1)
        sample = pd.DataFrame({
            'col1': list,
            'col2': list * 2,
            'col3': np.array(["A","B","C","D","E"])
        })
        print(sample)
        print(horizon)
        #先頭のn行だけを指定
        print(sample.head(n = 3))
        print(horizon)
        #query関数
        print(sample.query('index == 0')) # ０行目を指定
        print(horizon)
        print(sample.query('col3 == "A"')) # col3列目にAが含まれる行を指定
        print(horizon)
        print(sample.query('col3 == "A" | col3 == "D"')) # col3列目にAまたはDが含まれる列を指定
        print(horizon)
        print(sample.query('col3 == "A" & col3 == "D"')) # col3列目にAかつDが含まれる列を指定
        print(horizon)
        print(sample.query('col3 == "A"')[['col2', 'col3']]) # 条件を指定しつつ行列の指定もしている

    # シリーズ型の理解
    def pd_series():
        # pandasにおけるデータフレームから１列のみ抽出した型
        list = np.arange(start=1, stop=6, step=1)
        sample = pd.DataFrame({
            'col1': list,
            'col2': list * 2,
            'col3': np.array(["A","B","C","D","E"])
        })
        normal_type = type(sample)
        print(sample)
        print("↑のタイプは >> " + str(normal_type))
        print("----------------------------")
        series_type = type(sample.col1)
        print(sample["col1"])
        print("↑のタイプは >> " + str(series_type))

        # シリーズとアレイの関係
        print("----------------------")
        np_type1 = type(np.array(sample.col1))
        print("シリーズ形式のデータをアレイに変換1 >> " + str(np_type1))
        np_type2 = type(sample.col1.values)
        print("シリーズ形式のデータをアレイに変換2 >> " + str(np_type2))

    # 関数のヘルプ
    def function_help():
        list = np.arange(start=1, stop=6, step=1)
        sample = pd.DataFrame({
            'col1': list,
            'col2': list * 2,
            'col3': np.array(["A","B","C","D","E"])
        })
        print("pythonの関数の使い方を説明してくれるhelp関数")
        print(help(sample.query))
        print(help(sample.head))

    # 実行
    #list()
    #np_array()
    #np_arange()
    #np_tile()
    #srising()
    #pd_dataframe()
    #read_file()
    #join_dataframe()
    #row_dataframe()
    #col_dataframe()
    #pd_series()
    #function_help()

main()
