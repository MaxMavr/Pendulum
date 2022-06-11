from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.properties import Clock, NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
import math

Window.size = (1200, 750)
Window.clearcolor = (34/255, 31/255, 46/255, 1)

class HLLabel(Label):
    def __init__(self, *args, **kwargs):
        super(HLLabel, self).__init__(*args, **kwargs)
        Window.bind(mouse_pos=self.pos_check)

    def pos_check(self, inst, pos):
        if self.collide_point(*pos):
             self.color = (73/255, 70/255, 102/255, 1)
        else:
             self.color = (46/255, 43/255, 63/255, 1)

class HLButton(Button):
    def __init__(self, *args, **kwargs):
        super(HLButton, self).__init__(*args, **kwargs)
        Window.bind(mouse_pos=self.pos_check)

    def pos_check(self, inst, pos):
        if self.collide_point(*pos):
             self.btn_color_not_pressed = (73/255, 70/255, 102/255, 1)
        else:
             self.btn_color_not_pressed = (46/255, 43/255, 63/255, 1)

class HLCheckBox(CheckBox):
    def __init__(self, *args, **kwargs):
        super(HLCheckBox, self).__init__(*args, **kwargs)
        Window.bind(mouse_pos=self.pos_check)

    def pos_check(self, inst, pos):
        if self.collide_point(*pos):
             self.btn_color_not_pressed = (73/255, 70/255, 102/255, 1)
        else:
             self.btn_color_not_pressed = (46/255, 43/255, 63/255, 1)

pi = math.pi
g = 10

h_check = 0
al_check = 0
m_check = 0


def h_h(l, h):
    alpha = math.acos((l - h) / l)  # a

    return {"alpha": str(alpha)}


def paf_twv(l):
    period = 2 * pi * (l / g) ** 0.5  # T
    angular_frequency = (g / l) ** 0.5  # w
    frequency = angular_frequency / (2 * pi)  # v
    period = str(period)[:5]
    angular_frequency = str(angular_frequency)[:5]
    frequency = str(frequency)[:5]

    return {"period": str(period),
            "angular_frequency": str(angular_frequency),
            "frequency": str(frequency)}


def a_a(l, alpha):
    amplitude = l * math.sin(alpha)  # A
    amplitude = str(amplitude)[:5]

    return {"amplitude": str(amplitude)}


def esb_evvaa(m, l, alpha):
    energy = m * g * (l - math.cos(alpha) * l)  # E
    speed = (2 * g * (l - math.cos(alpha) * l)) ** 0.5  # vv
    boost = g * (math.sin(alpha))  # aa
    energy = str(energy)[:5]
    speed = str(speed)[:5]
    boost = str(boost)[:5]

    return {"energy": str(energy),
            "speed": str(speed),
            "boost": str(boost)}

class Container(GridLayout):
    line_points = ObjectProperty((0, 0, 0, 0))
    grafic_points = ObjectProperty((0, 0))
    number = NumericProperty(1)

    def checkh(self, instance, value):
        global h_check
        if value is True:
            h_check = 1
        else:
            h_check = 0

    def checkal(self, instance, value):
        global al_check
        if value is True:
            al_check = 1
        else:
            al_check = 0

    def checkm(self, instance, value):
        global m_check
        if value is True:
            m_check = 1
        else:
            m_check = 0

    def button_update(self):
        global long
        try:
            long = float(self.long.text)
        except:
            long = 1
            self.long.text = "1"


        paf = paf_twv(long)

        self.period.text = paf.get("period")
        self.angular_frequency.text = paf.get("angular_frequency")
        self.frequency.text = paf.get("frequency")

        if h_check == 1:
            global alpha
            try:
                high = float(self.high.text)
            except:
                high = 0.5
                self.high.text = "0.5"


            h = h_h(long, high)
            alpha = float(h["alpha"])
            a = a_a(long, alpha)

            self.amplitude.text = a.get("amplitude")

        if al_check == 1:
            try:
                alpha = float(self.alpha.text)
                alpha = (alpha * pi) / 180
            except:
                alpha = 1
                self.alpha.text = "1"

            a = a_a(long, alpha)

            self.amplitude.text = a.get("amplitude")

        if m_check == 1:
            try:
                mass = float(self.mass.text)
            except:
                mass = 1
                self.mass.text = "1"

            esb = esb_evvaa(mass, long, alpha)

            self.energy.text = esb.get("energy")
            self.speed.text = esb.get("speed")
            self.boost.text = esb.get("boost")

        if m_check == 0:
            self.energy.text = "0"
            self.speed.text = "0"
            self.boost.text = "0"

        if h_check == 0 and al_check == 0:
            self.amplitude.text = "0"
            self.energy.text = "0"
            self.speed.text = "0"
            self.boost.text = "0"

        if h_check == 1 or al_check == 1:
            Clock.schedule_interval(self.animate, 1/30)

    def animate(self, dt):
        self.number += 1/30
        A = long * math.sin(alpha)
        T = 2 * pi * (long / g) ** 0.5
        w = (2 * pi) / T

        xk = int(A * math.cos(w * self.number))
        yk = int(((long ** 2) - (xk ** 2)) ** 0.5)
        xk_ball = (self.pend.width / 2) + xk
        yk_ball = self.pend.height - yk + 30

        print("xk", xk_ball)
        print("yk", yk_ball)
        print("t", self.number,)

        self.anim.size = (30, 30)
        self.anim.color = (255/255, 137/255, 216/255, 1)
        self.anim.pos = (xk_ball - 15, yk_ball - 15)

        self.line_points = (self.pend.width / 2, self.pend.height - 30, xk_ball, yk_ball)

        if self.number == (1 + 1/30):
            self.grafic_points = (30, self.grafic.height / 2)

        self.grafic_points += (30 + self.number, (self.grafic.height / 2 + xk))






class PendulumApp(App):
    def build(self):
        self.icon = "L:/1/1x/logo.png"
        return Container()

if __name__ == '__main__':
    PendulumApp().run()
