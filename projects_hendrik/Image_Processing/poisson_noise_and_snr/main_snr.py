from big_ol_pile_of_manim_imports import *
from active_projects.eop.reusables.histograms import *

class poisson_and_snr(Scene):
    def construct(self):
        img= np.ones((32,32))+33
        img= np.random.poisson(img, (32,32) )

        max = 256
        val = np.histogram(img, bins=[i for i in np.arange(0, max + 1)])
        hist = Image_Histogram(val[1], val[0], x_scale=4 / max, y_scale=3/val[0].max())
        self.add(hist)
        self.wait(2)

if __name__ == "__main__": 
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -a -p  " + module_name
    os.system(command) 