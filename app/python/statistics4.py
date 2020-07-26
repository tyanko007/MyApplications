#! /usr/bin/env python3
# coding: utf-8

# 母集団からの標本抽出シミュレーション

# 必要なライブラリの準備
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
# グラフの描写用のライブラリ
from matplotlib import pyplot as plt
import seaborn as sns
# グラフをwebで表示するための独自ライブラリ
import imgfunc as f

# 小数点の整理
class list_format:
    def __init__(self, list):
        self.list = list

    def format(self):
        k = len(self.list)
        i_list = np.arange(start=0, stop=k, step=1)
        for i in i_list:
            self.list[i] = f'{self.list[i]:.3f}'
        return self.list

def main():
    # グラフデザインの固定と画像の初期化
    sns.set()
    plt.figure()

    # 5尾しかいない湖からの標本抽出
    def fish_5():
        # 変数の中身確認用
        def variable_confirm(c1, c2, c3, c4):
            print(c1, c2, c3, c4)

        data = np.array([2,3,4,5,6])
        # 標本からランダムサンプリング(同じものは禁止)
        rmdata = np.random.choice(data, size=1, replace=False)
        rmdata3 = np.random.choice(data, size=3, replace=False) # 3尾のサンプリング
        # 毎回同じ値をランダムにサンプリング(乱数を固定)
        seed = np.random.seed(1) # 引数に1を指定
        seed = np.random.choice(data, size=3, replace=False)

        # run function
        variable_confirm(data, rmdata, rmdata3, seed)

    # より多くの魚がいる湖からの抽出
    def fish_many():
        # 変数の中身確認用
        def variable_confirm(c1, c2):
            line_f = list_format(c2)
            line = "---------------------------"
            print(c1.head())
            print(line)
            print(line_f.format())
            print(line)
            print("c2の平均 >> " + str(f'{c2.mean():.3f}'))

        # 10000尾のサンプルデータ
        data = pd.read_csv("/root/app/sts4_csv.csv")["length"]
        # 10尾のサンプリング
        rmdata10 = np.random.choice(data, size=10, replace=False)

        # 母集団分布の準備
        base_mean = data.mean()
        base_std = sp.std(data, ddof=0) # 母標準偏差
        base_var = sp.var(data, ddof=0) # 母分散
        # グラフ描写
        def sigma_graph(list):
            title = "fish_population_graph"
            plt.title(title)
            graph = sns.distplot(list, kde=False, color='black')
            # オプション付きのview表示のコードの追加


        # run function
        variable_confirm(data, rmdata10)

    # run exec function
    # fish_5()
    # fish_many()

    def debug_space():
        test = f.image_graph("graph", "graph_title")
        test.view_option("", "", "")
    debug_space()

main()
