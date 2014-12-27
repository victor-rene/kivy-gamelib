class Board:

  def __init__(self):
    self.squares = None
    self.listeners = []
    self.starting_position()
    self.side_to_move = 1

  def clear(self):
    self.squares = [[' ' for rank in range(8)] for file in range(8)]
    
  def switch_turn(self):
    self.side_to_move *= -1
    
  def starting_position(self):
    self.from_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    
  def from_fen(self, fen):
    self.clear()
    fen_parts = fen.split(' ')
    fen_ranks = fen_parts[0].split('/')
    rank = 7
    file = 0
    while rank >= 0:
      fen_rank = fen_ranks[8 - (rank + 1)]
      file = 0
      i = 0
      n = len(fen_rank)
      while i < n:
        c = fen_rank[i]
        if c.isdigit():
          file += int(c)
        else:
          self.squares[file][rank] = c
          file += 1
        i += 1
      rank -= 1
    for listener in self.listeners:
      if hasattr(listener, 'update'):
        listener.update()

  def to_fen(self):
    space = 0
    fen = []
    for y in range(7, -1, -1):
      for x in range(8):
        if self.squares[x][y] == ' ':
          space += 1
        else:
          if space > 0:
            fen.append(str(space))
          fen.append(self.squares[x][y])
          space = 0
      if space > 0:
        fen.append(str(space))
      space = 0;
      if y > 0:
        fen.append("/")
    if self.side_to_move == 1:
      fen.append(" w")
    else: fen.append(" b")
    return ''.join(fen)
    
  def move(self, orig, dest):
    self.squares[dest[0]][dest[1]] = self.squares[orig[0]][orig[1]]
    self.squares[orig[0]][orig[1]] = ' '
    for listener in self.listeners:
      if hasattr(listener, 'update'):
        listener.update()
        
  def search_pieces(self, type):
    squares = []
    for rank in range(8):
      for file in range(8):
        if self.squares[file][rank] == type:
          squares.append([file, rank])
    return squares
    
  def add_listener(self, listener):
    self.listeners.append(listener)
    
  def remove_listener(self, listener):
    self.listeners.remove(listener)