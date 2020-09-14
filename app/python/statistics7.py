#! /usr/bin/env python3
# coding: utf-8

# 必要なライブラリのインストール
import numpy as np
import scipy as sp
from scipy import stats as sts
import pandas as pd
# グラフ描写用
from matplotlib import pyplot as plt
import seaborn as sns
# 自分用
import class_module as f
# グラフデザインの指定
sns.set()

def main():
    # main変数
    def variable_check():
        # 確率密度の実装
        pi = sp.pi # 円周率
        print("円周率 >> " + str(pi))
        napier = sp.exp(1) # ネイピア数
        print("自然定数の底(ネイピア数) >> " + str(napier))

        # 計算:確率変数=3, 平均=4, 標準偏差=0.8
        x = 3
        mu = 4
        sigma = 0.8

        p_density = 1 / (sp.sqrt(2 * pi * sigma**2)) * sp.exp(- ((x - mu)**2) / (2 * sigma**2))
        print("確率変数=3, 平均=4, 標準偏差=0.8の確率密度 >> " + f'{p_density:.3f}')

        # stats.norm.pdf関数を利用した確率密度の適用
        p_density_func = sts.norm.pdf(loc=4, scale=0.8, x=3)
        print(f'{p_density_func:.3f}')
        # 正規分布のinstanceを作成
        base_p_density = sts.norm(loc=4, scale=0.8)
        res_bpd = base_p_density.pdf(x=3)
        print(f'{res_bpd:.3f}')

    # 標本がある値以下になった割合の抽出
    def value_down_point():
        # シード値の固定
        np.random.seed(1)
        # 正規表現のベースデータ作成
        base_data = sts.norm.rvs(loc=4, scale=0.8, size=100000)
        base_data = f.list_format(lv=1, data=base_data).format()
        # 確率分布の値が３以下の割合
        print(sp.sum(base_data <= 3) / len(base_data))
        # 累積分布関数:f(x) = p(X<=x)を計算する関数
        base_data_func = sts.norm.cdf(loc=4, scale=0.8, x=3)
        base_data_funcb = sts.norm.cdf(loc=4, scale=0.8, x=4)
        print(base_data_func)
        print(base_data_funcb)

    # パーセント点の計算
    def percent_point():
        # 下側確率：確率変数のxがX下回る確率はyだといった条件のこと
        p_point = sts.norm.ppf(loc=4, scale=0.8, q=0.025)
        print(p_point)
        # 下側確率とパーセント計算
        vdp = sts.norm.cdf(loc=4, scale=0.8, x=3)
        p_point_vdf = sts.norm.ppf(loc=4, scale=0.8, q=vdp)
        print(p_point_vdf)

    # t分布の計算
    def t_value_calc():
        # 変数の確認用
        def var_check(v):
            print(v)

        # 準備
        np.random.seed(1)
        resb = np.zeros(10000)
        # 正規分布のインスタンス
        norm_dist = sts.norm(loc=4, scale=0.8)
        # シミュレーション
        for i in range(0, 10000):
            sample = norm_dist.rvs(size=10)
            sample_mean = sp.mean(sample)
            sample_std = sp.std(sample, ddof=1)
            sample_se = sample_std / sp.sqrt(len(sample))
            resb[i] = (sample_mean - 4) / sample_se
        #
        # var_check(resb)
        #
        title = "t_value_calc_graph and probability_density_graph"
        plt.title(title)
        # t値のヒストグラム
        graph = sns.distplot(resb, color="black")
        # 標準正規分布の確率密度
        x = np.arange(start=-8, stop=8.1, step=0.1)
        graph = plt.plot(x, sts.norm.pdf(x=x), color="black", linestyle="dotted")

        canvas = f.image_graph(dt_name=title, dt_graph=graph)
        canvas.view_option(me=4, st=0.8, va=0.64)

    # t分布のグラフ
    def t_bunpu():
        # 準備
        x = np.arange(start=-8, stop=8.1, step=0.1)
        # グラフの描写
        title="t_bunpu_graph"
        plt.title(title)
        plt.plot(x, sts.norm.pdf(x=x), color="black", linestyle="dotted")
        graph = plt.plot(x, sts.t.pdf(x=x, df=9), color="black")

        canvas = f.image_graph(dt_name=title, dt_graph=graph)
        canvas.view_option(va="", st="", me="")

    def tbunpu_and_tvalue():
        #--- t値（標本から計算された標準誤差）
        np.random.seed(1)
        resb = np.zeros(10000)
        # 正規分布のインスタンス
        norm_dist = sts.norm(loc=4, scale=0.8)
        # シミュレーション
        for i in range(0, 10000):
            sample = norm_dist.rvs(size=10)
            sample_mean = sp.mean(sample)
            sample_std = sp.std(sample, ddof=1)
            sample_se = sample_std / sp.sqrt(len(sample))
            resb[i] = (sample_mean - 4) / sample_se
        #--- まで ---
        #--- t分布の確率密度
        x = np.arange(start=-8, stop=8.1, step=0.1)
        #--- まで
        # グラフの描写
        title = "tbunpu_and_tvalue_graph"
        plt.title(title)
        sns.distplot(resb, color="black", norm_hist=True)
        graph = plt.plot(x, sts.t.pdf(x=x, df=9), color="black", linestyle="dotted")

        canvas = f.image_graph(dt_name=title, dt_graph=graph)
        canvas.view_option(me="", st="", va="")

    # 実行
    # variable_check()
    # value_down_point()
    # percent_point()
    # t_value_calc()
    # t_bunpu()
    tbunpu_and_tvalue()

main()
