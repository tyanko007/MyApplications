#! /usr/bin/env python3
# coding: utf-8

### 連続型の説明変数を一つもつモデル_単回帰

#--- library zone
# 数式関連
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats as sts

# グラフ描写関連
from matplotlib import pyplot as plt
import seaborn as sns

# 統計モデルを推定するライブラリ
import statsmodels.formula.api as smf
import statsmodels.api as sm

# 自分用ライブラリ
import class_module as f
#--- end

#--- valiavle definition
sns.set()
MODEL = pd.read_csv("model_samp1.csv")
# モデルを決めて構築する
# 構築するモデルは ビールの売り上げモデル ~ N(b0, b1 * 気温, sigma^2)
lm_model = smf.ols(formula = "beer ~ temperature", data = MODEL).fit()
# nullモデルのAICを比較
null_model = smf.ols(formula = "beer ~ 1", data = MODEL).fit()
# aicの計算
llf = lm_model.llf # 対数尤度
df = lm_model.df_model # 推定されたパラメタの値はわからないが説明変数の数ならわかる
aic = -2*(llf - (df + 1))
#--- end

#--- valiable value check field
var_check_flag = True

if var_check_flag == True:
    print("aic(手計算)の情報は以下")
    print(aic)
    print(type(aic))
#--- end

#--- create graph image field
def graph_plot(gh_title, gh_source):
    # tmp_me = input("平均値(特になければ空でOK) >>> ")
    # tmp_st = input("標準偏差(特になければ空でOK) >>> ")
    # tmp_va = input("分散(特になければ空でOK) >>> ")
    plt.title(gh_title)
    canvas = f.image_graph(dt_name=gh_title, dt_graph=gh_source)
    canvas.view_option(me="", st="", va="")
#--- end

#--- model field

#　純粋にビールと気温の売り上げデータを散布図としてグラフ化
graph_1 = sns.jointplot(x = "temperature", y = "beer", data = MODEL, color = "black") # データフレームを図示
graph_1_nm = "sample data frame"
# graph_plot(gh_title=graph_1_nm, gh_source=graph_1)
#--- end
