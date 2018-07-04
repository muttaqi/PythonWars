import string
import random
import time

#board
board1 =  list("    A     B     C     D     E \n")
board2 =  list("        _ _ _ _ _ _ _ _ _ \n")
board3 =  list(" P1    I     I C C I     I \n")
board4 =  list("       I     I  5  I     I          1 \n")
board5 =  list("  _ _ _I_ _ _I_C_C_I_ _ _I_ _ _ \n")
board6 =  list(" I     I     I     I     I     I \n")
board7 =  list(" I     I     I     I     I     I    2 \n")
board8 =  list(" I_ _ _I_ _ _I_ _ _I_ _ _I_ _ _I \n")
board9 =  list(" I     I     I     I     I     I \n")
board10 = list(" I     I     I     I     I     I    3 \n")
board11 = list(" I_ _ _I_ _ _I_ _ _I_ _ _I_ _ _I \n")
board12 = list(" I     I     I     I     I     I \n")
board13 = list(" I     I     I     I     I     I    4 \n")
board14 = list(" I_ _ _I_ _ _I_ _ _I_ _ _I_ _ _I \n")
board15 = list("       I     I C C I     I \n")
board16 = list("       I     I  5  I     I          5 \n")
board17 = list(" P2    I_ _ _I_C_C_I_ _ _I \n")

#initializing turn count, which increases after every iteration of the game loop
turnCount = -1

#stores inputs
specAnswer = 0
spawnAnswer = 0
unitPosAnswer = 0
unitMovAnswer = 0

#used to check if a unit is present in the selected tile when moving (unitPosAnswer)
unitPresent = False

# a bunch of random x and y's, used for mountains and rivers
randx1 = random.randint(1, 5)
randx2 = random.randint(1, 5)
randx3 = random.randint(1, 5)
randx4 = random.randint(1, 5)
randx5 = random.randint(1, 5)
randx6 = random.randint(1, 5)
randx7 = random.randint(1, 5)
randx8 = random.randint(1, 5)

randy1 = random.randint(1, 5)
randy2 = random.randint(1, 5)
randy3 = random.randint(1, 5)
randy4 = random.randint(1, 5)
randy5 = random.randint(1, 5)
randy6 = random.randint(1, 5)
randy7 = random.randint(1, 5)
randy8 = random.randint(1, 5)

#store random x's and y's in a list for simplicity
randXs = [randx1, randx2, randx3, randx4, randx5, randx6, randx7, randx8]
randYs = [randy1, randy2, randy3, randy4, randy5, randy6, randy7, randy8]

#stores unit information
p1u1 = [-1, 0, 0, 2, 'F', 1]
p1u2 = [-1, 0, 0, 2, 'F', 1]
p1u3 = [-1, 0, 0, 2, 'F', 1]
p1u4 = [-1, 0, 0, 2, 'F', 1]
p1u5 = [-1, 0, 0, 2, 'F', 1]
p1u6 = [-1, 0, 0, 2, 'F', 1]

p2u1 = [-1, 0, 0, 2, 'F', 2]
p2u2 = [-1, 0, 0, 2, 'F', 2]
p2u3 = [-1, 0, 0, 2, 'F', 2]
p2u4 = [-1, 0, 0, 2, 'F', 2]
p2u5 = [-1, 0, 0, 2, 'F', 2]
p2u6 = [-1, 0, 0, 2, 'F', 2]

#store unit info in a list for simplicity
unitList = [p1u1, p1u2, p1u3, p1u4, p1u5, p1u6, p2u1, p2u2, p2u3, p2u4, p2u5, p2u6]

#used for when a unit is on a mountain
p1u1Mountain = False
p1u2Mountain = False
p1u3Mountain = False
p1u4Mountain = False
p1u5Mountain = False
p1u6Mountain = False

p2u1Mountain = False
p2u2Mountain = False
p2u3Mountain = False
p2u4Mountain = False
p2u5Mountain = False
p2u6Mountain = False

#store info in a list for simplicity
unitMountainList = [p1u1Mountain, p1u2Mountain, p1u3Mountain, p1u4Mountain, p1u5Mountain, p1u6Mountain, p2u1Mountain, p2u2Mountain, p2u3Mountain, p2u4Mountain, p2u5Mountain, p2u6Mountain]

#do same for rivers
p1u1River = False
p1u2River = False
p1u3River = False
p1u4River = False
p1u5River = False
p1u6River = False

p2u1River = False
p2u2River = False
p2u3River = False
p2u4River = False
p2u5River = False
p2u6River = False

unitRiverList = [p1u1River, p1u2River, p1u3River, p1u4River, p1u5River, p1u6River, p2u1River, p2u2River, p2u3River, p2u4River, p2u5River, p2u6River]

#initialize capital health
capitalP1 = 5
capitalP2 = 5

#initialize assassin bool(used for assassin ability)
assassinSelected = False

#used to check inputs
def isInt(s):
    #try to turn into int
    try:
        int(s)
        #return true if it works
        return True
    #return false if not
    except ValueError:
        return False

