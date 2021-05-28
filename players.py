import random as r

class Player(object):
    def __init__(self,player_letter,game):
       self.player_letter = player_letter
       self.game = game
    def move(self):
        pass
class HumanPlayer(Player):
    def __init__(self,player_letter,game):
       super().__init__(player_letter,game)

    def move(self):
        is_valid = False
        move = None

        while not is_valid:
            try:
                move = int(input(f"{self.player_letter}\'s turn.input move[1-9]"))-1
                if move not in self.game.moves_available():
                    raise ValueError
                is_valid =True
            except:
                print("oops it was an invalid move,try again")
        return move
class ComputerPlayer(Player):
    def __init__(self,player_letter,game):
         super().__init__(player_letter,game)

    def move(self):
        return r.choice(self.game.moves_available())