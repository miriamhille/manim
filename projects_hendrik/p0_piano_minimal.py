from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
    CONFIG = get_piano_sounds()
    def construct(self):
        print(self.CONFIG)
        self.add(Dot())
        self.add_sound(self.C2,gain=-20)
        self.add_sound(self.E2,gain=-20)
        self.add_sound(self.G2,gain=-20)
        self.wait(1)
        self.add_sound(self.C2,gain=-20)
        self.add_sound(self.E2,gain=-20)
        self.add_sound(self.G2,gain=-20)
        self.add_sound(self.Ais2,gain=-20)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -pl   --leave_progress_bars " + module_name
    os.system(command)