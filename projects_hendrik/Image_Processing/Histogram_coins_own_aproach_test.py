from big_ol_pile_of_manim_imports import *
from active_projects.eop.reusable_imports import *
from coins_in_array import *
class Images(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 3,
        "function_color": RED,
        "axes_color": GREEN
    }


    def construct(self):

        ###Histogram poisson
        shot_noise = np.random.poisson(3, (34))
        val = np.histogram(shot_noise,bins=[i for i in np.arange(0,10)])
        print("HIIII",val)
        self.setup_axes()

        dot = Dot()
        dot.move_to(self.coords_to_point(0, 0))
        self.add(dot)
        self.wait(0.2)





if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -p  -s -c '#2B2B2B' -a --leave_progress_bars " + module_name
    os.system(command)












