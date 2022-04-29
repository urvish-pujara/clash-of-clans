from var import *


class Spell:
    def __init__(self,inp):
        self.inp = inp
    def start(self,king,every_troop):
        if self.inp == 'e':
            king.health = min(king.health*2,KING_HEALTH)
            for i in every_troop:
                i.health = min(i.health*2,TROOP_HEALTH)
        elif self.inp == 'r':
            king.power *= 2
            king.speed = min(king.speed*2,2*KING_SPEED)
            for i in every_troop:
                i.power *= 2
                i.speed = min(i.speed*2,2*TROOP_SPEED)