# coding: utf-8
from matplotlib import pyplot
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
from scipy import stats
import scipy as sp

class image_graph:
    def __init__(self, dt_graph, dt_name):
        self.gp = dt_graph
        self.nm = dt_name

    def view(self):

        print("Content-Type: text/html\n")
        print("""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>python_graph_view</title>
        </head>
        <body>
        <h1>グラフの描写</h1>
        <div id="graph">
        """)
        pyplot.savefig("/root/app/img/" + self.nm + ".png")
        print("<img src='./../img/" + self.nm + ".png'>")
        print("""
        </div>
        </body>
        </html>
        """)

    # when add option web content, your self
    def view_option(self, me, st, va):
        # encode to html
        print("Content-Type: text/html\n")
        # html header and fotter code
        def header():
            print("""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title>python_graph_view_enterprise</title>
                </head>
                <body>
                    <h1 style="text-align: center;">グラフ詳細</h1>
            """)
        def footer():
            print("""
                    <hr>
                    <small style="text-align: center;">&copy; 2020 tyanko personal.</small>
                </body>
                </html>
            """)
        # variable jadge null or value
        def var_null(var):
            if not var:
                return 0
            else:
                return 1
        # args data on web page
        header()
        print("<div id='graph_view'>")
        pyplot.savefig("/root/app/img/" + self.nm + ".png")
        print("<img src='./../img/" + self.nm + ".png'>")
        print("</div><div id='graph_info'>")
        # confirm graph status
        me_f = var_null(me)
        if me_f == 1:
            print("<p>標本の平均 >> " + str(f'{me:.3f}') + "</p>")
        st_f = var_null(st)
        if st_f == 1:
            print("<p>標本の標準偏差 >> " + str(f'{st:.3f}') + "</p>")
        va_f = var_null(va)
        if va_f == 1:
            print("<p>標本の分散 >> " + str(f'{va:.3f}') + "</p>")
        print("</div>")
        footer()


    # ****** end ******

    def canvas_print(self):

        fix, ig = pyplot.subplots()

        ig.set_title(self.nm)
        ig = self.gp

        canvas = FigureCanvasAgg(fix)
        canvas.print_png("/root/app/img/" + self.nm + ".png")

        img_path = "<img src='./../img/" + self.nm + ".png'"
        view(img_path)

# the population data create auto calclation class
class sigma_calc:

    def __init__(self, size, n_trial):
        self.size = size
        self.n_trial = n_trial
        # avarage=4, standard deviation=0.8
        self.pop = stats.norm(loc=4, scale=0.8)

    def create_source(self):
        box = np.zeros(self.n_trial)
        for i in range(0, self.n_trial):
            b = self.pop.rvs(size=self.size)
            box[i] = sp.mean(b)
        return box

    def create_source_var(self):
        box = np.zeros(self.n_trial)
        for i in range(0, self.n_trial):
            b = self.pop.rvs(size=self.size)
            box[i] = sp.var(b, ddof=1)
        return box

# adjustment list data format
class list_format:
    # data init
    def __init__(self, lv, data):
        self.l = lv
        self.d = data

    def format(self):
        # aling data
        if self.l == 1:
            sub = np.zeros(len(self.d))
            for i in range(0, len(self.d)):
                sub[i] = f'{self.d[i]:.3f}'
            return sub
        elif self.l == 2:
            # sub = np.zeros(self.l)
            sub = []
            for y in range(0, self.l):
                sub.append(np.zeros(len(self.d[y])))
                for i in range(0, len(self.d[y])):
                    sub[y][i] = f'{self.d[y][i]:.3f}'
            return sub
        else:
            return 0