#check if unit is on a terrain tile
def checkTerrain():
    global unitRiverList
    global unitMountainList

    #for each river co-ordinate
    for i in range(0,4):
        #for each unit
        for j in range(0, 11):
            #check if co-ordinates match
            if unitList[j][0] == randXs[i] and unitList[j][1] == randYs[i]:
                #trigger corresponding boolean
                unitRiverList[j] = True

    #same but for mountain
    for i in range(4, 8):
        for j in range(0, 11):
            if unitList[j][0] == randXs[i] and unitList[j][1] == randYs[i]:
                unitMountainList[j] = True

#apply terrain buffs
def applyTerrain():
    global unitRiverList
    global unitMountainList

    #if it is the start of a full turn
    if turnCount % 10 == 0 or turnCount % 10 == 3 or turnCount % 10 == 6 or turnCount % 10 == 8:
        for i in range(0, 6):
            #if boolean is true then increase hp with a max hp of 3 for normal units and 5 for special units(since every other unit is special)
            if unitRiverList[i * 2] == True and unitList[i * 2][3] < 3:
                unitList[i * 2][3] += 1

            if unitRiverList[i * 2 + 1] == True and unitList[i * 2 + 1][3] < 5:
                unitList[i * 2 + 1][3] += 1

    #same but for mountains, apply hp and atk buff
    for i in range(0, 12):
        if unitMountainList[i] == True:
            unitList[i][2] += 1
            unitList[i][3] += 1

#since mountain tile is only temporary, every turn it must be removed
def removeMountain():
    global unitRiverList
    global unitMountainList

    #for each mountain boolean
    for i in range(0, 12):
        #if true then remove buff
        if unitMountainList[i] == True:
            unitList[i][2] -= 1

            #only remove health buff if it is greater than 1(so you don't die just from exiting a mountain)
            if unitList[i][3] > 1:
                unitList[i][3] -= 1

#check if unit is present in specified co-ordinates
def checkForUnit(x, y):
    global unitPresent

    #for each unit
    for i in range(0, 12):
        #if unit is on specified co-ordinates
        if unitList[i][0] == x and unitList[i][1] == y:
            #trigger boolean
            unitPresent = True

#draw capital health
def drawCapitals():
    board4[16] = capitalP1
    board16[16] = capitalP2

#draws the board itself, used after every action to update the board
def drawBoard():

    #concatonate all lines
    board = board1 + board2 + board3 + board4 + board5 + board6 + board7 + board8 + board9 + board10 + board11 + board12 + board13 + board14 + board15 + board16 + board17

    #print all lines
    print ("".join(str(v) for v in board))

#used at the start of the game to draw the rivers on
def boardRiver(x, y):

    #check if valid coordinate
    if y > 0 and x > 0:

        #if valid coordinates
        if y == 1:
            board3[x * 6 - 3] = "R"
            board3[x * 6 - 1] = "R"
            board5[x * 6 - 3] = "R"
            board5[x * 6 - 1] = "R"

        elif y == 2:
            board6[x * 6 - 3] = "R"
            board6[x * 6 - 1] = "R"
            board8[x * 6 - 3] = "R"
            board8[x * 6 - 1] = "R"

        elif y == 3:
            board9[x * 6 - 3] = "R"
            board9[x * 6 - 1] = "R"
            board11[x * 6 - 3] = "R"
            board11[x * 6 - 1] = "R"

        elif y == 4:
            board12[x * 6 - 3] = "R"
            board12[x * 6 - 1] = "R"
            board14[x * 6 - 3] = "R"
            board14[x * 6 - 1] = "R"

        elif y == 5:
            board15[x * 6 - 3] = "R"
            board15[x * 6 - 1] = "R"
            board17[x * 6 - 3] = "R"
            board17[x * 6 - 1] = "R"

#same with mountains
def boardMountain(x, y):

    if y > 0 and x > 0:
        if y == 1:
            board3[x * 6 - 3] = "M"
            board3[x * 6 - 1] = "M"
            board5[x * 6 - 3] = "M"
            board5[x * 6 - 1] = "M"

        elif y == 2:
            board6[x * 6 - 3] = "M"
            board6[x * 6 - 1] = "M"
            board8[x * 6 - 3] = "M"
            board8[x * 6 - 1] = "M"

        elif y == 3:
            board9[x * 6 - 3] = "M"
            board9[x * 6 - 1] = "M"
            board11[x * 6 - 3] = "M"
            board11[x * 6 - 1] = "M"

        elif y == 4:
            board12[x * 6 - 3] = "M"
            board12[x * 6 - 1] = "M"
            board14[x * 6 - 3] = "M"
            board14[x * 6 - 1] = "M"

        elif y == 5:
            board15[x * 6 - 3] = "M"
            board15[x * 6 - 1] = "M"
            board17[x * 6 - 3] = "M"
            board17[x * 6 - 1] = "M"    

