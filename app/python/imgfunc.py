# coding: utf-8
from matplotlib import pyplot
from matplotlib.backends.backend_agg import FigureCanvasAgg

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
        print("<img src='./../img/" + self.nm + ".png'")
        print("""
        </div>
        </body>
        </html>
        """)

    def canvas_print(self):
        
        fix, ig = pyplot.subplots()

        ig.set_title(self.nm)
        ig = self.gp

        canvas = FigureCanvasAgg(fix)
        canvas.print_png("/root/app/img/" + self.nm + ".png")

        img_path = "<img src='./../img/" + self.nm + ".png'"
        view(img_path)
