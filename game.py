from random import randint
from building import Buildings, Defences
from king import King
from troops import Troops
from spell import Spell
from var import *
from input import *
from colorama import Fore, Back, Style
from numpy import random
import os
import os.path
level = 1
def gameEnd():
    result = 0
    for i in range(50):
        for j in range(50):
            if(base[i][j]== '@' or base[i][j]== '8'):
                result += 1
                break
        if(result != 0):
            break
    flag = True
    for i in range(50):
        for j in range(50):
            if(base[i][j]== 'H' or base[i][j]== 'C' or base[i][j]== 'T'):
                result += 2
                break
        if(result >= 2):
            break
    return result
town_hall_size = [4,3]
town_hall = Buildings(23,23,town_hall_size,'T',0)
every_building.append(town_hall)
town_hall.update()
last_direction = "w"

cannon_size = [2,3]
cannon_pos = []
wizard_size = [2,2]
wizard_pos = []
wizards = []
cannons = []
hut_size = [2,2]
hut_pos = [[4,4],[4,10],[10,4],[16,4],[4,16]]
walls = []
huts = []
wall_size = [1,1]
wall_pos = []
for i in range(len(hut_pos)):
    hut = Buildings(hut_pos[i][0],hut_pos[i][1],hut_size,'H',i)
    huts.append(hut)
    every_building.append(hut)
def level1():
    base[king.x][king.y] = " "
    king.health = KING_HEALTH
    king.power = KING_POWER
    king.speed = KING_SPEED
    king.x = POSITION_KING[0]
    king.y = POSITION_KING[1]
    base[king.x][king.y] = "8"
    cannon_pos.clear()
    wizard_pos.clear()
    wall_pos.clear()
    cannons.clear()
    wizards.clear()
    cannon_pos.append([19,19])
    cannon_pos.append([29,29])
    cannon_pos.append([14,34])
    # cannon_pos.append([34,14])
    wizard_pos.append([24,4])
    # wizard_pos.append([4,24])
    for i in range(len(cannon_pos)):
        cannon = Defences(cannon_pos[i][0],cannon_pos[i][1],cannon_size,'C',i)
        cannons.append(cannon)
        every_building.append(cannon)
    for i in cannons:
        i.update()
    for i in range(len(wizard_pos)):
        wizard = Defences(wizard_pos[i][0],wizard_pos[i][1],wizard_size,'W',i)
        wizards.append(wizard)
        every_building.append(wizard)
    for i in wizards:
        i.update()
    for i in huts:
        i.update()
    # wall_pos.append([21,i] for i in range(21,29)] + [[i,21] for i in range(21,29))
    for i in range(21,29):
        wall_pos.append([21,i])
        wall_pos.append([i,21])
    for i in range(21,29):
        wall_pos.append([28,i])
        wall_pos.append([i,28])
        # wall_pos.append([i,i])
    for i in range(len(wall_pos)):
        wall = Buildings(wall_pos[i][0],wall_pos[i][1],wall_size,'-',i)
        walls.append(wall)

    for i in walls:
        i.update()


# level 2
def level2():
    level1()
    for i in every_troop:
        i.health = 0
        base[i.x][i.y] = " "
        content[i.x][i.y] = " "
        # content2[i.x][i.y] = 0
    cannon_pos.append([34,14])
    cannon = Defences(cannon_pos[3][0],cannon_pos[3][1],cannon_size,'C',3)
    cannons.append(cannon)
    every_building.append(cannon)
    cannon.update()
    wizard_pos.append([4,24])
    wizard = Defences(wizard_pos[1][0],wizard_pos[1][1],wizard_size,'W',1)
    wizards.append(wizard)
    every_building.append(wizard)
    wizard.update()
    town_hall.health = TOWN_HALL_HEALTH
    for i in cannons:
        i.health = CANNON_HEALTH
    for i in wizards:
        i.health = WIZARD_HEALTH
    for i in huts:
        i.health = HUT_HEALTH
    for i in range(21,29):
        wall_pos.append([21,i])
        wall_pos.append([i,21])
    for i in range(21,29):
        wall_pos.append([28,i])
        wall_pos.append([i,28])
        # wall_pos.append([i,i])
    for i in range(len(wall_pos)):
        wall = Buildings(wall_pos[i][0],wall_pos[i][1],wall_size,'-',i)
        walls.append(wall)

    for i in walls:
        i.update()

