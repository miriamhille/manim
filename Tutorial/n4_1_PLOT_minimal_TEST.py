from big_ol_pile_of_manim_imports import *

class PlotFunctions(GraphScene):
    def construct(self):


        self.setup_axes(animate=True)
        dot=Dot()
        dot.move_to(self.coords_to_point(0, 0))
        self.my_func = lambda x: np.sin(x)
        func_graph=self.get_graph(self.my_func)
        self.add(func_graph)
        self.add(dot)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -pl -s --leave_progress_bars -a " + module_name
    os.system(command)