#used to set up the board
def boardInit():
    global randXs
    global randYs

    #ensure no mountain and river co-ordinates are the same
    #for each river co-ordinates
    for i in range(0,4):
        #for each mountain co-ordinates
        for j in range(4, 8):
            #if they're the same
            if randXs[i] == randXs[j] and randYs[i] == randYs[j]:
                #set to zero (deactivating them)
                randXs[i] = 0
                randYs[i] = 0

    #ensure no co-ordinates are off the board(corners)
    #for each co-ordinates
    for i in range(0,8):
        #if invalid co-ordinates
        if (randXs[i] == 1 and randYs[i] == 1)or(randXs[i] == 1 and randYs[i] == 5) or (randXs[i] == 5 and randYs[i] == 1) or (randXs[i] == 5 and randYs[i] == 5) or (randXs[i] == 3 and randYs[i] == 1) or (randXs[i] == 3 and randYs[i] == 5):
            #set to zero
            randXs[i] = 0
            randYs[i] = 0
    
    #drawing river and mountain tiles
    for i in range(0, 4):
        boardRiver(randXs[i], randYs[i])

    for i in range(4, 8):
        boardMountain(randXs[i], randYs[i])

#draw unit
def drawUnit(x, y, atk, hp, unit, player):
    global turnCount

    #if unit has been deployed(-1 denotes that it hasn't)
    if not x == -1:

        #check if valid coordinate
        if x == 1 and y == 1:
            #let user know
            print ("Invalid Co-ordinates")
            #ask again
            turnCount -= 1

        elif x == 1 and y == 5:
            print ("Invalid Co-ordinates")
            turnCount -= 1

        elif x == 5 and y == 1:
            print ("Invalid Co-ordinates")
            turnCount -= 1

        elif x == 5 and y == 5:
            print ("Invalid Co-ordinates")
            turnCount -= 1

        elif x == 3 and y == 1:
            print ("Invalid Co-ordinates")
            turnCount -= 1


        elif x == 3 and y == 5:
            print ("Invalid Co-ordinates")
            turnCount -= 1

        #if valid coordinates, find y
        elif y == 1:
            #print corresponding information in the proper place
            board3[x * 6 - 4] = player
            board3[x * 6] = player
            board4[x * 6 - 2] = unit
            board4[x * 6] = atk
            board4[x * 6 - 4] = hp
            board5[x * 6 - 4] = player
            board5[x * 6] = player

        elif y == 2:
            board6[x * 6 - 4] = player
            board6[x * 6] = player
            board7[x * 6 - 2] = unit
            board7[x * 6] = atk
            board7[x * 6 - 4] = hp
            board8[x * 6 - 4] = player
            board8[x * 6] = player

        elif y == 3:
            board9[x * 6 - 4] = player
            board9[x * 6] = player
            board10[x * 6 - 2] = unit
            board10[x * 6] = atk
            board10[x * 6 - 4] = hp
            board11[x * 6 - 4] = player
            board11[x * 6] = player

        elif y == 4:
            board12[x * 6 - 4] = player
            board12[x * 6] = player
            board13[x * 6 - 2] = unit
            board13[x * 6] = atk
            board13[x * 6 - 4] = hp
            board14[x * 6 - 4] = player
            board14[x * 6] = player

        elif y == 5:
            board15[x * 6 - 4] = player
            board15[x * 6] = player
            board16[x * 6 - 2] = unit
            board16[x * 6] = atk
            board16[x * 6 - 4] = hp
            board17[x * 6 - 4] = player
            board17[x * 6] = player

        #otherwise
        else:
            print ("Invalid Co-ordinates")
            turnCount -= 1

#draw all units
def drawUnits():
    #for each unit, draw unit
    for i in unitList:
        drawUnit(*i)

#clear unit info, used for deaths and during movement
def clearUnit(x, y, atk, hp, unit, player):
    global turnCount
    
    #find corresponding y
    if y == 1:
        #remove corresponding info
        board3[x * 6 - 4] = " "
        board3[x * 6] = " "
        board4[x * 6 - 2] = " "
        board4[x * 6] = " "
        board4[x * 6 - 4] = " "
        board5[x * 6 - 4] = "_"
        board5[x * 6] = "_"

    elif y == 2:
        board6[x * 6 - 4] = " "
        board6[x * 6] = " "
        board7[x * 6 - 2] = " "
        board7[x * 6] = " "
        board7[x * 6 - 4] = " "
        board8[x * 6 - 4] = "_"
        board8[x * 6] = "_"

    elif y == 3:
        board9[x * 6 - 4] = " "
        board9[x * 6] = " "
        board10[x * 6 - 2] = " "
        board10[x * 6] = " "
        board10[x * 6 - 4] = " "
        board11[x * 6 - 4] = "_"
        board11[x * 6] = "_"

    elif y == 4:
        board12[x * 6 - 4] = " "
        board12[x * 6] = " "
        board13[x * 6 - 2] = " "
        board13[x * 6] = " "
        board13[x * 6 - 4] = " "
        board14[x * 6 - 4] = "_"
        board14[x * 6] = "_"

    elif y == 5:
        board15[x * 6 - 4] = " "
        board15[x * 6] = " "
        board16[x * 6 - 2] = " "
        board16[x * 6] = " "
        board16[x * 6 - 4] = " "
        board17[x * 6 - 4] = "_"
        board17[x * 6] = "_"

