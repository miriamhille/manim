from big_ol_pile_of_manim_imports import *

class Szene1(Scene):
    def construct(self):
        tex= TextMobject("Warum geht die eine Lampe kaputt, die andere bleibt heile?")
        self.add(tex)
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -a -s -t -p  " + module_name
    os.system(command)