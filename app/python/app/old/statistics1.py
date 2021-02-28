# coding: utf-8

# 必要な関数の追加
import numpy as np
import scipy as sp
from scipy import stats # scipyの中のより統計分析に特化した関数の追加

# 表示される桁数の固定方法
# ---- 桁数いじり一覧 ----
#   1-1. formatの使用(桁数の固定のため足りない部分は余白として扱われる)
#    ex: print('{:n}'.format(args)')
#        print('{:10}'.format(123.456))
#   1-2. formatを使用した小数点の固定
#     ex: print('{:.nf}'.format(args))
#         print('{:.1f}'.format(123.456)) # 小数点以下四捨五入
#   2-1. f文字列の使用
#    ex: print(f'{args:n}')
#        print(f'{123.456:10}')
#   2-2: f文字列を使用した小数点の固定
#    ex: print(f'{args:.nf}')
#        print(f'{123.456:.1f}')
# ---- end ----

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
    # useful variables
    base_list = np.array([2,3,3,4,4,4,4,5,5,6])
    # ---- end ----
    # 基本統計学
    def basic_statistics(data):
        # データの扱い
        print("サンプルデータ >> " + str(data))
        print("合計 >> " + str(sp.sum(data))) # np.sum(args)やargs.sum()でも同じ結果を得られる
        print("サンプルサイズ >> " + str(len(data)))
        # データの整形
        N = len(data)
        sum_val = sp.sum(data)
        mu = sum_val / N # 平均値の計算
        print("平均 >> " + str(f'{mu:.3f}'))
        print("平均(scipy) >> " + str(f'{sp.mean(mu):.3f}'))
        sigma_dt = (data - mu) ** 2 # (個々のデータ - 平均)^2 のリスト
        sigma = sp.sum(sigma_dt) / N # 分散の計算
        print("分散 >> " + str(f'{sigma:.3f}'))
        print("分散(scipy) >> " + str(f'{sp.var(data, ddof=0):.3f}'))
        sigma2 = sp.sum(sigma_dt) / (N-1) # 不偏分散の計算
        print("不偏分散 >> " + str(f'{sigma2:.3f}'))
        print("不偏分散(scipy) >> " + str(f'{sp.var(data, ddof=1):.3f}'))
        sigma_root = sp.sqrt(sigma2) # 標準偏差の計算
        print("標準偏差 >> " + str(f'{sigma_root:.3f}'))
        print("標準偏差(scipy) >> " + str(f'{sp.std(data, ddof=1):.3f}'))
        standard = (data - mu) / sigma_root # {(個々のデータ - 平均) / 標準偏差}の値
        myins = list_format(standard) # リストを整形するクラスの初期化
        print("標準化 >> " + str(myins.format()))
        print("標準化したデータ : 平均 >> " + str(f'{sp.mean(myins.format()):.3f}' + ", 標準偏差 >> " + str(f'{sp.std(myins.format(), ddof=1):.3f}')))
        # その他の統計量計算
        print("----- その他 -----")
        print("最大値 >> " + str(sp.amax(data)))
        print("最小値 >> " + str(sp.amin(data)))
        print("中央値 >> " + str(sp.median(data)))
        # stats from scipyでの四分位点
        print("----- 四分位点: データを昇順に並び替えた時に下から25%,75%にくる値 -----")
        data2 = np.arange(start=1, stop=10, step=1)
        print("サンプルデータ >> " + str(data2))
        print("下から25%の位置の値 >> " + str(f'{stats.scoreatpercentile(data2, 25):.3f}'))
        print("下から75%の位置の値 >> " + str(f'{stats.scoreatpercentile(data2, 75):.3f}'))

    #実行関数
    basic_statistics(base_list)


main()
