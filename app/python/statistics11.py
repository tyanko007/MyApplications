#! /usr/bin/env python3
# coding: utf-8

### カイ二乗を用いた統計量計算
### 対象データは色のついたボタンごとの押下回数

# 必要なライブラリの読み込み
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats as sts
# グラフの描写用
from matplotlib import pyplot as plt
import seaborn as sns
# 自分用のライブラリ
import class_module as f
# グラフデザインの指定
sns.set()

def main():
    # 基本データ
    color_button_result = pd.read_csv("sts11_csv.csv")

    def calc_p():
        kai2 = 1 - sp.stats.chi2.cdf(x = 6.667, df = 1)
        print("自由度1のカイ二乗分布の類背密度関数を用いたp値 >>> " + str(f'{kai2:.3f}'))

    def cross_table(data):
        cs = pd.pivot_table(
            data = data, values="freq", aggfunc="sum", index="color", columns="click"
        )
        print(cs)
        exe = sp.stats.chi2_contingency(cs, correction=False)
        print("-----")
        print(exe)

    # 実行
    # calc_p()
    cross_table(color_button_result)


main()
