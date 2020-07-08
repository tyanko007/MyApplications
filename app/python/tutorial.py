#coding: utf-8

# ---- how to writing code ----
# 1. 変数は簡潔に
# 2. 表現方法別に関数にして実行したい物のみ指定
# 3. 説明文は必ずつける
# ---- end ----

import random
import time

def main():
    # 四則演算
    def calc():
        print("1+1=" + str(1+1)) # 足し算
        print("5-2=" + str(5-2)) # 引き算
        print("2*3=" + str(5*2)) # 掛け算
        print("2**3=" + str(2**3)) # 累乗
        print("6/3=" + str(6/3)) # 割り算(小数点あり)
        print("7//3=" + str(7//3)) # 割り算(小数点なし)
    #データ型
    def data_type():
        print("A = " + str(type("A"))) # 文字列型の検査
        print("1 = " + str(type(1))) # 数値型の検査
        print("2.7 = " + str(type(2.7))) # 不動小数点型の検査
        print("Ture = " + str(type(True))) # ブール型の検査
    #比較演算子
    def comparison():
        print("1 > 0.89 = " + str(1>0.89)) # 演算結果が正しい場合
        print("3 > 2 = " + str(3>2)) # 演算結果が正しくない場合
        print("etc...")
        print(">= は以上")
        print("<= は以下")
        print("== は等しい")
        print("!= は等しくない")
    #変数
    def variable():
        num1 = 2 # 変数num1に値を格納
        num2 = 1 # 変数num2に値の格納
        res = "数の和は" # 変数resへ文字列の格納
        print(str(num1) + "と" + str(num2) + res + str(num1+num2))
    # 関数
    def define():
        #戻り値なしの関数
        def none_return():
            print("none_return関数が実行されました")
            print("stady python programing")

        #戻り値ありの関数
        def done_return():
            # print("done_return関数が実行されました")
            print("あなたは兵士の剣を手に入れました")
            sword = "兵士の剣"
            return sword
        #引数ありの関数
        def argument(num):
            print("あなたは" + str(num) + "のダメージを与えました")
        #複合
        def story(name, age, job):
            print("ようこそ" + your_name + "さん")
            print("あなたは" + your_age + "才の" + your_job + "なのですね")
            print("冒険を始めるためにこれを差し上げます")
            weapon = done_return()
            print("スライムに攻撃をしてみてください")
            run = input("行動を右から選び入力してください [戦う] >>")
            print("あなたは" + run + "を選択しました")
            print(weapon + "で攻撃")
            damege = random.randrange(10)
            argument(damege)


        #none_return()
        your_name = input("冒険者の名前を入力してください >>")
        your_age = input("年齢を決めてください >>")
        your_job = input("職業を右から選び入力してください [戦士, 魔法使い] >>")
        story(your_name, your_age, your_job) # 冒険の始まりです

    #クラスとインスタンス
    def tclass():
        #---- sample code on study book ----
        class Sample_Class: # クラスの宣言
            def __init__(self, data1, data2): # 関数１
                self.data1 = data1
                self.data2 = data2

            def method2(self):
                return(self.data1 + self.data2) # 関数２

        sample_instance = Sample_Class(data1 = 2, data2 = 3) # インスタンスの作成

        print(sample_instance.data1)
        print(sample_instance.data2)
        print(sample_instance.method2())
        #---- end ----

    #if文を使った条件分岐
    def study_if():
        #only if
        tax = input("¥100の消費税10%はいくら? [10] >>")
        if(int(tax) == 10):
            print("正解")

        #if and else
        tax2 = input("¥300の消費税8%はいくら? >>")
        if(int(tax2) == 24):
            print("正解")
        else:
            print("不正解")

        #if and else and elif
        rack = random.randrange(10)
        if(rack <= 1):
            print("今日の運勢は大凶です")
        elif(rack > 1 and rack <= 8):
            print("あなたの運勢は吉です")
        else:
            print("あなたの運勢は大吉です")
    #for, whileを使った繰り返し構文
    def study_for():
        #print(range(0, 10))
        #for i in range(0,10):
            #print(i)

        #簡単なブラックジャックゲーム
        # 必要な変数の定義
        clear = 21
        result = 0
        flag = False

        # ゲーム開始
        print("さぁブラックジャックを始めましょう")
        def judge(score): # 結果発表関数
            if(score == clear):
                print("あなたのスコアは...")
                time.sleep(3)
                print(str(score) + "です！")
                print("ブラックジャック！！成功です！！！")
            else:
                print("あなたのスコアは...")
                time.sleep(3)
                print(str(score) + "です！")
                print("残念でしたm9")

        while(flag == False): # 擬似サイコロ振り動作
            coll = input("サイコロを振りますか? [yes : no] >>")
            if(coll == "yes" and result < 21):
                si = random.randint(1,6)
                result += si
                #print("現在の点数は..." + str(result) + "です") # debug code
            else:
                flag = True
        judge(result)

    # 実行関数まとめ
    #calc()
    #data_type()
    #comparison()
    #variable()
    #define()
    #tclass()
    #study_if()
    study_for()

main()
