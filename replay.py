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
import time

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


cannon_size = [2,3]
cannon_pos = [[19,19],[29,29], [14,34], [34,14]]
cannons = []
for i in range(len(cannon_pos)):
    cannon = Defences(cannon_pos[i][0],cannon_pos[i][1],cannon_size,'C',i)
    cannons.append(cannon)
    every_building.append(cannon)

for i in cannons:
    i.update()

hut_size = [2,2]
hut_pos = [[4,4],[4,10],[10,4],[16,4],[4,16]]
huts = []
for i in range(len(hut_pos)):
    hut = Buildings(hut_pos[i][0],hut_pos[i][1],hut_size,'H',i)
    huts.append(hut)
    every_building.append(hut)

for i in huts:
    i.update()


wall_size = [1,1]
wall_pos = [[21,i] for i in range(21,29)] + [[i,21] for i in range(21,29)]
for i in range(21,29):
    wall_pos.append([28,i])
    wall_pos.append([i,28])
    # wall_pos.append([i,i])
walls = []
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

file1 = open("replay/" + str(sys.argv[1])+".txt", 'r')
Lines = file1.readlines()
gems_arr.append(Lines[0][0])
gems_arr.append(Lines[0][1])
gems_arr.append(Lines[0][2])
count = 1
while True:
    if count >= len(Lines):
        p=""
    else:
        p = Lines[count][0]
    count += 1
    
    game_status = gameEnd()
    # print(king.health)
    for i in every_troop:
        print(i.health, end= " ")
    if(game_status==1):
        ##print(base)
        print("You won!\n")
        break
    
    elif(game_status==2):
        print("You lost!\n")
        break
    for i in cannons:
        i.active = False
        if i.health > 0:
            i.attack(king)
        # i.attack(king)
    if p == None:
        pass
    elif p == 'q':
        break
    elif p == 'w' or p == 'a' or p == 's' or p == 'd':
        king.move(p)
    elif p == ' ':
        king.attack(p,town_hall,cannons,huts,walls,stones)
    elif p == '1' or p == '2' or p == '3':
        troop = Troops()
        troop.spawn(p)
        every_troop.append(troop)
    elif p == 'e' or p == 'r':
        spell = Spell(p)
        spell.start(king,every_troop)

    for i in range(0,50):
        base[i][0]='.'
        base[i][49]='.'
    for i in range(0,50):
        base[0][i]='.'
        base[49][i]='.'
    base[20][0] = '1'
    base[0][35] = '2'
    base[40][49] = '3'
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
    # print(".................................................................................")
    # print(p)
    # print(".................................................................................")
    print('|' + Back.GREEN + green_bar + Back.RED + red_bar + Back.RESET + '|')
        
    # print("------------")
    # print(gems_arr)
    # print("------------")
    print()
    time.sleep(0.1)