#used to get stats of individual special units
def getSpecStats(specUnit, i):
    global specAtk
    global specHp

    global unitList

    #if it is the unit
    if specUnit == "Tank":
        #set corresponding variables to its value
        specAtk = 1
        specHp = 3

        #set unit name, i calls on a specific unit
        unitList[i * 2 + 1][4] = "T"

    elif specUnit == "Warrior":
        specAtk = 2
        specHp = 2

        unitList[i * 2 + 1][4] = "W"

    elif specUnit == "Assassin":
        specAtk = 2
        specHp = 1

        unitList[i * 2 + 1][4] = "A"

#used for player 1 spawn phase
def spawnP1(param):
    global specAnswer
    global turnCount
    global specAtk
    global specHp

    global unitPresent

    #for every pair of units
    for i in range(0, 3):
        #if it is less than a corresponding turn(this essentially specifies whic unit is being spawned)
        if turnCount <= 20 * i:
            #if the user inputs right
            if param == "Right":
                #check if there are any units there
                checkForUnit(4, 1)

                #if so inform and ask again
                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                #set up variables
                else:
                    unitList[i * 2][0] = 4
                    unitList[i * 2][1] = 1
                    unitList[i * 2][2] = 1
                    unitList[i * 2][3] = 2
                    drawUnit(*unitList[i * 2])
                    break

            #same for other spawn locations
            elif param == "Left":
                checkForUnit(2, 1)

                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                else:
                    unitList[i * 2][0] = 2
                    unitList[i * 2][1] = 1
                    unitList[i * 2][2] = 1
                    unitList[i * 2][3] = 2
                    drawUnit(*unitList[i * 2])
                    break

            elif param == "Under":
                checkForUnit(3, 2)

                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                else:
                    unitList[i * 2][0] = 3
                    unitList[i * 2][1] = 2
                    unitList[i * 2][2] = 1
                    unitList[i * 2][3] = 2
                    drawUnit(*unitList[i * 2])
                    break
                
            else:
                print("Not A Valid Answer")
                turnCount -= 1
                break

        #every other unit is special
        elif turnCount <= 20 * i + 10:
            if param == "Right":
                checkForUnit(4, 1)

                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                #same thing, but you use special stats
                else:
                    #get special stats
                    getSpecStats(specAnswer, i)
                    #set the values in their place
                    unitList[i * 2 + 1][0] = 4
                    unitList[i * 2 + 1][1] = 1
                    unitList[i * 2 + 1][2] = specAtk
                    unitList[i * 2 + 1][3] = specHp
                    drawUnit(*unitList[i * 2 + 1])
                    break

            elif param == "Left":
                checkForUnit(2, 1)

                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                else:
                    getSpecStats(specAnswer, i)
                    unitList[i * 2 + 1][0] = 2
                    unitList[i * 2 + 1][1] = 1
                    unitList[i * 2 + 1][2] = specAtk
                    unitList[i * 2 + 1][3] = specHp
                    drawUnit(*unitList[i * 2 + 1])
                    break

            elif param == "Under":
                checkForUnit(3, 2)

                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                else:
                    getSpecStats(specAnswer, i)
                    unitList[i * 2 + 1][0] = 3
                    unitList[i * 2 + 1][1] = 2
                    unitList[i * 2 + 1][2] = specAtk
                    unitList[i * 2 + 1][3] = specHp
                    drawUnit(*unitList[i * 2 + 1])
                    break

            else:
                print("Not A Valid Answer")
                turnCount -= 1
                break

