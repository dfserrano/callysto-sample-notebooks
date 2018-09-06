othello.py

import pygame
import sys
import random
import time
import copy
from pygame.locals import *
pygame.init()

#defineing the screen of size 640,480
screen = pygame.display.set_mode((640,480))


#defining the sizes of the artributes of the board and the screen
#color definations(WE GOT A DIFFERENT VARIETY OF COLOURS)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 200, 200)
BRIGHTBLUE = ( 0,50,255)
BROWN = (174, 94, 0)

#This dictionary stores all the coordinates of the boxes 
EMPTY = {'A1':[(145, 65)], 'A2':[(145, 115)], 'A3': [(145, 165)], 'A4':[(145, 215)],'A5':[(145, 265)],'A6':[(145,315)],'A7':[(145,365)],'A8':[(145,415)],
         'B1':[(195,65)],'B2':[(195,115)],'B3':[(195,165)],'B4':[(195,215)],'B5':[(195,265)],'B6':[(195,315)],'B7':[(195,365)],'B8':[(195,415)],
         'C1':[(245,65)],'C2':[(245,115)],'C3':[(245,165)],'C4':[(245,215)],'C5':[(245,265)],'C6':[(245,315)],'C7':[(245,365)],'C8':[(245,415)],
         'D1':[(295,65)],'D2':[(295,115)],'D3':[(295,165)],'D4':[(295,215)],'D5':[(295,265)],'D6':[(295,315)],'D7':[(295,365)],'D8':[(295,415)],
         'E1':[(345,65)],'E2':[(345,115)],'E3':[(345,165)],'E4':[(345,215)],'E5':[(345,265)],'E6':[(345,315)],'E7':[(345,365)],'E8':[(345,415)],
         'F1':[(395,65)],'F2':[(395,115)],'F3':[(395,165)],'F4':[(395,215)],'F5':[(395,265)],'F6':[(395,315)],'F7':[(395,365)],'F8':[(395,415)],
         'G1':[(445,65)],'G2':[(445,115)],'G3':[(445,165)],'G4':[(445,215)],'G5':[(445,265)],'G6':[(445,315)],'G7':[(445,365)],'G8':[(445,415)],
         'H1':[(495,65)],'H2':[(495,115)],'H3':[(495,165)],'H4':[(495,215)],'H5':[(495,265)],'H6':[(495,315)],'H7':[(495,365)],'H8':[(495,415)]}

#0=None
#1 = BLACK
#2 = White

for i  in EMPTY:
    EMPTY[i].append(0)
EMPTY['D4'][1] = 2
EMPTY['E4'][1] = 1
EMPTY['D5'][1] = 1
EMPTY['E5'][1] = 2
#the player always starts the game so we initilize the turn as player 1 
turn = "player1"

#Main loop where all our functions are called
def main():
    global MAINCLOCK
    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    title()
    time.sleep(2)
    askplayer()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
#Draws the tittle page
def title():
    screen.fill(BLUE)
    pygame.display.set_caption('Othello by  Kathleen Pescador and Abuni Gaiya ')
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    textsurface = myfont.render('Othello', False, WHITE)
    screen.blit(textsurface,(100,100))
    pygame.display.update()
#Draws the board 
def drawbackground():
    screen.fill(BROWN)
    othfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = othfont.render('OTHELLO', False, WHITE)
    screen.blit(textsurface,(275,20))
    pygame.draw.rect(screen, GREEN, (120,40,400,400),0)
    for i in [170, 220, 270, 320, 370, 420, 470]: # vertical lines
        pygame.draw.lines(screen, BLACK, False, [(i,40),(i,440)],1)
    for j in [90, 140, 190, 240, 290, 340, 390]: # horizontal lines
        pygame.draw.lines(screen, BLACK, False, [(120,j),(520,j)],1)
    pygame.draw.circle(screen, WHITE, (295 ,215), 23, 0)
    pygame.draw.circle(screen, WHITE, (345,265), 23, 0)
    pygame.draw.circle(screen, BLACK, (295,265), 23, 0)
    pygame.draw.circle(screen, BLACK, (345,215), 23, 0)
    pygame.display.update()

