# coding: utf-8

# 必要な関数の取り込み
import pandas as pd
import scipy as sp

def main():

    # base_variable
    base_list = pd.read_csv("./sts2_csv.csv")
    base_list2 = pd.read_csv("./sts2-2_csv.csv")
    base_list3 = pd.read_csv("./sts2-3_csv.csv")
    # print(base_list) # debug_code
    # print(base_list2) # debug_code
    # print(base_list3.index[1:5]) # debug_code
    # 統計コードの応用
    def application_statistics(data, data2):
        #グループごとの統計量
        group = data.groupby("species")
        print("特徴別の平均で分類")
        print(group.mean())
        print("標準偏差も可能")
        print(group.std(ddof=1))
        print("まとめて表示")
        print(group.describe())
        print("----------------------")

        #クロス集計処理
        cross = pd.pivot_table(
            data = data2,
            values = "sales",
            aggfunc = "sum",
            index = "store",
            columns = "color"
        )
        print("クロス集計表(値 = sales, 分類(縦) = store, 分類(横) = color)")
        print(cross)

    # 共分散
    def cov_statistics(data):
        #共分散の計算式 = Sxy/N, Sxy/N-1
        # prepare
        X = data["x"]
        Y = data["y"]
        size = len(data) # サンプルサイズ
        mu_x = sp.mean(X) # 平均値
        mu_y = sp.mean(Y)

        # run
        cov_sample = sum((X - mu_x)*(Y - mu_y)) / size
        print("共分散(母数) >> " + str(f'{cov_sample:.3f}'))
        cov = sum((X - mu_x)*(Y - mu_y)) / (size - 1)
        print("共分散(標本) >> " + str(f'{cov:.3f}'))
        print("分散共分散行列(scipy)母数 >> " + str(sp.cov(X, Y, ddof=0)))
        print("分散共分散行列(scipy)標本 >> " + str(sp.cov(X, Y, ddof=1)))

    # ピアソンの積率相関係数
    def rho_statistics(data):
        # prepare
        X = data["x"]
        Y = data["y"]

        # 分散
        sigma_x = sp.var(X, ddof=1)
        sigma_y = sp.var(Y, ddof=1)
        cov = sp.cov(X, Y, ddof=1)
        # 相関係数
        rho = cov / sp.sqrt(sigma_x * sigma_y)
        print(rho)
        print(sp.corrcoef(X, Y))


    # 実行
    # application_statistics(base_list, base_list2)
    # cov_statistics(base_list3)
    rho_statistics(base_list3)

main()