#used to check and respond to the tile the player wants to move to(note that the unit has been selected at this point)
def P1checkTargetTile(x, y, atk, hp, unit, player):
    global unitPresent
    
    global P1moveDown
    global P1moveLeft
    global P1moveRight
    global P1moveUp

    global turnCount

    global P1attack

    global unitMovAnswer

    global capitalP2

    #if unit is moving up
    if unitMovAnswer == "Up":
        #if they're trying to move over their own unit(which they can't)
        #for each friendly unit
        for i in range(0,6):
            #if co-ordinates match
            if unitList[i][0] == x and unitList[i][1] == y - 1:
                #inform and break
                print('You have a unit there!')
                break
        
        #if they're trying to move into an opposing unit(attack)
        #for each enemy unit
        for i in range(6, 12):
            #if coordinates match
            if unitList[i][0] == x and unitList[i][1] == y - 1:
                #deal damage
                unitList[i][3] -= atk
                #trigger boolean used to denote that something was done
                P1attack = True
                break

        #check if they are at the top
        if (x == 1 and y == 2) or (x == 5 and y == 2) or (y == 1):
            print("You can't move there!")

        #if allied capital
        elif x == 3 and y - 1 == 1:
            #ask again
            turnCount -= 1

        #if enemy capital
        elif x == 3 and y - 1 == 5:
            #deal damage
            capitalP2 -= atk
            #trigger boolean (see above)
            P1attack = True

        #if nothing was in the way, they can move up
        elif not P1attack:
            P1moveUp = True

    #same for other directions(comments are sparce as they're unneeded)
    elif unitMovAnswer == "Left":
        #if they're trying to move over they're own unit(which they can't)
        for i in range(0,6):
            if unitList[i][0] == x - 1 and unitList[i][1] == y:
                print('You have a unit there!')
                break
        
                #if they're trying to move into an opposing unit(attack)
        for i in range(6, 12):
            if unitList[i][0] == x - 1 and unitList[i][1] == y:
                unitList[i][3] -= atk
                P1attack = True
                break

        #check if they are at the leftmost
        if x == 1:
            print("You can't move there!")

        #if allied capital
        elif x - 1 == 3 and y == 1:
            print("You can't move there!")

        #if enemy capital
        elif x - 1 == 3 and y == 5:
            capitalP2 -= atk
            P1attack = True

        elif not P1attack:
            P1moveLeft = True

    elif unitMovAnswer == "Right":
        #if they're trying to move over they're own unit(which they can't)
        for i in range(0,6):
            if unitList[i][0] == x + 1 and unitList[i][1] == y:
                print('You have a unit there!')
                break
        
                #if they're trying to move into an opposing unit(attack)
        for i in range(6, 12):
            if unitList[i][0] == x + 1 and unitList[i][1] == y:
                unitList[i][3] -= atk
                P1attack = True
                break

        #check if they are at the rightmost
        if x == 5:
            print("You can't move there!")
                                                        
        #if allied capital
        elif x + 1 == 3 and y == 1:
            print("You can't move there!")

        #if enemy capital
        elif x + 1 == 3 and y == 5:
            capitalP2 -= atk

        elif not P1attack:
            P1moveRight = True

    elif unitMovAnswer == "Down":
        #if they're trying to move over they're own unit(which they can't)
        for i in range(0,6):
            if unitList[i][0] == x and unitList[i][1] == y + 1:
                print('You have a unit there!')
                break
        
        #if they're trying to move into an opposing unit(attack)
        for i in range(6, 12):
            if unitList[i][0] == x and unitList[i][1] == y + 1:
                unitList[i][3] -= atk
                P1attack = True
                break

        #check if they are at the bottom
        if (x == 1 and y == 4) or (x == 5 and y == 4) or (y == 5):
            print("You can't move there!")
                
        #if allied capital
        elif x == 3 and y + 1 == 1:
            print("You can't move there!")

        #if enemy capital
        elif x == 3 and y + 1 == 5:
            capitalP2 -= atk
            P1attack = True
                
        elif not P1attack:
            P1moveDown = True

#used to move the unit	
def p1MoveUnit(x, y):
    global unitList

    global P1moveDown
    global P1moveLeft
    global P1moveRight
    global P1moveUp

    global P1attack
	
    global turnCount
	
    global unitPresent

    global unitMovAnswer
    global unitPosAnswer

    global assassinSelected

    global unitPresent

    #for each unit you own
    for i in range(0, 6):
        #if coordinates match input
        if unitList[i][0] == x and unitList[i][1] == y:
            #if selected unit is an assassin
            if unitList[i][4] == "A":
                #flip boolean used for its special power
                assassinSelected = not assassinSelected

            #trigger a boolean used to denote there is indeed a unit present in the selected tile
            unitPresent = True

            #check what is in the target tile
            P1checkTargetTile(*unitList[i])

            #if there was nothing, they can move
            if P1moveUp:
                #clear original unit
                clearUnit(*unitList[i])
                #re-define coordinates
                unitList[i][0] = x
                unitList[i][1] -= 1

                #if selected unit was assassin
                if assassinSelected:
                    #re-input selected unit as itself
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    #ask again
                    turnCount -= 1

            #same for other directions
            elif P1moveLeft:
                clearUnit(*unitList[i])
                unitList[i][0] -= 1
                unitList[i][1] = y

                if assassinSelected:
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    turnCount -= 1
                    
            elif P1moveRight:
                clearUnit(*unitList[i])
                unitList[i][0] += 1
                unitList[i][1] = y

                if assassinSelected:
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    turnCount -= 1
                    
            elif P1moveDown:
                clearUnit(*unitList[i])
                unitList[i][0] = x
                unitList[i][1] += 1

                if assassinSelected:
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    turnCount -= 1

            #if the assassin attacked but did not move, he still gets his ability
            elif P2attack and assassinSelected:
                    print("The assassin gets another move!")
                    turnCount -= 1

            #otherwise if nothing was done, it must have been an invalid direction
            elif not P1attack:
                print("That's not a valid direction")
                turnCount -= 2

            drawUnit(*unitList[i])

    #if there was no unit present, they must not have any units there
    if not unitPresent:
        print("You do not have any units there")
        turnCount -= 2

#SAME THING BUT FOR PLAYER 2, SPARCE COMMENTS

