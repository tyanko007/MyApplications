#! /usr/bin/env python3
# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

print ("Content-Type: text/html\n");

plt.figure()

def main():

    def graph_view():

        fig, ax = plt.subplots()

        x = np.array([1,2,3,4,5,6,7,8,9])
        y = np.array([2,3,2,4,5,5,4,2,7])

        ax.plot(x, y, color="black")

        canvas = FigureCanvasAgg(fig)
        buf = io.StringIO()
        canvas.print_png("/root/app/web_test/tmp.png")
        # data = buf.getvalue()

        # response = make_response(data)
        # response.headers['Content-Type'] = 'image/png'
        # response.headers['Content-Length'] = len(data)
        # return response

        print("<img src='./../tmp.png' alt='graph_image'>")

    def html_view():
        print("""
        <head><meta charset='utf-8'><title>htmlグラフ描写</title></head>
        <body><h1>折れ線グラフ</h1><div id='graph'>
        """)
        graph_view()
        print("""
        </div></body>
        """)

    html_view()

main()