#Finds out what mode the player wants to play with and takes the player to the mode
def askplayer():
    screen.fill(WHITE)
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 24)
    textsurface = myfont.render('Would you like to play against the computer or a friend ?', False, BLACK)
    screen.blit(textsurface,(0,10))
    computer_button = pygame.draw.rect(screen,BRIGHTBLUE,(200,200,300,50));
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    comp = myfont.render('2 Players', False, BLACK)
    screen.blit(comp,(100,160))
    players_button = pygame.draw.rect(screen,PINK,(100,200,200,50))
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    play = myfont.render(' Vs Computer', False, BLACK)
    screen.blit(play,(310,160))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if players_button.collidepoint(mouse_pos):
                    time.sleep(2)

                    drawbackground()
                    gamemode2players()
                elif computer_button.collidepoint(mouse_pos):
                    time.sleep(2)

                    drawbackground()
                    gamemodecomputer()
                else:
                    pass
#This functions declaares the game is over and displays the winner
def gameover():
    pygame.draw.rect(screen,BRIGHTBLUE,(100,140,450,200));
    pygame.font.init()
    numfont = pygame.font.SysFont('Comic Sans MS', 45)
    wonfont = pygame.font.SysFont('Comic Sans MS', 80)
    tiefont = pygame.font.SysFont('Comic Sans MS', 50)
    white_tiles = 0
    black_tiles = 0
    # then checks who won
    for key, val in EMPTY.items():
        if val[1] == 1:
            black_tiles += 1
        elif val[1] == 2:
            white_tiles += 1

    if white_tiles > black_tiles:
        textsurface = numfont.render('THERE ARE ' + str(white_tiles) + ' WHITE TILES,', False, WHITE)
        screen.blit(textsurface,(110,180))
        textsurface = wonfont.render('WHITE WON!!!', False, WHITE)
        screen.blit(textsurface,(130,240))
    elif black_tiles > white_tiles:
        textsurface = numfont.render('THERE ARE ' + str(black_tiles) + ' BLACK TILES,', False, WHITE)
        screen.blit(textsurface,(110,180))
        textsurface = wonfont.render('BLACK WON!!!', False, WHITE)
        screen.blit(textsurface,(130,240))
    else:
        textsurface = tiefont.render('OOOPS ITS A TIE...', False, WHITE)
        screen.blit(textsurface,(130,220))
    pygame.display.update()

def drawwhitecircle(x,y):
    pygame.draw.circle(screen,WHITE, (x,y), 23, 0)
    pygame.display.update()

def drawblackcircle(x,y):
    pygame.draw.circle(screen, BLACK, (x,y), 23, 0)
    pygame.display.update()

def tileChange1(key, zo):
    itm = EMPTY[key]
    xo = itm[0][0]  # initial
    yo = itm[0][1]
    reached = False
    check = 0
    check2 = 0
    temp = [] # temp storage of coord while checking if it's reached or not

    while reached is False:
        yo -= 50
        if yo < 40:
            break
        for keys,value in EMPTY.items():
            if value[0][0] == xo and value[0][1] == yo:
                znew = value[1]
                if znew == zo: # if same colour as the initial placed tile
                    reached = True


                elif znew == 0:  # no tiles
                    check += 1

                    break
                else:
                    temp.append([(value[0][0],value[0][1]), keys])
                    check2 += 1

        if check != 0:
            break
        if check2!= 0:
            continue

    if reached is True:
        for k in temp:
            rKey = k[1]
            x = k[0][0]
            y = k[0][1]
            if znew == 1:
                drawblackcircle(x,y)
                EMPTY[rKey].insert(1,1)
            elif znew == 2:
                drawwhitecircle(x,y)
                EMPTY[rKey].insert(1,2)
            else:
                pass

