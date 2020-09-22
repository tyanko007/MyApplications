#! /usr/bin/env python3
# coding: utf-8

### t検定の実装 ###

# 必要なライブラリの準備
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats as sts
# グラフの描写用
from matplotlib import pyplot as plt
import seaborn as sns
# 自分用
import class_module as f

# グラフデザインの指定
sns.set()

def main():
    base_data = pd.read_csv("sts9_csv.csv")["weight"]

    # t検定 ~ 1 ~ t値の計算
    def t_kentei_tVal(junk_food):
        # 帰無仮説:スナック菓子の内容量は50gである
        # 対立仮説:スナック菓子の内容量は50gではない
        mu = sp.mean(junk_food) # 平均
        df = len(junk_food) - 1 # 自由度
        sigma = sp.std(junk_food, ddof=1)
        se = sigma / sp.sqrt(len(junk_food))
        t_value = (mu - 50) / se
        print("公式に当てはめた場合 >>> " + str(t_value))
        return t_value
    # t検定 ~ 2 ~ p値の計算
    def t_kentei_pVal(junk_food, t_value):
        # p値の計算方法: p(1-a) * 2(両側検定のため)
        df = len(junk_food) - 1
        alpha = sts.t.cdf(t_value, df=df)
        p_value = (1 - alpha) * 2
        print("公式に当てはめた結果 >>> " + str(p_value))
        # より簡単にt値、p値を算出する方法
        print("関数を当てはめた場合(ttest_1smap) >>> " + str(sts.ttest_1samp(a = junk_food, popmean=50)))
        return p_value
    # p値を求めるシュミレーション
    def pVal_sumiration(junk_food, t_value):
        # 試行回数は５００００回、比較対象値は５０
        t_value_array = np.zeros(50000)
        sigma = sp.std(junk_food, ddof=1)
        size = len(junk_food)
        dist = sts.norm(loc=50, scale=sigma)

        # t値のシュミレーション
        np.random.seed(1)
        for i in range(0, 50000):
            sample = dist.rvs(size=size)
            sample_mean = sp.mean(sample)
            sample_std = sp.std(sample, ddof=1)
            sample_se = sample_std / sp.sqrt(size)
            t_value_array[i] = (sample_mean - 50) / sample_se
        # p値のシュミレーション
        p_sval = (sum(t_value_array > t_value) / 50000) * 2
        print("50000回のt値がt標本値を超えた確率 >>> " + str(p_sval))

    # 実行
    tVal = t_kentei_tVal(base_data)
    pVal = t_kentei_pVal(base_data, tVal)
    pVal_sumiration(base_data, tVal)
    # デバッグ
    def debug():
        print("This space is debug zone.")
    # debug()
main()
