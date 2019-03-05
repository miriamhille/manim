

from big_ol_pile_of_manim_imports import *

class Images(Scene):

    def circ(self,img, radius, circle_opacity):
        n, m = np.shape(img)
        for j in range(0, n):
            for k in range(0, m):
                if (j - n / 2) ** 2 + (k - m / 2) ** 2 < radius ** 2:
                    img[j, k] = img[j, k] * (1-circle_opacity)
        return img

    def create_poission_noise_ball(self, num_photons=100):
        num_pixels = 512
        img_origin = np.ones((num_pixels, num_pixels))
        shot_noise_img = num_photons * img_origin
        shot_noise_img = self.circ(shot_noise_img, 75, circle_opacity= 0.01)
        shot_noise = np.random.poisson(shot_noise_img, (num_pixels, num_pixels))
        stretched_img=self.IPcontraststretch(shot_noise)
        return stretched_img

    def IPcontraststretch(self,image):
        image = np.asarray(image)
        M = image.max()
        m = image.min()
        stretched_img = (256 - 1) / (M - m) * (image - m)
        return np.uint8(stretched_img)

    def construct(self):
        seed = 42 # initilize the randomness for the poisson noise
        np.random.RandomState(seed)
        poission_With_one_pixel=[]
        text_for_the_images= []
        for photons_val in np.arange(3,10,1):
             poission_With_one_pixel.append(self.create_poission_noise_ball(num_photons=2))
             text_for_the_images.append(str(photons_val))
        poission_With_one_pixel_ALL= [ImageMobject(img_a).scale(2.5) for img_a in poission_With_one_pixel]

        for PLOT,text in zip(poission_With_one_pixel_ALL,text_for_the_images):
            self.clear()
            self.add(PLOT)
            print(text)
            t_2= TexMobject(r"\text{Rate of incident photons: }" + text +  r"\, \frac{\text{photon}}{s}")
            t_2.next_to(PLOT,DOWN)
            self.add(t_2)
            self.wait(0.1)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -pl   -a --leave_progress_bars " + module_name
    os.system(command)