def tileChange2(key, zo): # DOWNWARDS CHECKING
    itm = EMPTY[key]
    xo = itm[0][0]  # initial
    yo = itm[0][1]
    reached = False
    check = 0
    check2 = 0
    temp = [] # temp storage of coord while checking if it's reached or not

    while reached is False:
        yo += 50
        if yo > 440:
            break
        for keys,value in EMPTY.items():
            if value[0][0] == xo and value[0][1] == yo:
                znew = value[1]
                if znew == zo: # if same colour as the initial placed tile
                    reached = True


                elif znew == 0:  # no tiles
                    check += 1

                    break
                else:
                    temp.append([(value[0][0],value[0][1]), keys])
                    check2 += 1

        if check != 0:
            break
        if check2!= 0:
            continue

    if reached is True:
        for k in temp:
            rKey = k[1]

            x = k[0][0]
            y = k[0][1]
            if znew == 1:
                drawblackcircle(x,y)
                EMPTY[rKey].insert(1,1)
            elif znew == 2:
                drawwhitecircle(x,y)
                EMPTY[rKey].insert(1,2)
            else:
                pass



def tileChange3(key, zo): #RIGHTWARDS CHECKING
    itm = EMPTY[key]
    xo = itm[0][0]  # initial
    yo = itm[0][1]
    reached = False
    temp = [] # temp storage of coord while checking if it's reached or not
    check = 0
    check2 = 0
    while reached is False:
        xo += 50
        if xo > 520:
            break
        for keys,value in EMPTY.items():
            if value[0][0] == xo and value[0][1] == yo:
                znew = value[1]
                if znew == zo: # if same colour as the initial placed tile
                    reached = True

                elif znew == 0:  # no tiles

                    check += 1
                    break
                else:
                    temp.append([(value[0][0],value[0][1]), keys])
                    check2 += 1

        if check != 0:
            break
        if check2!= 0:
            continue

    if reached is True:
        for k in temp:
            rKey = k[1]
            x = k[0][0]
            y = k[0][1]
            if znew == 1:
                drawblackcircle(x,y)
                EMPTY[rKey].insert(1,1)
            elif znew == 2:
                drawwhitecircle(x,y)
                EMPTY[rKey].insert(1,2)
            else:
                pass

def tileChange4(key, zo): # LEFT CHECKING
    itm = EMPTY[key]
    xo = itm[0][0]  # initial
    yo = itm[0][1]
    reached = False
    check = 0
    check2 = 0
    temp = [] # temp storage of coord while checking if it's reached or not

    while reached is False: # LEFTWARDS CHECKING
        xo -= 50
        if xo < 120:
            break
        for keys,value in EMPTY.items():
            if value[0][0] == xo and value[0][1] == yo:
                znew = value[1]
                if znew == zo: # if same colour as the initial placed tile

                    reached = True

                elif znew == 0:  # no tiles

                    check += 1
                    reached = True
                    break
                else:
                    temp.append([(value[0][0],value[0][1]), keys])
                    check2 += 1

        if check != 0:
            break
        if check2!= 0:
            continue

    if reached is True:
        for k in temp:
            rKey = k[1]
            x = k[0][0]
            y = k[0][1]
            if znew == 1:
                drawblackcircle(x,y)
                EMPTY[rKey].insert(1,1)
            elif znew == 2:
                drawwhitecircle(x,y)
                EMPTY[rKey].insert(1,2)

def tileChange5(key, zo): #  DIAGONAL RIGHT UP
    itm = EMPTY[key]
    xo = itm[0][0]  # initial
    yo = itm[0][1]
    reached = False
    check = 0
    check2 = 0
    temp = [] # temp storage of coord while checking if it's reached or not

    while reached is False: # LEFTWARDS CHECKING
        xo += 50
        yo -= 50
        if xo > 520:
            break
        if yo < 40:
            break
        for keys,value in EMPTY.items():
            if value[0][0] == xo and value[0][1] == yo:
                znew = value[1]
                if znew == zo: # if same colour as the initial placed tile

                    reached = True

                elif znew == 0:  # no tiles

                    check += 1
                    reached = True
                    break
                else:
                    temp.append([(value[0][0],value[0][1]), keys])
                    check2 += 1

        if check != 0:
            break
        if check2!= 0:
            continue

    if reached is True:
        for k in temp:
            rKey = k[1]
            x = k[0][0]
            y = k[0][1]
            if znew == 1:
                drawblackcircle(x,y)
                EMPTY[rKey].insert(1,1)
            elif znew == 2:
                drawwhitecircle(x,y)
                EMPTY[rKey].insert(1,2)

