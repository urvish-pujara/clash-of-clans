from building import Buildings
from var import *
# import game
import math
class Troops:
    def __init__(self):
        self.health = TROOP_HEALTH
        self.power = TROOP_POWER
        self.speed = TROOP_SPEED
        self.x = 0
        self.y = 0
    
    def spawn(self,inp):
        if inp == '1':
            self.x = 20
            self.y = 1
            base[20][1] = '@'
            content[20][1] = 't'
        elif inp == '2':
            self.x = 1
            self.y = 35
            base[1][35] = '@'
            content[1][35] = 't'
        elif inp == '3':
            self.x = 40
            self.y = 48
            base[40][48] = '@'
            content[40][48] = 't'
        if inp == '4':

            self.health = ARCHER_HEALTH
            self.power = ARCHER_POWER
            self.speed = ARCHER_SPEED
            self.x = 10
            self.y = 1
            base[10][1] = 'A'
            content[10][1] = 'a'
        elif inp == '5':
            self.health = ARCHER_HEALTH
            self.power = ARCHER_POWER
            self.speed = ARCHER_SPEED
            self.x = 1
            self.y = 25
            base[1][25] = 'A'
            content[1][25] = 'a'
        elif inp == '6':
            self.health = ARCHER_HEALTH
            self.power = ARCHER_POWER
            self.speed = ARCHER_SPEED
            self.x = 30
            self.y = 48
            base[30][48] = 'A'
            content[30][48] = 'a'
        if inp == '7':
            self.health = BALLOON_HEALTH
            self.power = BALLOON_POWER
            self.speed = BALLOON_SPEED
            self.x = 30
            self.y = 1
            base[30][1] = 'B'
            content[30][1] = 'b'
        elif inp == '8':
            self.health = BALLOON_HEALTH
            self.power = BALLOON_POWER
            self.speed = BALLOON_SPEED
            self.x = 1
            self.y = 45
            base[1][45] = 'B'
            content[1][45] = 'b'
        elif inp == '9':
            self.health = BALLOON_HEALTH
            self.power = BALLOON_POWER
            self.speed = BALLOON_SPEED
            self.x = 20
            self.y = 48
            base[20][48] = 'B'
            content[20][48] = 'b'
    def update(self):
        if self.health > 0:
            if(self.speed == 1):
                base[self.x][self.y] = '@'
            elif(self.speed == 2 and self.power == 5):
                base[self.x][self.y] = 'A'
            elif(self.speed == 2 and self.power == 20):
                base[self.x][self.y] = 'B'
        else:
            base[self.x][self.y] = ' '
            content[self.x][self.y] = ' '
            every_troop.remove(self)
    def move(self):
        if self.health > 0:
            spd = self.speed
            while spd > 0:
                spd-=1
                dis = math.inf # distance
                dis2 = math.inf # distance
                base[self.x][self.y] = ' '
                content[self.x][self.y] = ' '

                for i in every_building:
                    if i.health > 0 and (i.shape == 'C' or i.shape == 'W'):
                        for j in range(i.list1[0]):
                            for k in range(i.list1[1]):
                                if abs(self.x-(i.pos_x + j)) + abs(self.y-(i.pos_y + k)) < dis2:
                                    dis2 = abs(self.x-(i.pos_x + j)) + abs(self.y-(i.pos_y + k))
                                    ind2 = i
                                    x_cord2 = i.pos_x + j
                                    y_cord2 = i.pos_y + k
                for i in every_building:
                    if i.health > 0:
                        for j in range(i.list1[0]):
                            for k in range(i.list1[1]):
                                if abs(self.x-(i.pos_x + j)) + abs(self.y-(i.pos_y + k)) < dis:
                                    dis = abs(self.x-(i.pos_x + j)) + abs(self.y-(i.pos_y + k))
                                    ind = i
                                    x_cord = i.pos_x + j
                                    y_cord = i.pos_y + k
                if dis != math.inf:
                    if(base[self.x][self.y] == '@'):
                        if dis == 1 or (dis == 2 and self.x != x_cord and self.y != y_cord):
                            ind.health -= self.power
                        else:
                            if(self.x < x_cord):
                                self.x += 1
                            elif(self.x > x_cord):
                                self.x -= 1
                            if(self.y < y_cord):
                                self.y += 1
                            elif(self.y > y_cord):
                                self.y -= 1
                        base[self.x][self.y] = '@'
                        content[self.x][self.y] = 't'
                    elif(base[self.x][self.y] == 'A'):
                        if dis <= 8:
                            ind.health -= self.power
                        else:
                            if(self.x < x_cord):
                                self.x += 1
                            elif(self.x > x_cord):
                                self.x -= 1
                            if(self.y < y_cord):
                                self.y += 1
                            elif(self.y > y_cord):
                                self.y -= 1
                        base[self.x][self.y] = 'A'
                        content[self.x][self.y] = 'a'
                    elif(base[self.x][self.y] == 'B'):
                        if dis2 != math.inf:
                            if dis2 == 0:
                                ind2.health -= self.power
                            else:
                                if(self.x < x_cord2):
                                    self.x += 1
                                elif(self.x > x_cord2):
                                    self.x -= 1
                                if(self.y < y_cord2):
                                    self.y += 1
                                elif(self.y > y_cord2):
                                    self.y -= 1
                            base[self.x][self.y] = 'B'
                            content[self.x][self.y] = 'b'
                        elif dis2 == math.inf and dis != math.inf:
                            if dis == 0:
                                ind.health -= self.power
                            else:
                                if(self.x < x_cord):
                                    self.x += 1
                                elif(self.x > x_cord):
                                    self.x -= 1
                                if(self.y < y_cord):
                                    self.y += 1
                                elif(self.y > y_cord):
                                    self.y -= 1
                            base[self.x][self.y] = 'B'
                            content[self.x][self.y] = 'b'
                            