def spawnP2(param):
    global specAnswer
    global turnCount
    global specAtk
    global specHp

    global unitPresent

    for i in range(3, 6):
        if turnCount <= 20 * i - 55:           
            if param == "Right":
                checkForUnit(4, 5)

                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                else:
                    unitList[i * 2][0] = 4
                    unitList[i * 2][1] = 5
                    unitList[i * 2][2] = 1
                    unitList[i * 2][3] = 2
                    drawUnit(*unitList[i * 2])
                    break

            elif param == "Left":
                checkForUnit(2, 5)

                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                else:
                    unitList[i * 2][0] = 2
                    unitList[i * 2][1] = 5
                    unitList[i * 2][2] = 1
                    unitList[i * 2][3] = 2
                    drawUnit(*unitList[i * 2])
                    break

            elif param == "Above":
                checkForUnit(3, 4)

                if unitPresent:
                    print('''There's a unit there!''')
                    turnCount -= 1
                    break

                else:
                    unitList[i * 2][0] = 3
                    unitList[i * 2][1] = 4
                    unitList[i * 2][2] = 1
                    unitList[i * 2][3] = 2
                    drawUnit(*unitList[i * 2])
                    break

            else:
                print("Not A Valid Answer")
                turnCount -= 1
                break
            
        elif turnCount <= 20 * i - 45:
            if param == "Right":
                getSpecStats(specAnswer, i)
                unitList[i * 2 + 1][0] = 4
                unitList[i * 2 + 1][1] = 5
                unitList[i * 2 + 1][2] = specAtk
                unitList[i * 2 + 1][3] = specHp
                drawUnit(*unitList[i * 2 + 1])
                break

            elif param == "Left":
                getSpecStats(specAnswer, i)
                unitList[i * 2 + 1][0] = 2
                unitList[i * 2 + 1][1] = 5
                unitList[i * 2 + 1][2] = specAtk
                unitList[i * 2 + 1][3] = specHp
                drawUnit(*unitList[i * 2 + 1])
                break

            elif param == "Above":
                getSpecStats(specAnswer, i)
                unitList[i * 2 + 1][0] = 3
                unitList[i * 2 + 1][1] = 4
                unitList[i * 2 + 1][2] = specAtk
                unitList[i * 2 + 1][3] = specHp
                drawUnit(*unitList[i * 2 + 1])
                break

            else:
                print("Not A Valid Answer")
                turnCount -= 1
                break

def P2checkTargetTile(x, y, atk, hp, unit, player):
    global unitPresent
    
    global P2moveDown
    global P2moveLeft
    global P2moveRight
    global P2moveUp

    global turnCount

    global P2attack

    global unitMovAnswer

    global capitalP1

    if unitMovAnswer == "Up":
        #if they're trying to move over they're own unit(which they can't)
        for i in range(6, 12):
            if unitList[i][0] == x and unitList[i][1] == y - 1:
                print('You have a unit there!')
                break
        
        #if they're trying to move into an opposing unit(attack)
        for i in range(0,6):
            if unitList[i][0] == x and unitList[i][1] == y - 1:
                unitList[i][3] -= atk
                P2attack = True
                break

        #check if they are at the top
        if (x == 1 and y == 2) or (x == 5 and y == 2) or (y == 1):
            print("You can't move there!")
                        
        #if allied capital
        elif x == 3 and y - 1 == 5:
            print("You can't move there!")

        #if enemy capital
        elif x == 3 and y - 1 == 1:
            capitalP1 -= atk
            P2attack = True
            print('938', P2attack)

        elif not P2attack:
            P2moveUp = True

    elif unitMovAnswer == "Left":
        #if they're trying to move over they're own unit(which they can't)
        for i in range(6,12):
            if unitList[i][0] == x - 1 and unitList[i][1] == y:
                print('You have a unit there!')
                break
        
                #if they're trying to move into an opposing unit(attack)
        for i in range(0, 6):
            if unitList[i][0] == x - 1 and unitList[i][1] == y:
                unitList[i][3] -= atk
                P2attack = True
                break

        #check if they are at the leftmost
        if x == 1:
            print("You can't move there!")

        #if allied capital
        elif x - 1 == 3 and y == 5:
            print("You can't move there!")

        #if enemy capital
        elif x - 1 == 3 and y == 1:
            capitalP1 -= atk
            P2attack = True

        elif not P2attack:
            P2moveLeft = True

    elif unitMovAnswer == "Right":
        #if they're trying to move over they're own unit(which they can't)
        for i in range(6,12):
            if unitList[i][0] == x + 1 and unitList[i][1] == y:
                print('You have a unit there!')
                turnCount -= 1
                break
        
                #if they're trying to move into an opposing unit(attack)
        for i in range(0, 6):
            if unitList[i][0] == x + 1 and unitList[i][1] == y:
                unitList[i][3] -= atk
                P2attack = True
                break

        #check if they are at the rightmost
        if x == 5:
            print("You can't move there!")

        #if allied capital
        elif x + 1 == 3 and y == 5:
            print("You can't move there!")

        #if enemy capital
        elif x + 1 == 3 and y == 1:
            capitalP1 -= atk
            P2attack = True

        elif not P2attack:
            P2moveRight = True

    elif unitMovAnswer == "Down":
        #if they're trying to move over they're own unit(which they can't)
        for i in range(6, 12):
            if unitList[i][0] == x and unitList[i][1] == y + 1:
                print('You have a unit there!')
                break
        
                #if they're trying to move into an opposing unit(attack)
        for i in range(0,6):
            if unitList[i][0] == x and unitList[i][1] == y + 1:
                unitList[i][3] -= atk
                P2attack = True
                break

        #check if they are at the bottom
        if (x == 1 and y == 4) or (x == 5 and y == 4) or (y == 5):
            print("You can't move there!")
                
        #if allied capital
        elif x == 3 and y + 1 == 5:
            print("You can't move there!")

        #if enemy capital
        elif x == 3 and y + 1 == 1:
            capitalP1 -= atk
            P2attack = True

        elif not P2attack:
            P2moveDown = True
			
