from kivy.graphics import Color, Line
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.widget import Widget


class SquareGrid(Widget):

    cols = NumericProperty(16)
    rows = NumericProperty(9)
    cell = ListProperty([0, 0])
    line_width = NumericProperty(1)
    line_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kw):
        super(SquareGrid, self).__init__(**kw)
        self.bind(cols=self.draw, rows=self.draw, pos=self.draw, size=self.draw)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            x = (touch.x - self.x) / self.cols
            y = (touch.y - self.y) / self.rows
            self.cell = x, y
            return True
        return super(SquareGrid, self).on_touch_down(touch)

    def draw(self, *args):
        x, y = self.pos
        w, h = self.size
        col_w = self.width / float(self.cols)
        row_h = self.height / float(self.rows)
        self.canvas.clear()
        with self.canvas:
            Color(*self.line_color)
            for y in range(self.rows + 1):
                for x in range(self.cols + 1):
                    Line(
                        points=[x * col_w, self.y, x * col_w, self.y + h],
                        width=self.line_width)
                    Line(
                        points=[self.x, y * row_h, self.x + w, y * row_h],
                        width=self.line_width)


if __name__ == '__main__':
    from kivy.base import runTouchApp
    sg = SquareGrid(cols=8, rows=6)
    runTouchApp(sg)
