from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class HeartBar(BoxLayout):

    health = NumericProperty(0)
    max_health = NumericProperty(20)

    def __init__(self, **kw):
        super(HeartBar, self).__init__(**kw)
        self.orientation = 'horizontal'
        self.hearts = []
        self.bind(health=self._calc_hearts)
        self.bind(max_health=self._calc_hearts)
        self._calc_hearts()

    def _calc_hearts(self, *args):
        """ Each heart is worth 4 pts. """
        del self.hearts[:]
        hp = self.health
        for i in range(self.max_health / 4):
            if hp > 4:
                n = 4
            elif hp <= 0:
                n = 0
            else:
                n = int(hp)
            self.hearts.append(n)
            hp -= 4
        self._draw_hearts()

    def _draw_hearts(self):
        self.clear_widgets()
        i = 0
        while i < (self.max_health / 4):
            heart = Image(size=(80, 80))
            heart.source = 'img/heart-' + str(self.hearts[i]) + '.png'
            self.add_widget(heart)
            i += 1
