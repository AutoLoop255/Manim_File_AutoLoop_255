from manimlib.imports import *

def arr(x,y,z):
    return np.array([x,y,z])

class Main_01(Scene):
    def construct(self):
        # construct
        text10 = TextMobject(
            "0 1 2 3 4 5 6 7 8 9",
            fill_color=["#2af598","#72afd3"],
            stroke_color=["#2af598","#72afd3"],
            height=0.5
            )

        text_ten = TextMobject(
            "十",
            fill_color=["#00c6fb","#005bea"],
            stroke_color=["#00c6fb","#005bea"],
            )
        text_ten.move_to(arr(-2,0,0))
        text_ten.scale(1.5)

        text_10 = TextMobject(
            "10",
            fill_color=["#00c6fb","#005bea"],
            stroke_color=["#00c6fb","#005bea"],
            )
        text_10.move_to(arr(2,0,0))
        text_10.scale(1.5)

        text_or = TextMobject(
            "或",
            fill_color=["#6a85b6","#bac8e0"],
            stroke_color=["#6a85b6","#bac8e0"],
            height=0.5,
            )

        text_Question = TextMobject(
            "?",
            fill_color=["#00c6fb","#005bea"],
            stroke_color=["#00c6fb","#005bea"],
            height=0.7,
            )
        group_10or10 = VGroup(text_ten,text_10,text_or)
        # setting
        # .set_color_by_gradient(["#00c6fb","#005bea"])

        # play
        # 生成1到10并展现到观众眼前
        self.play(Write(text10))
        self.play(text10.scale,1.5,text10.move_to,arr(0,-2.2,0))
        self.wait(1)

        # 生成 10或10 字符串 并向上移动
        self.play(Write(text_ten))
        self.play(text_ten.scale,1.5)
        self.play(Write(text_or))
        self.play(Write(text_10))
        self.play(text_10.scale,1.5)
        self.play(group_10or10.move_to,arr(0,0.8,0))
        self.wait(1)
        # ShowCreationThenDestructionAround 外框强调某一数字
        # ShowPassingFlashAround
        # SurroundingRectangle
        self.play(ShowCreationThenDestruction(SurroundingRectangle(text10,color=BLUE),time_width=0.1))
        self.wait(1)
        text_Question.move_to(group_10or10)
        self.play(Transform(group_10or10,text_Question))
        self.wait(1)
        
        self.play(group_10or10.next_to,text10)
        self.wait(1)
        self.play(FadeOut(group_10or10))
        self.wait(1)





