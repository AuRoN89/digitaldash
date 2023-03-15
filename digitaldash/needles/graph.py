"""Linear!"""
from kivy.properties import NumericProperty, ListProperty, ColorProperty
from kivy.uix.floatlayout import FloatLayout
from digitaldash.needles.needle import Needle
from math import cos
from kivy.clock import Clock


class NeedleGraph(Needle, FloatLayout):
    """Wrapper combining digitaldash.needles.needle and kivy.uix.stencilview."""

    update = NumericProperty()
    alpha = NumericProperty(1.0)
    step = NumericProperty()
    color = ColorProperty(defaultvalue="#FF0000FF")
    points = ListProperty(
        [(500, 500), [300, 300, 500, 300], [500, 400, 600, 400]]
    )
    linewidth = NumericProperty(10.0)

    _update_points_animation_ev = None
    dt = NumericProperty(0)

    def __init__(self, **kwargs):
        super(NeedleGraph, self).__init__()
        self.setUp(**kwargs)
        self.type = "Graph"

        # self.animate(True)

    # def animate(self, do_animation):
    #     if do_animation:
    #         self._update_points_animation_ev = Clock.schedule_interval(
    #             self.update, 0
    #         )
    #     elif self._update_points_animation_ev is not None:
    #         self._update_points_animation_ev.cancel()

    def setData(self, value):
        value = float(value)
        cy = self.height * 0.6
        cx = self.width * 0.1
        w = self.width * 0.8
        step = 20
        points = []

        for i in range(int(w / step)):
            x = i * step
            points.append(cx + x)
            points.append(cy + (x / w * 8.0 + value) * self.height * 0.2)
        self.points = points
