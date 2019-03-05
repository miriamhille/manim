from big_ol_pile_of_manim_imports import *
from active_projects.eop.reusables.histograms import *

class Shapes(Scene):

    def construct(self):
        print("Start")
        hist_y_values= np.array([1,2,3,4])
        grade_hist = Histogram(  np.ones(4), hist_y_values)
        self.add(grade_hist)
        re = Rectangle()
        re.set_color(color=GREEN)
        self.add(re)




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p -s -a " +module_name
    os.system(command)