def tileChange6(key, zo): # DIAGONAL LEFT UP
    itm = EMPTY[key]
    xo = itm[0][0]  # initial
    yo = itm[0][1]
    reached = False
    check = 0
    check2 = 0
    temp = [] # temp storage of coord while checking if it's reached or not

    while reached is False: # LEFTWARDS CHECKING
        xo -= 50
        yo -= 50
        if xo < 120:
            break
        if yo < 40:
            break
        for keys,value in EMPTY.items():
            if value[0][0] == xo and value[0][1] == yo:
                znew = value[1]
                if znew == zo: # if same colour as the initial placed tile

                    reached = True

                elif znew == 0:  # no tiles

                    check += 1
                    reached = True
                    break
                else:
                    temp.append([(value[0][0],value[0][1]), keys])
                    check2 += 1

        if check != 0:
            break
        if check2!= 0:
            continue

    if reached is True:
        for k in temp:
            rKey = k[1]
            x = k[0][0]
            y = k[0][1]
            if znew == 1:
                drawblackcircle(x,y)
                EMPTY[rKey].insert(1,1)
            elif znew == 2:
                drawwhitecircle(x,y)
                EMPTY[rKey].insert(1,2)

def tileChange7(key, zo): # DIAGONAL RIGHT DOWN
    itm = EMPTY[key]
    xo = itm[0][0]  # initial
    yo = itm[0][1]
    reached = False
    check = 0
    check2 = 0
    temp = [] # temp storage of coord while checking if it's reached or not

    while reached is False: # LEFTWARDS CHECKING
        xo += 50
        yo += 50
        if xo > 520:
            break
        if yo > 440:
            break
        for keys,value in EMPTY.items():
            if value[0][0] == xo and value[0][1] == yo:
                znew = value[1]
                if znew == zo: # if same colour as the initial placed tile

                    reached = True

                elif znew == 0:  # no tiles

                    check += 1
                    reached = True
                    break
                else:
                    temp.append([(value[0][0],value[0][1]), keys])
                    check2 += 1

        if check != 0:
            break
        if check2!= 0:
            continue

    if reached is True:
        for k in temp:
            rKey = k[1]
            x = k[0][0]
            y = k[0][1]
            if znew == 1:
                drawblackcircle(x,y)
                EMPTY[rKey].insert(1,1)
            elif znew == 2:
                drawwhitecircle(x,y)
                EMPTY[rKey].insert(1,2)

def tileChange8(key, zo): # DIAGONAL LEFT DOWN
    itm = EMPTY[key]
    xo = itm[0][0]  # initial
    yo = itm[0][1]
    reached = False
    check = 0
    check2 = 0
    temp = [] # temp storage of coord while checking if it's reached or not

    while reached is False: # LEFTWARDS CHECKING
        xo -= 50
        yo += 50
        if xo < 120:
            break
        if yo > 440:
            break
        for keys,value in EMPTY.items():
            if value[0][0] == xo and value[0][1] == yo:
                znew = value[1]
                if znew == zo: # if same colour as the initial placed tile

                    reached = True

                elif znew == 0:  # no tiles

                    check += 1
                    reached = True
                    break
                else:
                    temp.append([(value[0][0],value[0][1]), keys])
                    check2 += 1

        if check != 0:
            break
        if check2!= 0:
            continue

    if reached is True:
        for k in temp:
            rKey = k[1]
            x = k[0][0]
            y = k[0][1]
            if znew == 1:
                drawblackcircle(x,y)
                EMPTY[rKey].insert(1,1)
            elif znew == 2:
                drawwhitecircle(x,y)
                EMPTY[rKey].insert(1,2)

def isvalidmove(x,y):
    xmore = x + 50
    ymore = y + 50
    yless = y - 50
    xless = x - 50


    for key, value in EMPTY.items():
        if (value[0][0] == xless and value[0][1]==yless) and value[1]> 0:
            return True

        elif (value[0][0] == xless and value[0][1]==y) and value[1]> 0:
            return True
        elif (value[0][0] == xless and value[0][1]== ymore) and value[1]> 0:
            return True
        elif (value[0][0] == x and value[0][1]== ymore) and value[1]> 0:
            return True
        elif (value[0][0] == xmore and value[0][1]==ymore) and value[1]> 0:
            return True
        elif (value[0][0] == xmore and value[0][1]== y) and value[1]> 0:
            return True
        elif (value[0][0] == xmore and value[0][1]== yless) and value[1]> 0:
            return True
        elif (value[0][0] == x and value[0][1]== yless) and value[1]> 0:
            return True
        else:
            pass

