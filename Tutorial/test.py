from big_ol_pile_of_manim_imports import *

class EasyScence(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.wait(2)
        circ = Circle()
        tri= Triangle()

        self.add(tri)

        self.play(Transform(tri,circ))
        tex= TexMobject(r"Hello World \alpha")
        tex.next_to(circ,DOWN)
        self.play(Transform(dot, tex))

        self.wait(5)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -p  -a " + module_name
    os.system(command)