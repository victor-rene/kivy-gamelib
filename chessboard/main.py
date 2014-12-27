from kivy.app import runTouchApp
from kivy.core.window import Window

from chessgrid import ChessGrid

Window.size = 400, 400

if __name__ == '__main__':
  runTouchApp(ChessGrid())