def getValidBlack():
    occupied = []
    for k,v in EMPTY.items():
        xlow = v[0][0] - 50
        xhigh = v[0][0] + 50
        ylow = v[0][1] - 50
        yhigh = v[0][1] + 50
        if v[1] == 2 :
         #Putting all the occuppied spots in here
            occupied.append(v[0])
      
        else:
            pass
    #Now we need to check all the tiles arround the occupied to make sure they are valid
    valid = set()# returns a list of all valid moves at the moment
    for i in occupied:
        x = i[0]
        y = i[1]
        xless = i[0] - 50
        xmore = i[0] + 50
        yless = i[1] - 50
        ymore = i[1] + 50
        for key,value in EMPTY.items():
            if value[1] == 0:
                if (value[0][0] == xless and value[0][1]==yless) :
                    valid.add(value[0])

                if (value[0][0] == xless and value[0][1]==y) :
                    valid.add(value[0])

                if (value[0][0] == xless and value[0][1]== ymore):
                    valid.add(value[0])

                if (value[0][0] == x and value[0][1]== ymore) :
                    valid.add(value[0])

                if (value[0][0] == xmore and value[0][1]==ymore) :
                    valid.add(value[0])

                if (value[0][0] == xmore and value[0][1]== y):
                    valid.add(value[0])

                if (value[0][0] == xmore and value[0][1]== yless):
                    valid.add(value[0])
                if (value[0][0] == x and value[0][1]== yless):
                    valid.add(value[0])

    validlist = list(valid)
    return validlist

def getValidWhite():
    valid = set() # returns a list of all valid moves at the moment
    occupied = []
    for k,v in EMPTY.items():
        xlow = v[0][0] - 50
        xhigh = v[0][0] + 50
        ylow = v[0][1] - 50
        yhigh = v[0][1] + 50
        if v[1] == 0 :
         #Putting all the occuppied spots in here
            occupied.append(v)
        else:
            pass
    #Gets the valid moves 
    for i in occupied:
        x = i[0][0]
        y = i[0][1]
        xless = i[0][0] - 50
        xmore = i[0][0] + 50
        yless = i[0][1] - 50
        ymore = i[0][1] + 50
        for key,value in EMPTY.items():
            if value[1] == 0:
                if (value[0][0] == xless and value[0][1]==yless) :
                    valid.add(value[0])
                if (value[0][0] == xless and value[0][1]==y) :
                    valid.add(value[0])
                if (value[0][0] == xless and value[0][1]== ymore):
                    valid.add(value[0])
                if (value[0][0] == x and value[0][1]== ymore) :
                    valid.add(value[0])
                if (value[0][0] == xmore and value[0][1]==ymore) :
                    valid.add(value[0])
                if (value[0][0] == xmore and value[0][1]== y):
                    valid.add(value[0])
                if (value[0][0] == xmore and value[0][1]== yless):
                    valid.add(value[0])
                if (value[0][0] == x and value[0][1]== yless):
                    valid.add(value[0])

    validlist = list(valid)
    return validlist
#Checks if the tile is a corner
def iscorner(x,y):
    if(x ==145 and y == 65) or (x == 495 and y == 65) or (x == 145 and y == 415) or (x == 495 and y==415):
        return True
    
#Checks if the tile is by a wall
def isWall(x,y):
    if(x==145) or (y==65) or (x==495) or (y == 415):
        return True
    

