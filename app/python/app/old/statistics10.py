#! /usr/bin/env python3
# coding: utf-8

### 2変量のデータに対するt検定

## 必要なモジュールの読み込み
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats as sts
## グラフの描写用ライブラリ
from matplotlib import pyplot as plt
import seaborn as sns
## 自分用
import class_module as f

def main():
    # ベースデータの準備
    personal_report = pd.read_csv("sts10_csv.csv")

    # 対応のあるt検定
    def valid_t_kentei(data):
        # beforeとafterに分類
        before = data.query('medicine == "before"')["body_temperature"]
        after = data.query('medicine == "after"')["body_temperature"]
        # アレイ型に変換
        before = np.array(before)
        after = np.array(after)
        # 差の計算
        sa = before - after
        print(sa)
        # 差の平均値が0と異なるかどうか
        res_1 = sts.ttest_1samp(sa, 0)
        print(res_1)
        # 簡単な計算方法
        res_2 = sts.ttest_rel(before, after)
        print(res_2)

    # 対応のないt検定
    def invalid_t_kentei(data):
        # beforeとafterに分類
        before = data.query('medicine == "before"')["body_temperature"]
        after = data.query('medicine == "after"')["body_temperature"]
        # アレイ型に変換
        before = np.array(before)
        after = np.array(after)
        # 平均値の計算
        mean_bef = sp.mean(before)
        mean_aft = sp.mean(after)
        # 不偏分散の計算
        sigma_bef = sp.var(before, ddof=1)
        sigma_aft = sp.var(after, ddof=1)
        # サンプルサイズ
        m = len(before)
        n = len(after)
        # t値
        t_value = (mean_aft - mean_bef) / sp.sqrt((sigma_aft / m) + (sigma_bef / n))
        print(f'{t_value:.3f}')
        # 簡単な計算方法
        t_value_util = sts.ttest_ind(after, before, equal_var=False)
        print(t_value_util)

    #実行
    # valid_t_kentei(personal_report)
    invalid_t_kentei(personal_report)

    def debug(e):
        print(e)
    # debug(personal_report)

main()
