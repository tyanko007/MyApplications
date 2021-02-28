#! /usr/bin/env python3
# coding: utf-8

# must packages
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import class_module as f

plt.figure()

def main():

    # base variables
    base_list = pd.read_csv("/root/app/sts3_csv.csv")
    base_list2 = pd.read_csv("/root/app/sts2-3_csv.csv")
    # debug_place
    # print(base_list.groupby("species").describe()) # データの情報の確認

    # 折れ線グラフ
    def lineplot():
        # データの用意
        x = np.array([0,1,2,3,4,5,6,7,8,9])
        y = np.array([2,3,4,3,5,4,6,7,4,8])

        # グラフの描写
        title = "linegraph"
        plt.title(title)
        graph = plt.plot(x, y, color="blue")

        canvas_view = f.image_graph(graph, title)
        canvas_view.view()

    def lineplot_seaborn():
        # データの用意
        x = np.array([0,1,2,3,4,5,6,7,8,9])
        y = np.array([2,3,4,3,5,4,6,7,4,8])
        # グラフデザインの設定
        sns.set()

        # グラフの描写
        title = "linegraph_seaborn"
        plt.title(title)
        graph = plt.plot(x, y, color="black")

        canvas_view = f.image_graph(graph, title)
        canvas_view.view()

    def histogram():
        # データの用意
        list_data = np.array([2,3,3,4,4,4,4,5,5,6])
        # グラフデザインの設定
        sns.set()
        # グラフの描写
        title = "histogram_seaborn"
        plt.title(title)
        graph = sns.distplot(list_data, bins=5, color="black", kde=False)

        canvas_view = f.image_graph(graph, title)
        canvas_view.view()

    def bins_1_design():
        # データの用意
        list_data = np.array([2,3,3,4,4,4,4,5,5,6])
        # グラフデザインの設定
        sns.set()
        # グラフの描写
        title = "bins_1_histgram"
        plt.title(title)
        graph = sns.distplot(list_data, bins=1, color="black", kde=False)

        canvas_view = f.image_graph(graph, title)
        canvas_view.view()

    def kernel_design():
        # データの用意
        list_data = np.array([2,3,3,4,4,4,4,5,5,6])
        # グラフデザインの設定
        sns.set()
        # グラフの描写
        title = "kernel_design_histgram"
        plt.title(title)
        graph = sns.distplot(list_data, color="black")

        canvas_view = f.image_graph(graph, title)
        canvas_view.view()

    def multi_line(list_data):

        # グループ別に分割
        list_a = list_data.query('species=="A"')["length"]
        list_b = list_data.query('species=="B"')["length"]

        # グラフデザインの指定
        sns.set()
        #グラフの描写
        title = "multi_line_graph"
        plt.title(title)
        graph = sns.distplot(list_a, bins=5, color="red", kde=False)
        graph = sns.distplot(list_b, bins=5, color="blue", kde=False)
        # グラフの表示
        canvas_view = f.image_graph(graph, title)
        canvas_view.view()

    # 箱髭図
    def boxplot(data):

        #グラフデザインの指定
        sns.set()
        #グラフの描写
        title = "boxplot_graph"
        plt.title(title)
        graph = sns.boxplot(x = "species", y = "length", data = data, color = "gray")
        # 表示
        canvas_view = f.image_graph(graph, title)
        canvas_view.view()
    # ヴァイオリンプロット:箱の代わりにカーネル密度推定の結果を用いたもの
    def violinplot(data):
        # グラフデザインの指定
        sns.set()
        #グラフの描写
        title = "violinplot_graph"
        plt.title(title)
        graph = sns.violinplot(x="species", y="length", data=data, color="gray")
        canvas_view = f.image_graph(graph, title)
        canvas_view.view()
    # 棒グラフ
    def barplot(data):
        # グラフデザインの指定
        sns.set()
        #グラフの描写
        title = "barplot_graph"
        plt.title(title)
        graph = sns.barplot(x="species", y="length", data=data, color="gray")
        #表示
        canvas_view = f.image_graph(graph, title)
        canvas_view.view()
    # 散布図:数値データ×数値データ
    def jointplot(data):
        # グラフデザインの指定
        sns.set()
        #グラフの描写
        title = "jointplot_graph"
        plt.title(title)
        graph = sns.jointplot(x="x", y="y", data=data, color="black")
        #表示
        canvas_view = f.image_graph(graph, title)
        canvas_view.view()
    # 3変数以上のデータを図示(ペアプロット)
    def groupdata_stat():
        # データの準備:seaborn組み込みのアヤメ(辞書データ)を使用
        iris = sns.load_dataset("iris")
        #実行別に分割
        def iris_conf():
            print(iris.head(n = 3))
            #アヤメのデータの理解
            horizon = "---------------------------"
            print(horizon)
            print(iris.groupby("species").mean()) # 特徴別の平均値を取得
        def iris_graph(data):
            #グラフデザインの指定
            sns.set()
            #グラフの描写
            title = "iris_pairplot_graph"
            plt.title(title)
            graph = sns.pairplot(data, hue="species", palette="gray") # hueはカテゴリ型データの列名を指定する
            #表示
            canvas_view = f.image_graph(graph, title)
            canvas_view.view()

        #実行
        # iris_conf()
        iris_graph(iris)

    # 実行
    # lineplot()
    # lineplot_seaborn()
    # histogram()
    # bins_1_design()
    # kernel_design()
    # multi_line(base_list)
    # boxplot(base_list)
    # violinplot(base_list)
    # barplot(base_list)
    # jointplot(base_list2)
    groupdata_stat()

main()