#This is the function that computes what moves the computer makes we used the Monte Carlo Algorithm for function 
def compMove():
    validmoves = getValidBlack()
    validW = getValidWhite()
    bestlist = []
    '''
    We also tired some cases whereby the computer tired to stop the player from taking the good spots however for this game those cases seemed to work against us because unlike game like chess , any move you make to stop your opponent from winning ends up creating a better move for your opponent as it creates an bigger pile.
    '''
    #Case 1: By the monte carlo algorithm this is the backup stage, when the whole board is full of white checkers and black has no other option but to #play anywhere.
    
    if validmoves == []:
        return random.choice(validW)
    else:
    #Case 2: We took the corners as our priority spots, whenever we could play in a corner we played the not considering any other thing
        for i in validmoves:
            best = 0
            if iscorner(i[0],i[1]) is True:
                return i
            else:
                for v in EMPTY.values():
                    if v[0][0] == i[0] and v[0][1] == i[1]:
                        zo = v[1]
                        xo = i[0]
                        yo = i[1]
                        up = 0
                        down = 0
                        leftup = 0
                        leftdown = 0
                        left = 0
                        right = 0
                        rightup = 0
                        rightdown = 0

                        reachedup = False
                        reacheddown = False
                        reachedright = False
                        reachedleft = False
                        reachedleftup = False
                        reachedrightup = False
                        reachedleftdown = False
                        reachedrightdown = False
                        #CHECKING CASES
                        #UP
                        check = 0
                        while reachedup is False:
                            yo -= 50
                            up += 1
                            if yo < 40:
                                break
                            for keys,value in EMPTY.items():
                                if value[0][0] == xo and value[0][1] == yo:
                                    znew = value[1]
                                    if znew == 1: # if same colour as the initial placed tile
                                        reachedup = True

                                    elif znew == 0:  # no tiles
                                        check += 1
                                        up = 0
                                        break
                                    else:
                                        pass
                        if up > best:
                            best = up

                        #DOWN
                        check = 0
                        check2 =0
                        while reacheddown is False:
                            yo += 50
                            down += 1
                            if yo > 440:
                                break
                            for keys,value in EMPTY.items():
                                if value[0][0] == xo and value[0][1] == yo:
                                    znew = value[1]
                                    if znew == 1: # if same colour as the initial placed tile
                                        reached = True
                                    elif znew == 0:  # no tiles
                                        check += 1
                                        down = 0
                                        break
                                    else:
                                        check2 +=1
                            if check != 0:
                                break
                            if check2 !=0:
                                continue
                        if down > best:
                            best = down

                        #RIGHT
                        check =0
                        while reachedright is False:
                            xo += 50
                            right += 1
                            if xo > 520:
                                break
                            for keys,value in EMPTY.items():
                                if value[0][0] == xo and value[0][1] == yo:
                                    znew = value[1]
                                    if znew == 1: # if same colour as the initial placed tile
                                        reachedright=True
                                    elif znew == 0:  # no tiles
                                        check+= 1
                                        right = 0
                                        break
                                    else:
                                        pass
                            if check != 0:
                                break

                        if right> best:
                            best = right



                        #LEFT
                        check = 0
                        while reachedleft is False:# CHECKING
                            xo -= 50
                            left += 1
                            if xo < 120:
                                break
                            for keys,value in EMPTY.items():
                                if value[0][0] == xo and value[0][1] == yo:
                                    znew = value[1]
                                    if znew == 1: # if same colour as the initial placed tile
                                        reachedleft = True
                                    elif znew == 0:  # no tiles
                                        check += 1
                                        left = 0
                                        break
                                    else:
                                        pass
                            if check != 0:
                                break

                        if left > best:
                            best = left


                                #RIGHTUP
                        check = 0
                        while reachedrightup is False: # LEFTWARDS CHECKING
                            xo += 50
                            yo -= 50
                            rightup +=1
                            if xo > 520:
                                break
                            if yo < 40:
                                break
                            for keys,value in EMPTY.items():
                                if value[0][0] == xo and value[0][1] == yo:
                                    znew = value[1]
                                    if znew == 1: # if same colour as the initial placed tile
                                        reachedrightup = True

                                    elif znew == 0:  # no tiles
                                        check +=1
                                        rightup = 0
                                        break
                                    else:
                                        pass
                            if check != 0:
                                break

                        if rightup> best:
                            best = rightup


                        #RIGHTDOWN
                        check = 0
                        while reachedrightdown is False: # LEFTWARDS CHECKING
                            xo += 50
                            yo += 50
                            rightdown += 1
                            if xo > 520:
                                break
                            if yo > 440:
                                break
                            for keys,value in EMPTY.items():
                                if value[0][0] == xo and value[0][1] == yo:
                                    znew = value[1]
                                    if znew == 1: # if same colour as the initial placed tile
                                        reachedrigthtdown = True

                                    elif znew == 0:  # no tiles
                                        check +=1
                                        rightdown = 0
                                        break
                                    else:
                                        pass
                            if check != 0:
                                break
                        if rightdown > best:
                            best = rightdown


                        #LEFTUP
                        check = 0
                        while reachedleftup is False: # LEFTWARDS CHECKING
                            xo -= 50
                            yo -= 50
                            leftup += 1
                            if xo < 120:
                                break
                            if yo < 40:
                                break
                            for keys,value in EMPTY.items():
                                if value[0][0] == xo and value[0][1] == yo:
                                    znew = value[1]
                                    if znew == 1: # if same colour as the initial placed tile
                                        reachedleftup = True
                                    elif znew == 0:  # no tiles
                                        check+=1
                                        leftup = 0
                                        break
                                    else:
                                        pass
                            if check != 0:
                                break
                        if leftup > best:
                                best = leftup

                        #LEFTDOWN
                        check = 0
                        while reachedleftdown is False: # LEFTWARDS CHECKING
                            xo -= 50
                            yo += 50
                            leftdown += 1
                            if xo < 120:
                                break
                            if yo > 440:
                                break
                            for keys,value in EMPTY.items():
                                if value[0][0] == xo and value[0][1] == yo:
                                    znew = value[1]
                                    if znew == 1: # if same colour as the initial placed tile
                                        reachedleftdown = True

                                    elif znew == 0:  # no tile
                                        check+=1
                                        leftdown = 0
                                        break
                                    else:
                                        pass
                            if check != 0:
                                break
                        if leftdown > best:
                            best = leftdown

                        bestlist.append(best)
        #This loop gets the best out of the best of the possible moves    
        for j in bestlist:
            if j == max(bestlist):
                c = bestlist.index(j)
        #Case 3: The wall was our second priority but what we can't just play on any spot on the wall so we got the best spots on the wall her to play on
                if isWall(validmoves[c][0],validmoves[c][1]):
                    return validmoves[c]
        #If there was no benefit of playing on the available spots on the wall we still play the because this is always a better move
                elif isWall(i[0],i[1]) is True:
                    return i
                else:
                    return validmoves[c]
                    
                