def level3():
    level1()
    for i in every_troop:
        i.health = 0
        base[i.x][i.y] = " "
        content[i.x][i.y] = " "
        # content2[i.x][i.y] = 0
    cannon_pos.append([34,14])
    cannon = Defences(cannon_pos[3][0],cannon_pos[3][1],cannon_size,'C',3)
    cannons.append(cannon)
    every_building.append(cannon)
    cannon.update()
    wizard_pos.append([4,24])
    wizard = Defences(wizard_pos[1][0],wizard_pos[1][1],wizard_size,'W',1)
    wizards.append(wizard)
    every_building.append(wizard)
    wizard.update()



    cannon_pos.append([8,8])
    cannon = Defences(cannon_pos[4][0],cannon_pos[4][1],cannon_size,'C',4)
    cannons.append(cannon)
    every_building.append(cannon)
    cannon.update()
    wizard_pos.append([12,12])
    wizard = Defences(wizard_pos[2][0],wizard_pos[2][1],wizard_size,'W',2)
    wizards.append(wizard)
    every_building.append(wizard)
    wizard.update()



    town_hall.health = TOWN_HALL_HEALTH
    for i in cannons:
        i.health = CANNON_HEALTH
    for i in wizards:
        i.health = WIZARD_HEALTH
    for i in huts:
        i.health = HUT_HEALTH
    for i in range(21,29):
        wall_pos.append([21,i])
        wall_pos.append([i,21])
    for i in range(21,29):
        wall_pos.append([28,i])
        wall_pos.append([i,28])
        # wall_pos.append([i,i])
    for i in range(len(wall_pos)):
        wall = Buildings(wall_pos[i][0],wall_pos[i][1],wall_size,'-',i)
        walls.append(wall)

    for i in walls:
        i.update()



stone_size = [1,1]
stone_pos = [[45,30],[45,35],[45,40]]
stones = []
for i in range(len(stone_pos)):
    stone = Buildings(stone_pos[i][0],stone_pos[i][1],stone_size,'S',i)
    stones.append(stone)

for i in stones:
    i.update()
gems_arr = []
king = King()
king.update()
gems = 0
gems_arr.append(0)
for i in stones:
    gems_arr.append(random.randint(1,4))
gems_arr[2] += gems_arr[1]
gems_arr[3] += gems_arr[2]

for i in range(1000):
    if os.path.exists('replay/'+str(i)+'.txt'):
        continue
    else:
        file1 = open('replay/'+str(i)+'.txt', "a")
        break

