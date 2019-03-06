from big_ol_pile_of_manim_imports import *

class Test(Scene):
    CONFIG = {
        "radius": DEFAULT_DOT_RADIUS,
        "stroke_width": 0,
        "fill_opacity": 1.0,
        "color": RED
    }
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.wait(2)

if __name__ == "__main__": 
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -a -pl -s " + module_name
    os.system(command) 