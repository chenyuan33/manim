# -*- coding: utf-8 -*-
from manim import *


class Test(Scene):
    def construct(self):
        banner = ManimBanner()
        banner.shift(UP * 0.5)
        self.play(banner.create(), run_time=1)
        self.play(banner.animate.scale(0.3), run_time=0.5)
        self.play(banner.expand(), run_time=1)

        t_zh = Text("测试中文能否显示").next_to(banner, DOWN * 2)
        tex = Tex(r"$\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$").next_to(
            t_zh, DOWN)
        self.play(Write(t_zh), run_time=0.1)
        self.play(Write(tex), run_time=0.1)
        self.wait(0.1)
        self.play(Unwrite(banner), Unwrite(t_zh), Unwrite(tex), run_time=0.1)

        dot_group = VGroup()

        for i in range(-2, 3):
            for j in range(1, -2, -1):
                dot = Dot(color=BLUE).shift(i * RIGHT + j * UP)
                self.play(Create(dot), run_time=0.1)
                dot_group.add(dot)

        line_group = VGroup()
        for i in dot_group:
            for j in dot_group:
                if i.get_center()[0] > j.get_center()[0] or i.get_center()[0] == j.get_center()[0] and i.get_center()[1] > j.get_center()[1]:
                    l = Line(i.get_center(), j.get_center(), color=RED)
                    self.play(Create(l), run_time=0.1)
                    line_group.add(l)
        self.wait(0.1)
        self.play(FadeOut(line_group), run_time=0.1)

        arrow_group = VGroup()
        for i in range(-2, 3):
            l = Arrow([i, 1, 0], [i, -1, 0], color=RED)
            self.play(Create(l), run_time=0.1)
            arrow_group.add(l)
        self.wait(0.1)

        DashedLine_group = VGroup()
        for j in range(1, -2, -1):
            l = DashedLine([-2, j, 0], [2, j, 0], color=YELLOW)
            self.play(Create(l), run_time=0.1)
            DashedLine_group.add(l)
        self.wait(0.1)
        self.play(FadeOut(arrow_group), FadeOut(
            DashedLine_group), run_time=0.1)

        c = Circle(radius=1, color=GREEN)
        self.play(Create(c), run_time=0.1)
        self.wait(0.1)
        self.play(FadeOut(c), run_time=0.1)

        c = Ellipse(width=4, height=2, color=GREEN)
        self.play(Create(c), run_time=0.1)
        self.wait(0.1)
        self.play(FadeOut(c), run_time=0.1)

        self.play(dot_group.animate.shift(UP), run_time=0.25)
        self.play(dot_group.animate.shift(RIGHT), run_time=0.25)
        self.play(dot_group.animate.shift(DOWN * 2), run_time=0.5)
        self.play(dot_group.animate.shift(LEFT * 2), run_time=0.5)
        self.play(dot_group.animate.shift(UP * 2), run_time=0.5)
        self.play(dot_group.animate.shift(RIGHT), run_time=0.25)
        self.play(dot_group.animate.shift(DOWN), run_time=0.25)
        self.play(Rotate(dot_group, angle=PI/2), run_time=0.5)
        self.play(dot_group.animate.shift(UP), run_time=0.25)
        self.play(Rotate(dot_group, angle=PI*2,
                  about_point=ORIGIN), run_time=2)

        rect = Rectangle(width=2, height=1, color=BLUE)
        self.play(ReplacementTransform(dot_group, rect), run_time=0.5)
        self.wait(0.1)

        numl = NumberLine([-5, 6, 1], length=11,
                          include_numbers=True, include_tip=True)
        self.play(ReplacementTransform(rect, numl), run_time=0.5)
        self.wait(0.1)
        p = Dot(numl.n2p(-5), color=RED)
        self.play(Create(p), run_time=0.1)
        n = Tex('-5')
        self.play(Write(n), run_time=0.1)
        n.add_updater(lambda x: x.become(Tex(
            str(round(numl.p2n(p.get_center()), 2))
            if round(numl.p2n(p.get_center()), 2) != round(numl.p2n(p.get_center()))
            else str(round(numl.p2n(p.get_center()))).split('.')[0]
        ).next_to(p, UP * 0.2)))
        self.play(p.animate.move_to(numl.n2p(5)), run_time=1)
        self.play(p.animate.move_to(numl.n2p(-5)), run_time=1)
        self.play(p.animate.move_to(numl.n2p(5)), run_time=1)
        self.play(p.animate.move_to(numl.n2p(-5)), run_time=1)
        self.play(FadeOut(p), FadeOut(n), run_time=0.1)

        a = Axes(x_range=[-5, 5, 1], y_range=[-1, 5, 1], x_length=10, y_length=6, axis_config={"include_numbers": True})
        self.play(FadeOut(numl), run_time=0.5)
        self.play(Create(a), run_time=0.5)
        f1 = a.plot(lambda x: np.sin(x), x_range=[-5, 5, 0.01], color=RED)
        s1 = Tex(r"$y=\sin(x)$", color=RED)
        s1.move_to(a.c2p(6, np.sin(5)))
        self.play(Create(f1), Create(s1), run_time=0.5)
        f2 = a.plot(lambda x: np.cos(x), x_range=[-5, 5, 0.01], color=GREEN)
        s2 = Tex(r"$y=\cos(x)$", color=GREEN)
        s2.move_to(a.c2p(6, np.cos(5)))
        self.play(Create(f2), Create(s2), run_time=0.5)
        f3 = a.plot(lambda x: np.sin(x) + np.cos(x), x_range=[-5, 5, 0.01], color=BLUE)
        s3 = Tex(r"$y=\sin(x)+\cos(x)$", color=BLUE)
        s3.move_to(a.c2p(6, np.sin(5) + np.cos(5)))
        self.play(ReplacementTransform(VGroup(f1, f2), f3), ReplacementTransform(VGroup(s1, s2), s3), run_time=0.5)

        self.wait()
