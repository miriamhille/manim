from big_ol_pile_of_manim_imports import *
import numpy as np
from active_projects.eop.reusables.histograms import *
##Histogram like this:
## 0   2    2     1
#0   1    2    3    4


class MinimalHist(Scene):
    def construct(self):

        values= [1,2,2,1,3]
        val = np.histogram(values, bins=[i for i in np.arange(0, 10)])
        hist= Histogram(val[1],val[0], mode= "posts")
        self.add(hist)
        self.wait(0.2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -a -p -s  " + module_name
    os.system(command)