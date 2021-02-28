#! /usr/bin/env python3
# coding: utf-8

#*** 推定 ***

# 必要なライブラリの読み込み
# 計算
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats as sts
# グラフの操作
from matplotlib import pyplot as plt
import seaborn as sns
# 独自のクラスライブラリ
import class_module as f

# グラフデザインの指定
sns.set()

def main():
    # 基本準備
    base_list = pd.read_csv("sts8_csv.csv")["length"]

    # 点推定
    def point_est(fish):
        fish_me = sp.mean(fish)
        print("点推定(標本平均) >>> " + str(f'{fish_me:.3f}'))
        # 分散も同じ要領で行える
        fish_va = sp.var(fish, ddof=1) # 不偏分散
        print("分散推定(標準偏差) >>> " + str(f'{fish_va:.3f}'))

    def section_est(fish):
        # 自由度
        n = len(fish) - 1
        # 平均
        fish_me = sp.mean(fish)
        # 標準誤差
        se = sp.var(fish, ddof=1) / sp.sqrt(len(fish))
        # 信頼区間
        interval = sts.t.interval(alpha=0.95, df=n, loc=fish_me, scale=se)
        print("信頼区間(左：下限推定, 右：上限推定) >>> " + str(interval))

        # 信頼区間をt分布を使って計算
        t_975 = sts.t.ppf(q = 0.975, df = n)
        lower = fish_me - t_975 * se
        upper = fish_me + t_975 * se
        print("下限信頼区間 >> " + f'{lower:.3f}')
        print("上限信頼区間 >> " + f'{upper:.3f}')

        print("標本標準偏差を10倍にした場合の95%の信頼区間")
        se2 = (sp.var(fish, ddof=1) * 10) / sp.sqrt(len(fish))
        interval_10 = sts.t.interval(alpha=0.95, df=n, loc=fish_me, scale=se2)
        print("10倍の信頼区間 >>> " + str(interval_10))
        print("サンプルサイズを10倍にした場合")
        n_10 = (len(fish) * 10) - 1
        se3 = sp.var(fish, ddof=1) / (sp.sqrt(len(fish) * 10))
        interval_10 = sts.t.interval(alpha=0.95, df=n_10, loc=fish_me, scale=se3)
        print("サンプルサイズが10倍の信頼区間 >>> " + str(interval_10))

        # 区間推定の結果の解釈(95%の証明のようなもの)
    def detail_section_est(fish):
        # 変数確認用
        def var_cehck(v):
            print(v)

        # 試行回数は20000回で実施
        res_box = np.zeros(20000, dtype="bool")
        # var_cehck(res_box) # 変数の中身を確認
        # シュミレーションの実行
        np.random.seed(1)
        dist = sts.norm(loc=4, scale=0.8)
        for i in range(0, 20000):
            sample = dist.rvs(size = 10)
            n = len(res_box) - 1
            mu = sp.mean(sample)
            std = sp.std(sample, ddof=1)
            se = std / sp.sqrt(len(sample))
            interval = sts.t.interval(alpha=0.95, df=n, loc=mu, scale=se)
            if(interval[0] <= 4 and interval[1] >= 4):
                res_box[i] = True
        result = sum(res_box) / len(res_box)
        print("信頼区間が母平均(4)を含んでいた割合 >>> " + str(result))


    # 実行
    # point_est(base_list)
    # section_est(base_list)
    detail_section_est(base_list)

    # デバック
    def debug(v):
        print(v)
    # debug(base_list)
main()
