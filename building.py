## shree ganeshay namah
# from game import *
from var import *

class Buildings:
    def __init__(self,pos_x,pos_y,list1,shape,ind):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.list1 = list1
        self.shape = shape
        self.ind = ind
        self.active = False
        self.health = HUT_HEALTH
        if self.shape == 'T':
            self.health = TOWN_HALL_HEALTH
        elif self.shape == 'C':
            self.health = CANNON_HEALTH
        elif self.shape == '-':
            self.health = 1
        elif self.shape == 'S':
            self.health = STONE_HEALTH
        elif self.shape == 'W':
            self.health = WIZARD_HEALTH
    
    def update(self):
        if self.health > 0:
            for i in range(self.list1[0]):
                for j in range(self.list1[1]):
                    base[self.pos_x+i][self.pos_y+j]=self.shape
                    content[self.pos_x+i][self.pos_y+j]=self.shape
                    content2[self.pos_x+i][self.pos_y+j]=self.ind
        else:
            for i in range(self.list1[0]):
                for j in range(self.list1[1]):
                    base[self.pos_x+i][self.pos_y+j]=' '
                    content[self.pos_x+i][self.pos_y+j]=' '
                    content2[self.pos_x+i][self.pos_y+j]=0


class Defences(Buildings):
    def attack(self,king):
        if self.shape == 'C':
            for i in range(-CANNON_RANGE,CANNON_RANGE+1,1):
                for j in range(-CANNON_RANGE,CANNON_RANGE+1,1):
                    if self.pos_x+i >= 0 and self.pos_x+i < 50 and self.pos_y+j >= 0 and self.pos_y+j < 50:
                        if base[self.pos_x+i][self.pos_y+j] == '8':
                            king.health -= CANNON_ATTACK
                            self.active = True
                            return
                        elif base[self.pos_x+i][self.pos_y+j] == '@' or base[self.pos_x+i][self.pos_y+j] == 'A':
                            for k in every_troop:
                                if k.x == self.pos_x+i and k.y == self.pos_y+j:
                                    k.health -= CANNON_ATTACK
                                    self.active = True
                                    return
        elif self.shape == 'W':
            for i in range(-CANNON_RANGE,CANNON_RANGE+1,1):
                for j in range(-CANNON_RANGE,CANNON_RANGE+1,1):
                    if self.pos_x+i >= 0 and self.pos_x+i < 50 and self.pos_y+j >= 0 and self.pos_y+j < 50:
                        if base[self.pos_x+i][self.pos_y+j] == '8':
                            king.health -= CANNON_ATTACK
                            self.active = True
                            centre_x = self.pos_x+i
                            centre_y = self.pos_y+j
                            for k in every_troop:
                                if k.x == centre_x-1 or k.x == centre_x+1 or k.x == centre_x:
                                    if k.y == centre_y-1 or k.y == centre_y+1 or k.y == centre_y:    
                                        k.health -= CANNON_ATTACK
                                        self.active = True
                            return
                        elif base[self.pos_x+i][self.pos_y+j] == '@' or base[self.pos_x+i][self.pos_y+j] == 'A' or base[self.pos_x+i][self.pos_y+j] == 'B':
                            for k in every_troop:
                                if k.x == self.pos_x+i and k.y == self.pos_y+j:
                                    centre_x = self.pos_x+i
                                    centre_y = self.pos_y+j
                                    self.active = True
                                    break
                            for k in every_troop:
                                if k.x == centre_x-1 or k.x == centre_x+1 or k.x == centre_x:
                                    if k.y == centre_y-1 or k.y == centre_y+1 or k.y == centre_y:    
                                        k.health -= CANNON_ATTACK
                                        self.active = True
                            if king.x == centre_x-1 or king.x == centre_x+1 or king.x == centre_x:
                                if king.y == centre_y-1 or king.y == centre_y+1 or king.y == centre_y:
                                    king.health -= CANNON_ATTACK
                                    self.active = True
                            return