#! /usr/bin/env python3
# coding: utf-8

# ライブラリのインストール
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
# グラの描写用ライブラリ
from matplotlib import pyplot as plt
import seaborn as sns
# グラフの表示用クラス
import class_module as f

# グラフデザインの指定
sns.set()

# array型リストのformat調整
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
    # ベースデータ読み込み
    # end
    # ベース変数の設定
    base_population = stats.norm(loc=4, scale=0.8)
    # end

    # 標本平均を何度も計算
    def loop_calclation(pop):
        sample_list_box = np.zeros(10000) # 空のリストを用意
        np.random.seed(1) # 乱数の固定
        # 標本抽出のシミュレーション
        for i in range(0, 10000):
            sample = pop.rvs(size=10)
            sample_list_box[i] = sp.mean(sample)

        res = list_format(sample_list_box).format()
        print(res, len(res))
        print("10000の標本平均の平均 >> " + str(f'{res.mean():.3f}'))

    # 標本平均の特徴
    def sigma_mean_feature(pop):
        box = np.zeros(10000) # 空のリストを用意
        np.random.seed(1) # 乱数の固定
        # 標本抽出のシミュレーション
        for i in range(0, 10000):
            var = pop.rvs(size=10)
            box[i] = sp.mean(var)

        box_mean = np.mean(box) # １００００もの標本平均の平均
        box_std = sp.std(box, ddof=1) # １００００もの標本平均の不偏標準偏差
        box_var = sp.var(box, ddof=1) # ついでに分散も
        # グラフに示す
        title = "sigma_mean_feature_graph"
        plt.title(title)
        graph = sns.distplot(box, color="black")
        canvas = f.image_graph(graph, title)
        canvas.view_option(box_mean, box_std, box_var)

    # サンプルサイズを変化させたときの標本平均
    def bigger_samplesize(pop):
        # サンプルサイズの用意(10 ~ 100100まで100区切りでプールを用意)
        size_array = np.arange(start=10, stop=100100, step=100)
        # 標本平均を格納する箱の用意
        samplesize_box = np.zeros(len(size_array))
        # 標本平均をサンプルサイズ別に格納
        np.random.seed(1)
        for i in range(0, len(size_array)):
            dt = pop.rvs(size = size_array[i])
            samplesize_box[i] = sp.mean(dt)
        # 標本平均の各情報
        box_mean = sp.mean(samplesize_box)
        box_std = sp.std(samplesize_box, ddof=1)
        box_var = sp.var(samplesize_box, ddof=1)
        # グラの描写
        title = "bigger_samplesize_graph"
        plt.title(title)
        graph = plt.plot(size_array, samplesize_box, color="black")
        graph = plt.xlabel("sanple_size")
        graph = plt.ylabel("sample_mean")
        canvas = f.image_graph(graph, title)
        canvas.view_option(box_mean, box_std, box_var)

    # サンプルサイズを変えた際の標本平均の分布
    def arange_samplesize():
        # シード値の固定
        np.random.seed(1)
        # samplesize=10
        size_10 = f.sigma_calc(size=10, n_trial=10000)
        size_10_df = pd.DataFrame({
            "list_mean": size_10.create_source(),
            "size": np.tile("size 10", 10000)
        })
        # samplesize=20
        size_20 = f.sigma_calc(size=20, n_trial=10000)
        size_20_df = pd.DataFrame({
            "list_mean": size_20.create_source(),
            "size": np.tile("size 20", 10000)
        })
        # samplesize=30
        size_30 = f.sigma_calc(size=30, n_trial=10000)
        size_30_df = pd.DataFrame({
            "list_mean": size_30.create_source(),
            "size": np.tile("size 30", 10000)
        })

        # 結合
        sim_result = pd.concat([size_10_df, size_20_df, size_30_df])
        # print(sim_result.head())

        # グラフの表示
        title = "arange_samplesize_graph"
        plt.title(title)
        graph = sns.violinplot(x="size", y="list_mean", data=sim_result, color="gray")
        canvas = f.image_graph(graph, title)
        canvas.view_option(me="", st="", va="")

    # 標本平均集団と母集団との標準偏差の関係
    def sigma_mean_deviation():
        # prepare
        base_samplesize = np.arange(start=2, stop=102, step=2)
        base_box = np.zeros(len(base_samplesize))
        # シード値の固定
        np.random.seed(1)
        for i in range(0, len(base_samplesize)):
            tmp_box = f.sigma_calc(size=base_samplesize[i], n_trial=100)
            base_box[i] = sp.std(tmp_box.create_source(), ddof=1)
        # グラフの描写
        title = "sigma_mean_deviation_graph"
        plt.title(title)
        graph = plt.plot(base_samplesize, base_box, color="black")
        graph = plt.xlabel("base_samplesize")
        graph = plt.ylabel("base_box")
        canvas = f.image_graph(graph, title)
        canvas.view_option(me="", st="", va="")

    # 標本平均の標準偏差=標準誤差の計算
    def sigma_standard_error():
        # prepare
        spm = np.arange(start=2, stop=102, step=2)
        std_box = np.zeros(len(spm))
        # 単純な計算式
        st_err_1 = 0.8 / np.sqrt(spm)
        # 標本平均の標準偏差
        np.random.seed(1)
        for i in range(0, len(spm)):
            tmp = f.sigma_calc(size=spm[i], n_trial=100)
            std_box[i] = sp.std(tmp.create_source(), ddof=1)
        # 変数の確認用
        def var_conf(v):
            print(v)
        # var_conf(std_box) # コメントアウト推奨

        # 標本平均の標準偏差と標準誤差のグラフ
        title = "sigma_standard_error_graph"
        plt.title(title)
        graph = plt.plot(spm, std_box, color="black")
        graph = plt.plot(spm, st_err_1, linestyle="dotted", color="black")
        graph = plt.xlabel("smaple_size")
        graph = plt.ylabel("mean_std_value")
        canvas = f.image_graph(dt_graph=graph, dt_name=title)
        canvas.view_option(me="", st="", va="")


    # 実行
    # loop_calclation(base_population)
    # sigma_mean_feature(base_population)
    # bigger_samplesize(base_population)
    # arange_samplesize()
    # sigma_mean_deviation()
    sigma_standard_error()

    # debug room
    def debug_space():
        # normal confirm. for exsample check the variable status for yourself.
        def exe_conf():
            # np.random.seed(1)
            test = f.sigma_calc(size = 10, n_trial = 10000)
            print(test.create_source())
            print(f'{sp.mean(test.create_source()):.3f}')

        # exception confirm. for exsample check error flow and error code
        def err_conf():
            elist = np.arange(start=2, stop=102, step=2)
            box = np.zeros(len(elist))
            for i in range(0, len(elist)):
                a = f.sigma_calc(size=10, n_trial=10)
                box[i] = sp.mean(a.create_source())
            print(box)

        # select debug func
        # exe_conf()
        # err_conf()

    # debug_space()
    # end
main()