def gamemode2players():
    # plays one round of the game each time this function is called
    tiles_counter = 0
    turn = 'player1'
    while True:
        if tiles_counter == 30:
            gameover()
            break
        if(turn == "player1"):
            overlap= pygame.draw.rect(screen,BROWN,(250,445,300,40));
            wfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = wfont.render('WHITE TURN', False, WHITE)
            screen.blit(textsurface,(260,450))
            pygame.display.update()
            if any(EMPTY):
                while(turn == "player1"):
                    # get all events
                    ev = pygame.event.get()
                    # proceed events
                    for event in ev:
                        # handle MOUSEBUTTONUP
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            #drawblackcircle(pos[0],pos[1])
                            #pygame.draw.circle(screen, BLACK, (300,60), 23, 0)
                            for x in range(pos[0]-25, pos[0] + 25):
                                for y in range(pos[1]-25, pos[1]+25):
                                    for z in range(2):
                                        if z == 0:
                                            if [(x, y),z] in EMPTY.values():
                                                for key,value in EMPTY.items():
                                                    if value[0] == (x,y) and value[1] == z and isvalidmove(x,y) :

                                                        EMPTY[key].insert(1,2)
                                                        drawwhitecircle(x, y)
                                                        tileChange1(key, 2)
                                                        tileChange2(key, 2)
                                                        tileChange3(key, 2)
                                                        tileChange4(key, 2)
                                                        tileChange5(key, 2)
                                                        tileChange6(key, 2)
                                                        tileChange7(key, 2)
                                                        tileChange8(key, 2)
                                                        EMPTY[key].insert(1,2)
                                                        turn = "player2"

                                                        break
                                        else:
                                            pass
                    break

            else:
                gameover()
                break

        if(turn == "player2"):
            overlap= pygame.draw.rect(screen, BROWN,(250,445,300,40));
            bfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = wfont.render('BLACK TURN', False, BLACK)
            screen.blit(textsurface,(260,450))
            pygame.display.update()
            if any(EMPTY):
                while(turn == "player2"):
                    # get all events
                    ev = pygame.event.get()
                    # proceed events
                    for event in ev:
                        # handle MOUSEBUTTONUP
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            for x in range(pos[0]-25, pos[0] + 25):
                                for y in range(pos[1]-25, pos[1]+25):
                                    for z in range(2):
                                        if z == 0:
                                            if [(x, y),z] in EMPTY.values():
                                                for key,value in EMPTY.items():
                                                    if value[0] == (x,y) and value[1] == z and isvalidmove(x,y):

                                                        EMPTY[key].insert(1,1)
                                                        drawblackcircle(x, y)
                                                        tiles_counter = tiles_counter + 1
                                                        tileChange1(key, 1)
                                                        tileChange2(key, 1)
                                                        tileChange3(key, 1)
                                                        tileChange4(key, 1)
                                                        tileChange5(key, 1)
                                                        tileChange6(key, 1)
                                                        tileChange7(key, 1)
                                                        tileChange8(key, 1)
                                                        EMPTY[key].insert(1,1)
                                                        turn = "player1"

                                                        break
                                        else:
                                            pass


                    break
            else:
                gameover()
                break


