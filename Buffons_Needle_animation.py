from manim import *
import numpy as np 

class Buffon(Scene):
    def construct(self):
        L = 10 # length of plane 
        n = 5 # number of vertical partitions of the plane (at least 2)
        N = 500 # number of needles
        length = 1 # length of needle
        ax = Axes(
            x_range = [0, L],
            y_range = [0, L],
            x_length = 7,
            y_length = 7,
            tips = False
        ).shift(2 * LEFT)
        #self.add(ax)

        approx = 0.000
        pi_text = always_redraw(lambda : MathTex(r"\pi \approx {: .3f}".format(approx)).move_to(ax.get_right()).shift(2 * RIGHT))
        self.add(pi_text)


        e1 = Line(ax.c2p(0,0), ax.c2p(L, 0))
        e2 = Line(ax.c2p(L,0), ax.c2p(L,L))
        e3 = Line(ax.c2p(L,L), ax.c2p(0,L))
        e4 = Line(ax.c2p(0,L), ax.c2p(0,0))
        edge = VGroup(e1, e2, e3, e4)
        self.play(Create(edge), run_time = 1)
        self.wait()



        ptt = np.linspace(0, L, n+1)
        ptt1 = ptt[1:-1]

        for x in ptt1:
            l = Line(ax.c2p(x,0), ax.c2p(x, L))
            self.play(Create(l), run_time = 0.5)
        
        succ = 0
        count = 0 
        succt = always_redraw(lambda: MathTex("{}".format(succ)).to_edge(UP + RIGHT))
        self.add(succt)


        np.random.seed(1234)
        for i in range(N):
            count += 1
            coord1 = np.random.uniform(0,L,2)
            theta = np.random.uniform(0, 2*np.pi)
            d1 = Dot(ax.c2p(coord1[0], coord1[1]), color = 'RED', radius= 0.5 * DEFAULT_DOT_RADIUS)
            coord2 = np.array([coord1[0] + length * np.cos(theta), coord1[1] + length * np.sin(theta)])
            d2 = Dot(ax.c2p(coord2[0], coord2[1]))
            l = Line(d1.get_center(), d2.get_center(), color = 'SKYBLUE', fill_opacity = 0.7)
            
            for i in ptt:
                if (coord1[0] <= i and i <= coord2[0]) or (coord1[0] >= i and i >= coord2[0]):
                    succ += 1
                    break
            approx = (2 * length * count) / (ptt1[0] * succ) if succ != 0 else 0
            self.play(FadeIn(l), FadeIn(d1), run_time = 0.1)
            self.add()
        
        self.wait()



        

        



        
