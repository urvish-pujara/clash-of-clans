from var import *
import time
class King:
    def __init__(self):
        self.health = KING_HEALTH
        self.power = KING_POWER
        self.speed = KING_SPEED
        self.x = POSITION_KING[0]
        self.y = POSITION_KING[1]
    
    def update(self):
        if self.health > 0:
            base[self.x][self.y] = '8'
        else:
            base[self.x][self.y] = ' '

    def move(self,inp):
        spd = self.speed
        while spd > 0:
            spd-=1
            if inp == 'w':
                # self.health -= 10
                if self.x > 0 and base[self.x-1][self.y] == ' ':
                    base[self.x][self.y] = ' '
                    self.x -= 1
                    self.update()
            elif inp == 'a':
                if self.y > 0 and base[self.x][self.y-1] == ' ':
                    base[self.x][self.y] = ' '
                    self.y -= 1
                    self.update()
            elif inp == 's':
                if self.x < 49 and base[self.x+1][self.y] == ' ':
                    base[self.x][self.y] = ' '
                    self.x += 1
                    self.update()
            elif inp == 'd':
                if self.y < 49 and base[self.x][self.y+1] == ' ':
                    base[self.x][self.y] = ' '
                    self.y += 1
                    self.update()
        
    def attack(self,inp,town_hall,cannons,huts,walls,stones,wizards,hero,last_direction):
        if inp == ' ' and hero == 1:
            # ATTACKING RIGHT
            if content[self.x][self.y+1] != ' ' and content[self.x][self.y+1] != '.':
                if content[self.x][self.y+1] == 'T':
                    if town_hall.health > 0:
                        town_hall.health -= self.power
                        if town_hall.health <= 0:
                            town_hall.health = 0
                elif content[self.x][self.y+1] == 'C':
                    if cannons[content2[self.x][self.y+1]].health > 0:
                        cannons[content2[self.x][self.y+1]].health -= self.power
                        if cannons[content2[self.x][self.y+1]].health <= 0:
                            cannons[content2[self.x][self.y+1]].health = 0
                elif content[self.x][self.y+1] == 'W':
                    if wizards[content2[self.x][self.y+1]].health > 0:
                        wizards[content2[self.x][self.y+1]].health -= self.power
                        if wizards[content2[self.x][self.y+1]].health <= 0:
                            wizards[content2[self.x][self.y+1]].health = 0
                elif content[self.x][self.y+1] == 'H':
                    if huts[content2[self.x][self.y+1]].health > 0:
                        huts[content2[self.x][self.y+1]].health -= self.power
                        if huts[content2[self.x][self.y+1]].health <= 0:
                            huts[content2[self.x][self.y+1]].health = 0
                elif content[self.x][self.y+1] == '-':
                    if walls[content2[self.x][self.y+1]].health > 0:
                        walls[content2[self.x][self.y+1]].health -= self.power
                elif content[self.x][self.y+1] == 'S':
                    if stones[content2[self.x][self.y+1]].health > 0:
                        stones[content2[self.x][self.y+1]].health -= self.power
            # ATTACKING LEFT
            elif content[self.x][self.y-1] != ' ' and content[self.x][self.y-1] != '.':
                if content[self.x][self.y-1] == 'T':
                    if town_hall.health > 0:
                        town_hall.health -= self.power
                        if town_hall.health <= 0:
                            town_hall.health = 0
                elif content[self.x][self.y-1] == 'C':
                    if cannons[content2[self.x][self.y-1]].health > 0:
                        cannons[content2[self.x][self.y-1]].health -= self.power
                        if cannons[content2[self.x][self.y-1]].health <= 0:
                            cannons[content2[self.x][self.y-1]].health = 0
                elif content[self.x][self.y-1] == 'W':
                    if wizards[content2[self.x][self.y-1]].health > 0:
                        wizards[content2[self.x][self.y-1]].health -= self.power
                        if wizards[content2[self.x][self.y-1]].health <= 0:
                            wizards[content2[self.x][self.y-1]].health = 0
                elif content[self.x][self.y-1] == 'H':
                    if huts[content2[self.x][self.y-1]].health > 0:
                        huts[content2[self.x][self.y-1]].health -= self.power
                        if huts[content2[self.x][self.y-1]].health <= 0:
                            huts[content2[self.x][self.y-1]].health = 0
                elif content[self.x][self.y-1] == '-':
                    if walls[content2[self.x][self.y-1]].health > 0:
                        walls[content2[self.x][self.y-1]].health -= self.power
                elif content[self.x][self.y-1] == 'S':
                    if stones[content2[self.x][self.y-1]].health > 0:
                        stones[content2[self.x][self.y-1]].health -= self.power
            # ATTACKING UP
            elif content[self.x-1][self.y] != ' ' and content[self.x-1][self.y] != '.':
                if content[self.x-1][self.y] == 'T':
                    if town_hall.health > 0:
                        town_hall.health -= self.power
                        if town_hall.health <= 0:
                            town_hall.health = 0
                elif content[self.x-1][self.y] == 'C':
                    if cannons[content2[self.x-1][self.y]].health > 0:
                        cannons[content2[self.x-1][self.y]].health -= self.power
                        if cannons[content2[self.x-1][self.y]].health <= 0:
                            cannons[content2[self.x-1][self.y]].health = 0
                elif content[self.x-1][self.y] == 'W':
                    if wizards[content2[self.x-1][self.y]].health > 0:
                        wizards[content2[self.x-1][self.y]].health -= self.power
                        if wizards[content2[self.x-1][self.y]].health <= 0:
                            wizards[content2[self.x-1][self.y]].health = 0
                elif content[self.x-1][self.y] == 'H':
                    if huts[content2[self.x-1][self.y]].health > 0:
                        huts[content2[self.x-1][self.y]].health -= self.power
                        if huts[content2[self.x-1][self.y]].health <= 0:
                            huts[content2[self.x-1][self.y]].health = 0
                elif content[self.x-1][self.y] == '-':
                    if walls[content2[self.x-1][self.y]].health > 0:
                        walls[content2[self.x-1][self.y]].health -= self.power
                elif content[self.x-1][self.y] == 'S':
                    if stones[content2[self.x-1][self.y]].health > 0:
                        stones[content2[self.x-1][self.y]].health -= self.power
            # ATTACKING DOWN
            elif content[self.x+1][self.y] != ' ' and content[self.x+1][self.y] != '.':
                if content[self.x+1][self.y] == 'T':
                    if town_hall.health > 0:
                        town_hall.health -= self.power
                        if town_hall.health <= 0:
                            town_hall.health = 0
                elif content[self.x+1][self.y] == 'C':
                    if cannons[content2[self.x+1][self.y]].health > 0:
                        cannons[content2[self.x+1][self.y]].health -= self.power
                        if cannons[content2[self.x+1][self.y]].health <= 0:
                            cannons[content2[self.x+1][self.y]].health = 0
                elif content[self.x+1][self.y] == 'W':
                    if wizards[content2[self.x+1][self.y]].health > 0:
                        wizards[content2[self.x+1][self.y]].health -= self.power
                        if wizards[content2[self.x+1][self.y]].health <= 0:
                            wizards[content2[self.x+1][self.y]].health = 0
                elif content[self.x+1][self.y] == 'H':
                    if huts[content2[self.x+1][self.y]].health > 0:
                        huts[content2[self.x+1][self.y]].health -= self.power
                        if huts[content2[self.x+1][self.y]].health <= 0:
                            huts[content2[self.x+1][self.y]].health = 0
                elif content[self.x+1][self.y] == '-':
                    if walls[content2[self.x+1][self.y]].health > 0:
                        walls[content2[self.x+1][self.y]].health -= self.power
                elif content[self.x+1][self.y] == 'S':
                    if stones[content2[self.x+1][self.y]].health > 0:
                        stones[content2[self.x+1][self.y]].health -= self.power
        if inp == 'u' and hero == 1:
            involve_hut=[0,0,0,0,0,0]
            involve_cannon=[0,0,0,0,0]
            involve_wizard=[0,0,0,0,0]
            involve_townhall=0
            for i in range(self.x - 5, self.x +5):
                for j in range(self.y - 5, self.y +5):
                    if content[i][j] == 'T':
                        involve_townhall=1
                    elif content[i][j] == 'C':
                        involve_cannon[content2[i][j]]=1
                    elif content[i][j] == 'W':
                        involve_wizard[content2[i][j]]=1
                    elif content[i][j] == 'H':
                        involve_hut[content2[i][j]]=1
                    elif content[i][j] == '-':
                        if walls[content2[self.x+1][self.y]].health > 0:
                            walls[content2[self.x+1][self.y]].health -= self.power
            for i in range(5):
                if huts[i].health > 0 and involve_hut[i]==1:
                    huts[i].health -= 2*self.power
                    if huts[i].health <= 0:
                        huts[i].health = 0
            
            for i in range(4):
                if cannons[i].health > 0 and involve_cannon[i]==1:
                    cannons[i].health -= 2*self.power
                    if cannons[i].health <= 0:
                        cannons[i].health = 0
            

            for i in range(2):
                if wizards[i].health > 0 and involve_wizard[i]==1:
                    wizards[i].health -= 2*self.power
                    if wizards[i].health <= 0:
                        wizards[i].health = 0

            if(involve_townhall==1):
                if town_hall.health > 0:
                    town_hall.health -= 2*self.power
                    if town_hall.health <= 0:
                        town_hall.health = 0
        if inp == ' ' and hero == 2:
            direction =[]
            positions=[]
            # last_direction = "w"
            if last_direction == "w":
                positions = [-8,0] 
            elif last_direction == "s":
                positions = [8,0]
            elif last_direction == "a":
                positions = [0,-8]
            elif last_direction == "d":
                positions = [0,8]
            for i in range(5):
                    for j in range(5):
                        direction.append([positions[0]+i-2,positions[1]+j-2])
            building_geting_attacked = []
            involve_hut=[0,0,0,0,0,0]
            involve_cannon=[0,0,0,0,0]
            involve_wizard=[0,0,0,0,0]
            involve_townhall=0
            # ATTACKING RIGHT
            for d in direction:
                if content[self.x+d[0]][self.y+d[1]] != ' ' and content[self.x+d[0]][self.y+d[1]] != '.':
                    if content[self.x+d[0]][self.y+d[1]] == 'T':
                        involve_townhall=1
                    elif content[self.x+d[0]][self.y+d[1]] == 'C':
                        involve_cannon[content2[self.x+d[0]][self.y+d[1]]]=1
                    elif content[self.x+d[0]][self.y+d[1]] == 'W':
                        involve_wizard[content2[self.x+d[0]][self.y+d[1]]]=1
                    elif content[self.x+d[0]][self.y+d[1]] == 'H':
                        involve_hut[content2[self.x+d[0]][self.y+d[1]]]=1
                    elif content[self.x+d[0]][self.y+d[1]] == '-':
                        if walls[content2[self.x+d[0]][self.y+d[1]]].health > 0:
                            walls[content2[self.x+d[0]][self.y+d[1]]].health -= self.power
            for i in range(5):
                if huts[i].health > 0 and involve_hut[i]==1:
                    huts[i].health -= self.power
                    if huts[i].health <= 0:
                        huts[i].health = 0
            
            for i in range(4):
                if cannons[i].health > 0 and involve_cannon[i]==1:
                    cannons[i].health -= self.power
                    if cannons[i].health <= 0:
                        cannons[i].health = 0
            

            for i in range(2):
                if wizards[i].health > 0 and involve_wizard[i]==1:
                    wizards[i].health -= self.power
                    if wizards[i].health <= 0:
                        wizards[i].health = 0

            if(involve_townhall==1):
                if town_hall.health > 0:
                    town_hall.health -= self.power
                    if town_hall.health <= 0:
                        town_hall.health = 0
        if inp == 't' and hero == 2:
            time.sleep(1)
            direction =[]
            positions=[]
            # last_direction = "w"
            if last_direction == "w":
                positions = [-16,0] 
            elif last_direction == "s":
                positions = [16,0]
            elif last_direction == "a":
                positions = [0,-16]
            elif last_direction == "d":
                positions = [0,16]
            for i in range(9):
                    for j in range(9):
                        direction.append([positions[0]+i-4,positions[1]+j-4])
            building_geting_attacked = []
            involve_hut=[0,0,0,0,0,0]
            involve_cannon=[0,0,0,0,0]
            involve_wizard=[0,0,0,0,0]
            involve_townhall=0
            # ATTACKING RIGHT
            for d in direction:
                if content[self.x+d[0]][self.y+d[1]] != ' ' and content[self.x+d[0]][self.y+d[1]] != '.':
                    if content[self.x+d[0]][self.y+d[1]] == 'T':
                        involve_townhall=1
                    elif content[self.x+d[0]][self.y+d[1]] == 'C':
                        involve_cannon[content2[self.x+d[0]][self.y+d[1]]]=1
                    elif content[self.x+d[0]][self.y+d[1]] == 'W':
                        involve_wizard[content2[self.x+d[0]][self.y+d[1]]]=1
                    elif content[self.x+d[0]][self.y+d[1]] == 'H':
                        involve_hut[content2[self.x+d[0]][self.y+d[1]]]=1
                    elif content[self.x+d[0]][self.y+d[1]] == '-':
                        if walls[content2[self.x+d[0]][self.y+d[1]]].health > 0:
                            walls[content2[self.x+d[0]][self.y+d[1]]].health -= self.power
            for i in range(len(huts)):
                if huts[i].health > 0 and involve_hut[i]==1:
                    huts[i].health -= self.power
                    if huts[i].health <= 0:
                        huts[i].health = 0
            
            for i in range(len(cannons)):
                if cannons[i].health > 0 and involve_cannon[i]==1:
                    cannons[i].health -= self.power
                    if cannons[i].health <= 0:
                        cannons[i].health = 0
            

            for i in range(len(wizards)):
                if wizards[i].health > 0 and involve_wizard[i]==1:
                    wizards[i].health -= self.power
                    if wizards[i].health <= 0:
                        wizards[i].health = 0

            if(involve_townhall==1):
                if town_hall.health > 0:
                    town_hall.health -= self.power
                    if town_hall.health <= 0:
                        town_hall.health = 0