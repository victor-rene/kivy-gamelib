from kivy.animation import Animation
from kivy.base import runTouchApp

from foobar import FooBar


if __name__ == '__main__':
    fb = FooBar(pos=(375, 50), size=(100, 500), size_hint=(None, None))
    anim = Animation(force=100) + Animation(force=-100)
    anim.repeat = True
    anim.start(fb)
    runTouchApp(fb)
