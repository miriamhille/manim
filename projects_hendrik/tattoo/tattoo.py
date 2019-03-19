from big_ol_pile_of_manim_imports import *

class Tattoo(Scene):
    def gaussian(self,x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    def construct(self):
        func = []
        func.append(ParametricFunction(lambda t:(t,    np.sin(t), 0) , t_min=0, t_max=TAU, color= BLACK))
        for f in func:
            self.add(f.move_to(LEFT))


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -c '#FFCC99' -a -p -s  " + module_name
    os.system(command)