print("Press '1' for using king\nPress '2' for using queen\n")
hero = 0
hero = int(input())
file1.write(str(gems_arr[1])+str(gems_arr[2])+str(gems_arr[3])+"\n")
# level = 0
level1()
while True:
    
    x = Get()
    p = input_to(x)
    game_status = gameEnd()
    # print(king.health)
    if(game_status==1 and level == 1):
        ##print(base)
        level = 2
        print("You won level 1!\n")
        level2()
    elif(game_status==1 and level == 2):
        ##print(base)
        level = 3
        print("You won level 2!\n")
        level3()
    elif(game_status==1 and level == 3):
        ##print(base)
        print("You won the game!\n")
        break
    elif(game_status==2):
        print("You lost!\n")
        quit()
    for i in cannons:
        i.active = False
        if i.health > 0:
            i.attack(king)
        # i.attack(king)
    for i in wizards:
        i.active = False
        if i.health > 0:
            i.attack(king)
        # i.attack(king)
    if p == None:
        pass
    elif p == 'q':
        file1.write(p + "\n")
        break
    elif p == 'w' or p == 'a' or p == 's' or p == 'd':
        last_direction = p
        file1.write(p + "\n")
        king.move(p)
    elif p == ' ':
        file1.write(p + "\n")
        king.attack(p,town_hall,cannons,huts,walls,stones,wizards,hero,last_direction)
    elif p == 'u':
        file1.write(p + "\n")
        king.attack(p,town_hall,cannons,huts,walls,stones,wizards,hero,last_direction)
    elif p == '1' or p == '2' or p == '3':
        # print(every_troop)
        file1.write(p + "\n")
        troop = Troops()
        troop.spawn(p)
        every_troop.append(troop)
    elif p == '4' or p == '5' or p == '6':
        file1.write(p + "\n")
        archer = Troops()
        archer.spawn(p)
        every_troop.append(archer)
    elif p == '7' or p == '8' or p == '9':
        file1.write(p + "\n")
        balloon = Troops()
        balloon.spawn(p)
        every_troop.append(balloon)
    elif p == 'e' or p == 'r':
        file1.write(p + "\n")
        spell = Spell(p)
        spell.start(king,every_troop)
    elif p == 't':
        file1.write(p + "\n")
        king.attack(p,town_hall,cannons,huts,walls,stones,wizards,hero,last_direction)

    for i in range(0,50):
        base[i][0]='.'
        base[i][49]='.'
    for i in range(0,50):
        base[0][i]='.'
        base[49][i]='.'
    base[20][0] = '1'
    base[0][35] = '2'
    base[40][49] = '3'
    base[10][0] = '4'
    base[0][25] = '5'
    base[30][49] = '6'
    base[30][0] = '7'
    base[0][45] = '8'
    base[20][49] = '9'
    os.system('clear')
    for i in every_building:
        i.update()
    for i in walls:
        if content[i.pos_x][i.pos_y] == '-':
            i.update()
        # i.update()
    king.update()
    for i in every_troop:
        i.update()
        i.move()
    for i in range(50):
        for j in range(50):
            if base[i][j] == 'T':
                if town_hall.health > TOWN_HALL_HEALTH/2:
                    print(Fore.GREEN + base[i][j] + Fore.RESET,end=' ')
                elif town_hall.health > TOWN_HALL_HEALTH/4:
                    print(Fore.YELLOW + base[i][j] + Fore.RESET,end=' ')
                else:
                    print(Fore.RED + base[i][j] + Fore.RESET,end=' ')
            elif base[i][j] == 'C':
                if cannons[content2[i][j]].active == True:
                    print(Back.LIGHTWHITE_EX ,end='')
                if cannons[content2[i][j]].health > CANNON_HEALTH/2:
                    print(Fore.GREEN + base[i][j] + Fore.RESET,end=' ')
                elif cannons[content2[i][j]].health > CANNON_HEALTH/4:
                    print(Fore.YELLOW + base[i][j] + Fore.RESET,end=' ')
                else:
                    print(Fore.RED + base[i][j] + Fore.RESET,end=' ')
                print(Back.RESET,end='')
            elif base[i][j] == 'W':
                if wizards[content2[i][j]].active == True:
                    print(Back.LIGHTWHITE_EX ,end='')
                if wizards[content2[i][j]].health > WIZARD_HEALTH/2:
                    print(Fore.GREEN + base[i][j] + Fore.RESET,end=' ')
                elif wizards[content2[i][j]].health > WIZARD_HEALTH/4:
                    print(Fore.YELLOW + base[i][j] + Fore.RESET,end=' ')
                else:
                    print(Fore.RED + base[i][j] + Fore.RESET,end=' ')
                print(Back.RESET,end='')
            elif base[i][j] == 'H':
                if huts[content2[i][j]].health > HUT_HEALTH/2:
                    print(Fore.GREEN + base[i][j] + Fore.RESET,end=' ')
                elif huts[content2[i][j]].health > HUT_HEALTH/4:
                    print(Fore.YELLOW + base[i][j] + Fore.RESET,end=' ')
                else:
                    print(Fore.RED + base[i][j] + Fore.RESET,end=' ')
            
            elif base[i][j] == 'S':
                if stones[content2[i][j]].health > 0:
                    print('🪨',end=' ')
                else:
                    print(" ",end=' ')
            else:
                print(base[i][j],end=' ')
        print()
    # print(king.health)
    green_bar = ' ' * int(10*king.health/int(KING_HEALTH))
    red_bar = ' ' * (10 - 10*king.health//KING_HEALTH)
    index =0
    for i in stones:
        if(i.health<=0):
            index +=1
    print("💎:",end = " ")
    print(gems_arr[index])
    print()
    
    print('|' + Back.GREEN + green_bar + Back.RED + red_bar + Back.RESET + '|')
    
file1.close()
