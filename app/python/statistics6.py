#! /usr/bin/env python3
# coding: utf-8

# 標本分散のシミュレーション

# 必要なパッケージ
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
# グラフ作図
from matplotlib import pyplot as plt
import seaborn as sns
# 個人用
import class_module as f
# グラフデザインの背景の指定
sns.set()

def main():
    # 標本分散の平均の確認
    def var_check():
        np.random.seed(1)
        var = f.sigma_calc(size=10, n_trial=10000)
        var_f = f.list_format(lv=1, data=var.create_source_var())

    # サンプルサイズ別の母分散平均のグラフ
    def arange_samplesize_var():
        # シード値の固定
        np.random.seed(1)
        # 準備
        pop = stats.norm(loc=4, scale=0.8)
        # 各サンプルサイズの用意
        size = np.arange(start=10, stop=100010, step=10)
        box = np.zeros(len(size))
        for i in range(0, len(size)):
            tmp = pop.rvs(size=size[i])
            box[i] = sp.var(tmp, ddof=1)
        # グラフの描写
        title = "range_samplesize_var_graph"
        plt.title(title)
        plt.xlabel("sample_size")
        plt.ylabel("arange_var_data")
        graph = plt.plot(size, box, color="black")
        canvas = f.image_graph(dt_graph=graph, dt_name=title)
        canvas.view_option(me=4, st=0.8, va="")

    # 中心極限定理：
    # 分布にさゆうされることなくサンプルサイズが大きい時確率変数の和は正規分布に近いものになる
    def coin_check():
        n_size = 10000
        n_trial = 50000
        # 表なら1, 裏なら0
        coin = np.array([0, 1])
        count_coin = np.zeros(n_trial)
        # 思考実験：コインをn_size回数投げる施工をn_trial回行う
        np.random.seed(1)
        for i in range(0, n_trial):
            count_coin[i] = sp.sum(sp.random.choice(coin, size=n_size, replace=True))
        # ヒストグラムで描写
        title = "coin_check_graph(ver.Histgram)"
        plt.title(title)
        graph = sns.distplot(count_coin, color="black")
        canvas = f.image_graph(dt_name=title, dt_graph=graph)
        canvas.view_option(me="", va="", st="")

    # 実行
    # var_check()
    # arange_samplesize_var()
    coin_check()

    # debug_code
    def debug():
        np.random.seed(1)
        t = f.sigma_calc(size=10, n_trial=10)
        tf = f.list_format(lv=1, data=t.create_source_var())
        print(tf.format())

    # debug()

main()
