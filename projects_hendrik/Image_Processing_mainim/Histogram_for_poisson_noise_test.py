from big_ol_pile_of_manim_imports import *
from active_projects.eop.reusables.histograms import *

class Images(Scene):
    def construct(self):
        hist_y_values= (1,2,3,4)
        grade_hist = Histogram(
             np.ones(4),
             hist_y_values,
             mode="widths")
        self.add(OutlineableBars())
        self.wait(0.2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -p -s  -a --leave_progress_bars " + module_name
    os.system(command)