def p2MoveUnit(x, y):
    global unitList

    global P2moveDown
    global P2moveLeft
    global P2moveRight
    global P2moveUp

    global P2attack
	
    global turnCount

    global unitMovAnswer
    global unitPosAnswer

    global assassinSelected

    global unitPresent
    
    for i in range(6, 12):
        if unitList[i][0] == x and unitList[i][1] == y:
            if unitList[i][4] == "A":
                assassinSelected = not assassinSelected
                print('DEBUG 765', unitList[i][4], assassinSelected)

            unitPresent = True

            P2checkTargetTile(*unitList[i])

            if P2moveUp:
                clearUnit(*unitList[i])
                unitList[i][0] = x
                unitList[i][1] -= 1

                if assassinSelected:
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    turnCount -= 1
                    
            elif P2moveLeft:
                clearUnit(*unitList[i])
                unitList[i][0] -= 1
                unitList[i][1] = y

                if assassinSelected:
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    turnCount -= 1
                    
            elif P2moveRight:
                clearUnit(*unitList[i])
                unitList[i][0] += 1
                unitList[i][1] = y

                if assassinSelected:
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    turnCount -= 1
                    
            elif P2moveDown:
                clearUnit(*unitList[i])
                unitList[i][0] = x
                unitList[i][1] += 1

                if assassinSelected:
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    turnCount -= 1

            elif P2attack and assassinSelected:
                    unitPosAnswer = "".join([chr(unitList[i][0] + 64), str(unitList[i][1])])
                    print("The assassin gets another move!")
                    turnCount -= 1

            elif not P2attack:
                print("That's not a valid direction")
                turnCount -= 2

            drawUnit(*unitList[i])

    if unitPresent == False:
        print("You do not have any units there")
        turnCount -= 2

#since alot of mechanics rely on turn-by-turn booleans, this resets the bools after every action
def resetBools():
    global P1moveDown
    global P1moveLeft
    global P1moveRight
    global P1moveUp

    global P2moveDown
    global P2moveLeft
    global P2moveRight
    global P2moveUp

    global P1match
    global P2match

    global P1attack
    global P2attack

    global unitPresent

    global P1surrounded
    global P2surrounded

    P1match = False
    P2match = False

    P1moveDown = False
    P1moveLeft = False
    P1moveRight = False
    P1moveUp = False

    P2moveDown = False
    P2moveLeft = False
    P2moveRight = False
    P2moveUp = False

    P1attack = False
    P2attack = False

    unitPresent = False

    P1surrounded = False
    P2surrounded = False

    for i in range(0, 12):
        unitMountainList[i] = False
        unitRiverList[i] = False

#check for dead units
def checkDeath():
    #for each unit
    for i in range(0,12):
        #if hp is 0 or less
        if int(unitList[i][3]) <= 0:
            #erase unit
            clearUnit(*unitList[i])

            #set unit values as dead
            unitList[i][0] = -1
            unitList[i][1] = 0
            unitList[i][2] = 0
            unitList[i][3] = 0

#check if anyone has won
def checkWin():
    #if capital's health is 0 or less
    if capitalP1 <= 0:
        #inform, wait and close
        print('''Player 1's capital has been destroyed! Player 2 Wins!''')
        time.sleep(3)
        quit()

    #same
    if capitalP2 <= 0:
        print('''Player 2's capital has been destroyed! Player 1 Wins!''')
        time.sleep(3)
        quit()

    #for each unit, check if it is around the opposing capital, if three units are then it is surrounded and they win
    for i in range(6, 12):
        if unitList[i][0] == 2 and unitList[i][1] == 1:
            for i in range(0, 6):
                if unitList[i][0] == 3 and unitList[i][1] == 2:
                    for i in range(0, 6):
                        if unitList[i][0] == 4 and unitList[i][1] == 1:
                            #inform, wait, and close
                            print('''Player 1's capital has been surrounded! Player 2 Wins!''')
                            time.sleep(3)
                            quit()

    #same
    for i in range(0, 6):
        if unitList[i][0] == 2 and unitList[i][1] == 5:
            for i in range(6, 12):
                if unitList[i][0] == 3 and unitList[i][1] == 4:
                    for i in range(6, 12):
                        if unitList[i][0] == 4 and unitList[i][1] == 5:
                            print('''Player 2's capital has been surrounded! Player 1 Wins!''')
                            time.sleep(3)
                            quit()

