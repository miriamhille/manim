from big_ol_pile_of_manim_imports import *
from active_projects.eop.reusable_imports import *
from coins_in_array import *
class Images(Scene):
    def construct(self):
        ###Histogram poisson
        # val = []
        # for i in range(0,3):
        #     shot_noise = np.random.poisson(3, (34))
        #     print(shot_noise)
        #     val.append(np.histogram(shot_noise,bins=[i for i in np.arange(0,10)]))
        ##histogram coins
        FLIP10_ALL = [coins_in_array[0 + k:10 + k] for k in np.arange(0, 50,10)]
        FLIP10_HEADS = np.array([sum(flip10) for flip10 in FLIP10_ALL])
        val = []
        for k,value in enumerate(FLIP10_HEADS):
            elements=FLIP10_HEADS[0:k+1]
            print(elements)
            val.append(np.histogram(elements, bins=[i for i in np.arange(0, 12)]))
        #FLIP100_ALL = [coins_in_array[0 + k:100 + k] for k in range(0, 1)]
        # FLIP100_HEADS = np.array([sum(flip100) for flip100 in FLIP100_ALL])
        # val = []
        # for k,value in enumerate(FLIP100_HEADS):
        #     elements=FLIP100_HEADS[0:k]
        #     print(elements)
        #     val.append(np.histogram(elements, bins=[i for i in np.arange(40, 60,3)]))
        print("HIIII",val)
        x = None
        for ziehung, [hist, bin_edges] in enumerate(val,1):
            y_scale= 1
            if hist.max()>3:
                y_scale=3/hist.max()
            grade_hist = Histogram( bin_edges, hist, mode="posts",y_scale= y_scale)
            NEW_ORIGIN=  DOWN*3+LEFT*5-grade_hist.get_lower_left_point()
            grade_hist.move_to(NEW_ORIGIN)
            if x== None:
                x=grade_hist
            a=TextMobject("Anzahl Muenzen die Kopf zeigen bei 10 Ziehungen")
            b=TextMobject("Ziehung Nummer :" + str(ziehung) )
            a.next_to(TOP, DOWN)
            b.next_to(a,DOWN)
            self.clear()
            self.add(grade_hist, a,b)
            print(hist)
            self.wait(0.2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -p -s  -c '#2B2B2B' -a --leave_progress_bars " + module_name
    os.system(command)