def gamemodecomputer():
    turn = 'player1' # white tiles
    tiles_counter = 0
    while True:
        if tiles_counter == 30:
            gameover()
            break
        if(turn == "player1"):
            overlap= pygame.draw.rect(screen,BROWN,(200,445,300,40));
            wfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = wfont.render('WHITE TURN', False, WHITE)
            screen.blit(textsurface,(260,450))
            pygame.display.update()
            if any(EMPTY):
                while(turn == "player1"):
                    # get all events
                    ev = pygame.event.get()
                    # proceed events
                    for event in ev:
                        # handle MOUSEBUTTONUP
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            for x in range(pos[0]-25, pos[0] + 25):
                                for y in range(pos[1]-25, pos[1]+25):
                                    for z in range(2):
                                        if z == 0:
                                            if [(x, y),z] in EMPTY.values():
                                                for key,value in EMPTY.items():
                                                    if value[0] == (x,y) and value[1] == z and isvalidmove(x,y):
                                                        EMPTY[key].insert(1,2)
                                                        drawwhitecircle(x, y)
                                                        tileChange1(key, 2)
                                                        tileChange2(key, 2)
                                                        tileChange3(key, 2)
                                                        tileChange4(key, 2)
                                                        tileChange5(key, 2)
                                                        tileChange6(key, 2)
                                                        tileChange7(key, 2)
                                                        tileChange8(key, 2)
                                                        EMPTY[key].insert(1,2)
                                                        turn = "computer"
                                        else:
                                            pass
                    break
                else:
                    gameover()
                    break
            if(turn == "computer"):
                overlap= pygame.draw.rect(screen, BROWN,(200,445,300,40));
                bfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = wfont.render('COMPUTER (BLACK) TURN', False, BLACK)
                screen.blit(textsurface,(200,450))
                pygame.display.update()
                pauseUntil = time.time() + random.randint(5, 15) * 0.1
                while time.time() < pauseUntil:
                    pygame.display.update()
                if any(EMPTY):
                    while(turn == "computer"):
                        move = compMove()
                        x = move[0]
                        y = move[1]
                        drawblackcircle(x,y)
                        tiles_counter = tiles_counter + 1
                        for key,value in EMPTY.items():
                            if move[0] == value[0][0] and move[1] == value[0][1]:
                                EMPTY[key].insert(1,1)
                                tileChange1(key, 1)
                                tileChange2(key, 1)
                                tileChange3(key, 1)
                                tileChange4(key, 1)
                                tileChange5(key, 1)
                                tileChange6(key, 1)
                                tileChange7(key, 1)
                                tileChange8(key, 1)
                                EMPTY[key].insert(1,1)
                                turn = "player1"

                else:

                    gameover()
                    break


if __name__ == '__main__':
    main()