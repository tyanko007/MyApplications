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
# モデルによる予測
yosoku = lm_model.predict()
# 引数を指定しての予測も可能
yosoku_dl = lm_model.predict({"temperature":[0]})
# 計算式の確認(気温が２０度の時の売り上げ期待値)
yosoku_res1 = lm_model.predict(pd.DataFrame({"temperature":[20]}))
b0 = lm_model.params[0]
b1 = lm_model.params[1]
temp = 20
yosoku_res2 = b0 + b1 * temp
# 残差の取得
resid = lm_model.resid
# 決定係数の計算(データへのモデルへの当てはまり具合)
mu = sp.mean(MODEL.beer)
y = MODEL.beer
yhat = lm_model.predict()
r_squared = sp.sum((yhat - mu)**2) / sp.sum((y - mu)**2)
r_squared_c = lm_model.rsquared # こっちでも取得可能
#--- end

#--- valiable value check field
var_check_flag = True

if var_check_flag == True:
    print("----- 決定係数の確認 -----")
    print("平均 >>>" + str(mu) + ", 実測値 >>>" + str(y) + ", 予測値 >>>" + str(yhat))
    print("決定係数 >>>" + str(r_squared_c))

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
# 回帰直線の図示
graph_2 = sns.lmplot(x = "temperature", y = "beer", data = MODEL, scatter_kws={"color": "black"}, line_kws={"color": "black"})
graph_2_nm = "kaikityokusen model"
# graph_plot(gh_title=graph_2_nm, gh_source=graph_2)
#--- end
