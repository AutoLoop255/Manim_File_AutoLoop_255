from manimlib.imports import *

def arr(x,y,z):
    return np.array([x,y,z])

class lit(Scene):

    def construct(self):
        sq1 = Square(color=BLUE)
        sq2 = Square(color=GREEN)
        cr = Circle(radius=2**0.5,color=YELLOW_A)
        sq2.rotate(PI/4)
        group1 = VGroup(sq1,sq2,cr)
        text01 = TextMobject("AutoLoop\_255",color=BLUE)
        line01 = Line(np.array([-2.5,0,0]),np.array([2.5,0,0]),color=BLUE)
        # move
        group1.scale(0.75)
        self.play(ShowCreation(group1))        
        self.play(
            sq1.rotate,PI/2,sq1.set_color,GREEN,sq1.scale,2,
            sq2.rotate,-PI/2,sq2.set_color,BLUE,sq2.scale,2,
            cr.scale,2**0.5/2,cr.set_color,YELLOW_D,cr.scale,2
            )
        self.play(
            sq1.scale,1.25,sq1.rotate,PI,sq1.set_color,RED,
            sq2.set_opacity,0,sq2.scale,2.5,sq2.rotate,PI,
            cr.set_opacity,0,cr.scale,0.1,cr.rotate,PI
            )
        self.play(sq1.set_color,GREEN,sq1.scale,0.3,sq1.rotate,PI/4,sq1.shift,LEFT*2,sq1.scale,2/3)
        self.play(Write(line01),sq1.shift,RIGHT*4,sq1.rotate,PI,sq1.set_color,BLUE)
        self.play(sq1.shift,LEFT*4,sq1.rotate,PI/4)
        self.play(sq1.shift,RIGHT*2,sq1.set_opacity,0,sq1.scale,0.05,line01.set_opacity,0)
        self.play(ShowCreation(text01))
        self.play(text01.scale,2.0)
        self.play(text01.shift,DOWN)
        self.wait(0.3)
        self.play(text01.set_opacity,0)
        self.wait(1)


        