#! /usr/bin/env python3
# coding: utf-8

# must packages
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import imgfunc as f

plt.figure()

def main():

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

    def multi_line():
        list_data = pd.read_csv("/root/app/sts3_csv.csv")

        # print(list_data.groupby("species").describe()) # データの情報の確認

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

    # 実行
    # lineplot()
    # lineplot_seaborn()
    # histogram()
    # bins_1_design()
    # kernel_design()
    multi_line()


main()