#loop with all input prompts depending on a "clock" variable turnCount
def gameLoop():
    global turnCount
    global specAnswer
    global spawnAnswer
    global unitMovAnswer
    global unitPosAnswer

    global P1surrounded
    global P2surrounded

    #check and apply terrain buffs
    checkTerrain()
    applyTerrain()

    #update capitals
    drawCapitals()

    #update all units
    drawUnits()

    #update board
    drawBoard()

    #intro and manual
    if turnCount == -1:
        print('''Welcome to Python Wars! In this game, you fight to destroy or surround the enemy capital! Player 1's capital is on the top, while Player 2's capital is on the bottom. Every turn has a movement phase where each player moves. Every other turn, including the first turn, the player can spawn a unit prior to their movement phase. \nEvery other spawn phase, you can spawn a special unit. Your choices include a tank, who has additional hp, a warrior who has additional atk, and an assassin who has additional attack and two moves per turn, but less hp. \nNormal units have 2 hp and 1 atk. This info is displayed on the tile the unit occupies, with hp on the left and atk on the right. \nThe player each unit belongs to can be seen on the corners. \nMountain tiles are denoted with M's, and they give a temporary boost to atk and hp while the unit is on it. River tiles heal a unit's hp, up until a certain limit, which is 3 for normal units and 5 for special units. \nPositioning is key to this game! If the enemy surrounds your capital, you lose. But even if one your units contributes to your capital being surrounded, you won't be able to spawn units if it happens. This can lead to the enemy having more units than you in the end! \nEnjoy!''')

    #P1 S
    elif turnCount % 10 == 0 and turnCount <= 60:
        #check if surrounded, almost same code as in checkWin
        for i in range(0, 12):
            if unitList[i][0] == 2 and unitList[i][1] == 1:
                for i in range(0, 12):
                    if unitList[i][0] == 3 and unitList[i][1] == 2:
                        for i in range(0, 12):
                            if unitList[i][0] == 4 and unitList[i][1] == 1:
                                #if so, inform and skip spawn phase
                                print('''Player 1's capital is surrounded! Your spawn phase has been skipped! ''')
                                P1surrounded = True

        #if not, ask where to spawn and what to spawn if it is special
        if not P1surrounded:
            if turnCount % 20 == 10:
                specAnswer = input("Player 1 - Spawning Phase \nYou can now spawn a special unit. What unit would you like: Tank, Warrior, or Assassin ")

            spawnAnswer = input("Player 1 - Spawning Phase \nWhere from your capital would you like to spawn your unit: Right, Left, or Under? ")
            #spawn it
            spawnP1(spawnAnswer)

    #P1 movement; selected unit
    elif turnCount % 5 == 1:
        assassinSelected = False
        unitPosAnswer = input("Player 1 - Movement Phase \nWhat unit would you like to move? (ex: B4) ")

    #P1 movement; desired direction
    elif turnCount % 5 == 2:
        unitMovAnswer = input("Player 1 - Movement Phase \nWhich direction would you like to move it: Up, Right, Down or Left ")

        #make uppercase
        unitPosAnswer = unitPosAnswer.upper()
        #if it is a proper response, 2 chars and the second char is a number
        if len(unitPosAnswer) == 2 and isInt(unitPosAnswer[1]) == True:
            #run input through the moving function
            p1MoveUnit(string.ascii_uppercase.index(unitPosAnswer[0]) + 1, int(unitPosAnswer[1]))

        #if not inform and ask again
        else:
            print('Invalid Answer')
            turnCount -= 2

    #same for player 2
    elif turnCount % 10 == 3 and turnCount <= 60:
        for i in range(0, 12):
            if unitList[i][0] == 2 and unitList[i][1] == 5:
                for i in range(0, 12):
                    if unitList[i][0] == 3 and unitList[i][1] == 4:
                        for i in range(0, 12):
                            if unitList[i][0] == 4 and unitList[i][1] == 5:
                                print('''Player 2's capital is surrounded! Your spawn phase has been skipped! ''')
                                P2surrounded

        if not P2surrounded:
            if turnCount % 20 == 13:
                specAnswer = input("Player 2 - Spawning Phase \nYou can now spawn a special unit. What unit would you like: Tank, Warrior, or Assassin ")

            spawnAnswer = input("Player 2 - Spawning Phase \nWhere from your capital would you like to spawn your unit: Right, Left, or Above? ")
            spawnP2(spawnAnswer)

    elif turnCount % 10 == 4 or turnCount % 10 == 8:
        assassinSelected = False
        unitPosAnswer = input("Player 2 - Movement Phase \nWhat unit would you like to move? (ex: B4) ")

    elif turnCount % 10 == 5 or turnCount % 10 == 9:
        unitMovAnswer = input("Player 2 - Movement Phase \nWhich direction would you like to move it: Up, Right, Down or Left ")

        unitPosAnswer = unitPosAnswer.upper()
        if len(unitPosAnswer) == 2 and isInt(unitPosAnswer[1]) == True:
            p2MoveUnit(string.ascii_uppercase.index(unitPosAnswer[0]) + 1, int(unitPosAnswer[1]))

        else:
            print('Invalid Answer')
            turnCount -= 2

    #remove mountain buff
    removeMountain()

    #reset bools
    resetBools()

    #check for win
    checkWin()

    #check unit deaths
    checkDeath()

    #next "turn"(really next action)
    turnCount += 1

    #run gameloop again
    gameLoop()

#board setup
boardInit()
drawBoard()

#run game
gameLoop()
