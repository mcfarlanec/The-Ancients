from tkinter import *
from time import *
from random import *
from math import *

#         THE ANCIENTS            #
#     BY: COLIN MCFARLANE         #
#          VERSION 1.0            #
#   LAST MODIFIED: JAN 26, 2017.  #

root = Tk()
screen = Canvas(root, width=800, height=500, background="black")
screen.pack()


# --------- INITAL VALUES ---------#
def setInitalValues():
    global startImage, instructionsImage, gameOverImage, victoryImage
    global background, backgroundImage, backgroundx, backgroundy, backgroundSpeed
    global player, playerx, playery, playerSpeedModifier, playerxSpeed, playerySpeed, playerAttackFrames, playerImage, playerMovementImage, playerAttackImage, playerHitbox, playerMovementCheck, playerDeath
    global windblades, windbladesx, windbladesy, windbladeSpeed, windbladeImage
    global boss, bossx, bossy, bossSpeedModifier, bossxSpeed, bossySpeed, bossImage, bossAttackImage, bossDeathImage, crabAttackFrames, bossHitbox, bossHealthBox, bossHealth, bossText, bossCountdown
    global fireballCount, fireballImage, fireballSpeed, fireballx, fireballAttack, fireball1, fireball2, fireball3, firebally1, firebally2, firebally3
    global rockImage, rockx, rocky, rocks, rockNum, rockAttack, rockxSpeed, rockySpeed
    global timeFinish, timeStart, bossTimeDifference, firstTime, playerTimeDifference, windbladeDelay
    global snakes, snakex, snakey, snakeSpeed, snakeNum, snakeImage, snakeAttack, hydraFrames
    global arrows, arrowx, arrowy, arrowNum, arrowxSpeed, arrowySpeed, arrowImage

    startImage = PhotoImage(file="start.gif")
    instructionsImage = PhotoImage(file="instructions.gif")
    gameOverImage = PhotoImage(file="over.gif")
    victoryImage = PhotoImage(file="victory.gif")

    if currentBoss == 1:
        background = 0
        backgroundImage = PhotoImage(file="volcano.gif")
        backgroundx = 400
        backgroundy = 150
        backgroundSpeed = 0.1

        player = 0
        playerImage = PhotoImage(file="rider.gif")
        playerMovementImage = PhotoImage(file="ridermoving.gif")
        playerAttackImage = PhotoImage(file="riderattacking.gif")
        playerx = 600
        playery = 380
        playerSpeedModifier = 5
        playerxSpeed = 0
        playerySpeed = 0
        playerHitbox = 0
        playerMovementCheck = False
        playerAttackFrames = 0
        playerDeath = False

        windblades = []
        windbladesx = []
        windbladesy = []
        windbladeSpeed = 8
        windbladeImage = PhotoImage(file="windblade.gif")

        boss = 0
        bossImage = PhotoImage(file="crab.gif")
        bossAttackImage = PhotoImage(file="crabAttack.gif")
        bossDeathImage = PhotoImage(file="crabDeath.gif")
        bossx = 150
        bossy = 350
        bossxSpeed = 0
        bossySpeed = 1
        crabAttackFrames = 0
        bossHealth = 79
        bossHealthBox = 0
        bossText = 0
        bossHitbox = 0
        bossCountdown = 0

        fireballCount = 0
        fireballSpeed = 5
        fireballx = 0
        fireballAttack = False
        fireballImage = PhotoImage(file="fireball.gif")
        fireball1 = 0
        fireball2 = 0
        fireball3 = 0
        firebally1 = 0
        firebally2 = 0
        firebally3 = 0

        rockImage = PhotoImage(file="rock.gif")
        rockx = []
        rocky = []
        rocks = []
        rockNum = 4
        rockAttack = False
        rockxSpeed = 1
        rockySpeed = 5

        timeFinish = 0
        timeStart = 0
        bossTimeDifference = 0
        playerTimeDifference = 0
        windbladeDelay = 0
        firstTime = True

    if currentBoss == 2:
        background = 0
        backgroundImage = PhotoImage(file="ruins.gif")
        backgroundx = 400
        backgroundy = 75
        backgroundSpeed = 0.1

        player = 0
        playerImage = PhotoImage(file="rider.gif")
        playerMovementImage = PhotoImage(file="ridermoving.gif")
        playerAttackImage = PhotoImage(file="riderattacking.gif")
        playerx = 600
        playery = 380
        playerSpeedModifier = 5
        playerxSpeed = 0
        playerySpeed = 0
        playerHitbox = 0
        playerMovementCheck = False
        playerAttackFrames = 0
        playerDeath = False

        windblades = []
        windbladesx = []
        windbladesy = []
        windbladeSpeed = 8
        windbladeImage = PhotoImage(file="windblade.gif")

        boss = 0
        bossImage = PhotoImage(file="hydra.gif")
        bossAttackImage = PhotoImage(file="hydraAttack.gif")
        bossDeathImage = PhotoImage(file="hydraDeath.gif")
        bossx = 150
        bossy = 350
        bossxSpeed = 3
        bossySpeed = 3
        bossHealth = 79
        bossHealthBox = 0
        bossText = 0
        bossHitbox = 0
        bossCountdown = 0

        snakes = []
        snakex = []
        snakey = []
        snakeSpeed = 4
        snakeNum = 5
        snakeImage = PhotoImage(file="snake.gif")
        snakeAttack = False
        hydraFrames = 0

        timeFinish = 0
        timeStart = 0
        bossTimeDifference = 0
        playerTimeDifference = 0
        windbladeDelay = 0

    if currentBoss == 3:
        background = 0
        backgroundImage = PhotoImage(file="forest.gif")
        backgroundx = 0
        backgroundy = 0
        backgroundSpeed = 0.1

        player = 0
        playerImage = PhotoImage(file="rider.gif")
        playerMovementImage = PhotoImage(file="ridermoving.gif")
        playerAttackImage = PhotoImage(file="riderattacking.gif")
        playerx = 600
        playery = 380
        playerSpeedModifier = 5
        playerxSpeed = 0
        playerySpeed = 0
        playerHitbox = 0
        playerMovementCheck = False
        playerAttackFrames = 0
        playerDeath = False

        windblades = []
        windbladesx = []
        windbladesy = []
        windbladeSpeed = 8
        windbladeImage = PhotoImage(file="windblade.gif")

        boss = 0
        bossImage = PhotoImage(file="warrior.gif")
        bossAttackImage = PhotoImage(file="warriorAttack.gif")
        bossDeathImage = PhotoImage(file="warriorDeath.gif")
        bossx = 150
        bossy = 350
        bossxSpeed = 2
        bossySpeed = 1
        bossHealth = 79
        bossHealthBox = 0
        bossText = 0
        bossHitbox = 0
        bossCountdown = 0

        arrows = []
        arrowx = []
        arrowy = []
        arrowxSpeed = 5
        arrowySpeed = 2
        arrowImage = PhotoImage(file="arrow.gif")
        arrowNum = 1

        timeFinish = 0
        timeStart = 0
        bossTimeDifference = 0
        playerTimeDifference = 0
        windbladeDelay = 0


# --------- BACKGROUND ---------#
def drawBackground():
    global background

    background = screen.create_image(backgroundx, backgroundy, image=backgroundImage)  # Creates the background image


# --------- PLAYER FUNCTIONS ---------#
def createPlayer():
    global player, playerHitbox, playerMovementCheck, playerAttackFrames

    if playerAttackFrames != 0:
        player = screen.create_image(playerx, playery, image=playerAttackImage)  # creates the attacking player image
        playerAttackFrames = playerAttackFrames - 1

    elif playerMovementCheck == False:
        player = screen.create_image(playerx, playery,
                                     image=playerImage)  # if the player is not moving, creates a standing image

    elif playerMovementCheck == True:
        player = screen.create_image(playerx, playery, image=playerMovementImage)  # moving player image


def movePlayer():
    global player, playerx, playery, playerxSpeed, playerySpeed

    playerx = playerx + playerxSpeed
    playery = playery + playerySpeed  # Changing the players speed (based on key strokes)


def playerAttack():
    global windblades, windbladesx, windbladesy, windbladeDelay, playerAttackFrames

    if playerTimeDifference >= 0.15:  # Can only attack every 0.15 seconds
        playerAttackFrames = 15

        windbladeDelay = time()

        windbladesx.append(playerx)
        windbladesy.append(playery)
        windblades.append(0)


def movePlayerProjectiles():
    global windblades, windbladesx, windbladesy

    for i in range(0, len(windbladesx)):
        windbladesx[i] = windbladesx[i] - windbladeSpeed

    checkWindbladesHit()


def checkWindbladesOutofBounds():
    global windblades, windbladesx, windbladesy

    i = 0

    while i < len(windbladesx) - 1:
        if windbladesx[i] < 0:
            windbladesy.pop(i)  # Checking if the players projectiles have flown off screen
            windbladesx.pop(i)
            windblades.pop(i)

        else:
            i = i + 1


def checkWindbladesHit():  # Player hit detection
    global bossHealth, windblades, windbladesx, windbladesy

    i = 0

    while i < len(windbladesx):

        if windbladesx[i] > bossx - 90 and windbladesx[i] < bossx + 70 and windbladesy[i] > bossy - 30 and windbladesy[
            i] < bossy + 70:
            windbladesy.pop(i)
            windbladesx.pop(
                i)  # if the player projectiles are inside a bosses 'hitbox', takes one health away from boss
            windblades.pop(i)

            bossHealth = bossHealth - 1

        else:
            i = i + 1

    checkWindbladesOutofBounds()


def drawWindblades():
    global windblades, windbladesx, windbladesy

    for i in range(0, len(windbladesy)):
        windblades[i] = screen.create_image(windbladesx[i] - 5, windbladesy[i] - 5,
                                            image=windbladeImage)  # animating player projectiles


def deleteWindblades():
    global windblades, windbladesx, windbladesy

    for i in range(0, len(windbladesy)):  # Deleting player projectiles
        screen.delete(windblades[i])


def checkPlayerBoundries():
    global playerx, playery

    if playerx > 780:
        playerx = playerx - 10

    if playerx < 20:
        playerx = playerx + 10  # player boundries so they cannot run around the whole screen

    if playery > 280:
        playery = playery - 10

    if playery < 470:
        playery = playery + 10


# --------- BOSS FUNCTIONS ---------#
def createBoss():
    global boss, crabAttackFrames, bossHealthBox, bossText, bossHitbox, hydraFrames, snakeAttack

    if currentBoss == 1:  # If on the first boss

        if bossHealth <= 0:
            boss = screen.create_image(bossx, bossy, image=bossDeathImage)
            bossHealthBox = screen.create_rectangle(0, 300, 900, 350, fill="grey")  # Boss death text and images
            bossText = screen.create_text(400, 325, text="ANCIENT DEFEATED", font="times 20")

        else:
            if fireballAttack == True:  # If the boss is using the fireball attack

                if crabAttackFrames < 175:  # changes what the boss looks like to animate attacks

                    boss = screen.create_image(bossx, bossy, image=bossAttackImage)
                    crabAttackFrames = crabAttackFrames + 1

            elif fireballAttack == False:  # otherwise, use the normal boss look

                boss = screen.create_image(bossx, bossy, image=bossImage)
                crabAttackFrames = 0

            bossHealthBox = screen.create_rectangle(10, 25, bossHealth * 10, 50,
                                                    fill="red")  # Creating the boss healthbar and name
            bossText = screen.create_text(400, 75, text="THE ANCIENT DEMON", font="times 20", fill="red")

    if currentBoss == 2:

        if bossHealth <= 0:
            boss = screen.create_image(bossx, bossy, image=bossDeathImage)
            bossHealthBox = screen.create_rectangle(0, 300, 900, 350, fill="grey")  # Boss death text and images
            bossText = screen.create_text(400, 325, text="ANCIENT DEFEATED", font="times 20")

        else:
            if snakeAttack == True and hydraFrames < 100:

                boss = screen.create_image(bossx, bossy,
                                           image=bossAttackImage)  # changes what the boss looks like to animate attacks
                hydraFrames = hydraFrames + 1

            elif snakeAttack == True or snakeAttack == False:
                boss = screen.create_image(bossx, bossy, image=bossImage)  # otherwise, use normal boss image

                if hydraFrames > 1:
                    snakeAttack = False
                    hydraFrames = 0

            bossHealthBox = screen.create_rectangle(10, 25, bossHealth * 10, 50,
                                                    fill="red")  # Creating the boss healthbar and name
            bossText = screen.create_text(400, 75, text="THE ANCIENT HYDRA", font="times 20", fill="red")

    if currentBoss == 3:

        if bossHealth <= 0:
            boss = screen.create_image(bossx, bossy, image=bossDeathImage)
            bossHealthBox = screen.create_rectangle(0, 300, 900, 350, fill="grey")  # Boss death text and images
            bossText = screen.create_text(400, 325, text="ANCIENT DEFEATED", font="times 20")

        else:

            boss = screen.create_image(bossx, bossy, image=bossImage)  # Creates boss image itself

            bossHealthBox = screen.create_rectangle(10, 25, bossHealth * 10, 50,
                                                    fill="red")  # Creating the boss healthbar and name
            bossText = screen.create_text(400, 75, text="THE ANCIENT KING", font="times 20", fill="red")


def moveBoss():  # controled boss movement using boundries. different for each boss.
    global bossx, bossy, bossxSpeed, bossySpeed

    if currentBoss == 1:  # First boss movement

        if bossHealth <= 0:
            bossySpeed = 0

        else:

            if bossy > 425:
                bossySpeed = - bossySpeed

            elif bossy < 250:
                bossySpeed = 1

    if currentBoss == 2:  # Second boss movement

        if bossHealth <= 0:
            bossySpeed = 0
            bossxSpeed = 0

        else:

            if bossx < 50:
                bossxSpeed = 3

            elif bossx > 400:
                bossxSpeed = - bossxSpeed

            if bossy > 425:
                bossySpeed = - bossySpeed

            elif bossy < 250:
                bossySpeed = 3

    if currentBoss == 3:  # Third boss movement

        if bossHealth <= 0:
            bossySpeed = 0
            bossxSpeed = 0

        else:

            if bossx < 50:
                bossxSpeed = 2

            elif bossx > 575:
                bossxSpeed = - bossxSpeed

            if bossy > 375:
                bossySpeed = - bossySpeed

            elif bossy < 300:
                bossySpeed = 1

    bossx = bossx + bossxSpeed
    bossy = bossy + bossySpeed


def bossAttack():
    global boss, timeStart, bossTimeDifference, firstTime, fireball1, fireball2, fireball3, fireballCount, bossx, bossy, fireballx, fireballAttack, firebally1, firebally2, firebally3
    global rockx, rocky, rocks, rockNum, rockAttack, rockxSpeed, rockySpeed
    global snakeAttack, playerDeath
    global arrowx, arrowy, arrows

    if currentBoss == 1:

        if bossHealth <= 0:  # if the boss is at zero health, no attacks
            pass

        else:

            if bossTimeDifference >= 3 and firstTime == True:
                firstTime = False
                timeStart = time()

            elif bossTimeDifference >= 3 and firstTime == False:  # if three seconds have passed, the boss shoots fireballs

                fireballAttack = True

                fireballx = bossx + fireballx + fireballSpeed
                firebally1 = bossy
                firebally2 = bossy
                firebally3 = bossy

                timeStart = time()

                fireballCount = fireballCount + 1

            if fireballCount == 3:  # If the boss has used three fireballs, rocks will fall from the sky as a second attack

                fireballCount = 0  # Resests the count of fireballs

                rockAttack = True  # Sets rockAttack to true (used later for moving and checking the rocks)

                rockx = []  # Creating empty arrays for the rocks
                rocky = []

                for x in range(rockNum):  # Giving the rocks random starting positions

                    xCord = randint(150, 650)
                    yCord = -40

                    rockx.append(xCord)
                    rocky.append(yCord)
                    rocks.append(0)

    if currentBoss == 2:

        if bossHealth <= 0:  # if the boss is at zero health, no attacks
            pass

        else:

            if bossTimeDifference >= 4:  # Every four seconds, create the wave of snakes

                timeStart = time()

                snakeAttack = True

                for x in range(snakeNum):
                    xCord = - 100
                    yCord = randint(250, 475)

                    snakex.append(xCord)
                    snakey.append(yCord)
                    snakes.append(0)

    if currentBoss == 3:

        if bossHealth <= 0 or playerDeath == True:  # if the boss is at zero health, no attacks
            pass

        else:

            if bossTimeDifference >= 0.5:  # Every 0.5 seconds creates an arrow for the player to dodge

                timeStart = time()

                for x in range(arrowNum):
                    xCord = 0
                    yCord = randint(0, 300)

                    arrowx.append(xCord)
                    arrowy.append(yCord)
                    arrows.append(0)


def moveProjectiles():
    global fireball1, fireball2, fireball3, fireballx, bossx, fireballSpeed, fireballAttack, firebally1, firebally2, firebally1, playerDeath
    global rockx, rocky, rocks, rockNum, rockAttack, rockxSpeed, rockySpeed

    if currentBoss == 1:

        if fireballAttack == True:  # If fireballAttack is true, move the fireballs, reset if they go off screen.

            fireballx = fireballx + fireballSpeed
            firebally1 = bossy + 50
            firebally2 = bossy + 30
            firebally3 = bossy + 10

            fireball1 = screen.create_image(fireballx, firebally1,
                                            image=fireballImage)  # creating and moving each of the fireballs
            fireball2 = screen.create_image(fireballx, firebally2, image=fireballImage)
            fireball3 = screen.create_image(fireballx, firebally3, image=fireballImage)

            if fireballx > 850:  # if the fireballs go too far off screen remove them
                fireballAttack = False
                fireballx = 0
                fireball1 = 0
                fireball2 = 0
                fireball3 = 0

            if fireballx > playerx - 30 and fireballx < playerx + 30 and firebally2 > playery - 50 and firebally2 < playery + 50:  # if the fireball is within the players hitbox, game over
                playerDeath = True
                gameOver()

        if rockAttack == True:  # if rockAttack is true, the second attack begins

            for x in range(len(rockx)):  # moving the rocks
                rockx[x] = rockx[x] + rockxSpeed
                rocky[x] = rocky[x] + rockySpeed

            i = 0
            while i < len(rockx):

                if rockx[i] > playerx - 30 and rockx[i] < playerx + 30 and rocky[i] > playery - 50 and rocky[
                    i] < playery + 50:  # Checking if the rocks hit the player, if they did gameover
                    rocky.pop(i)
                    rockx.pop(i)
                    rocks.pop(i)

                    playerDeath = True
                    gameOver()
                    break

                else:
                    i = i + 1

            i = 0
            while i < len(rocky) - 1:  # checking if the rocks have hit the ground and should be deleted
                if rocky[i] > 550:
                    rocky.pop(i)
                    rockx.pop(i)
                    rocks.pop(i)

                    rockAttack = False

                else:
                    i = i + 1


def createRocks():
    if rockAttack == True:  # creates the images of the rocks

        for i in range(0, len(rocky)):
            rocks[i] = screen.create_image(rockx[i], rocky[i], image=rockImage)


def deleteRocks():
    if rockAttack == True:  # deletes the images of the rocks

        for i in range(0, len(rockx)):
            screen.delete(rocks[i])


def createSnakes():
    if currentBoss == 2:  # creates the images of the snakes

        for i in range(len(snakex)):
            snakes[i] = screen.create_image(snakex[i], snakey[i], image=snakeImage)


def checkSnakes():
    global playerDeath

    if currentBoss == 2:

        for x in range(len(snakex)):  # moving the snakes
            snakex[x] = snakex[x] + snakeSpeed

        i = 0

        while i < len(snakex) - 1:
            if snakex[i] > 850:  # destroying the snakes if they are off screen
                snakey.pop(i)
                snakex.pop(i)
                snakes.pop(i)

            else:
                i = i + 1
        i = 0

        while i < len(snakex) - 1:
            if snakex[i] > playerx - 20 and snakex[i] < playerx + 20 and snakey[i] > playery - 25 and snakey[
                i] < playery + 25:

                playerDeath = True  # If the snakes hit the player, game over.
                gameOver()
                break

            else:
                i = i + 1


def deleteSnakes():
    if currentBoss == 2:

        for i in range(0, len(snakex)):  # deletes snakes for animating purposes
            screen.delete(snakes[i])


def createArrows():  # creates the images of the arrows
    if currentBoss == 3:
        for i in range(len(arrowx)):
            arrows[i] = screen.create_image(arrowx[i], arrowy[i], image=arrowImage)


def checkArrows():
    global playerDeath
    if currentBoss == 3:

        for x in range(len(arrowx)):
            arrowx[x] = arrowx[x] + arrowxSpeed  # moving the arrows
            arrowy[x] = arrowy[x] + arrowySpeed

        i = 0

        while i < len(arrowx) - 1:
            if arrowy[i] > 550:
                arrowy.pop(i)  # destroying the arrows if they are off screen
                arrowx.pop(i)
                arrows.pop(i)

            else:
                i = i + 1
        i = 0

        while i < len(arrowx) - 1:
            if arrowx[i] > playerx - 20 and arrowx[i] < playerx + 20 and arrowy[i] > playery - 25 and arrowy[
                i] < playery + 25:

                playerDeath = True
                gameOver()  # If an arrow hits the player, game over.
                break

            else:
                i = i + 1


def deleteArrows():
    if currentBoss == 3:
        for i in range(0, len(arrowx)):  # deletes arrows for animating purposes
            screen.delete(arrows[i])


# --------- KEY HANDLERS ---------#
def keyDownHandler(event):
    global playerxSpeed, playerySpeed, playerSpeedModifier, playerMovementCheck

    if event.keysym == "Left":
        playerxSpeed = - playerSpeedModifier  # Moves the players character left
        playerMovementCheck = True

    if event.keysym == "Right":
        playerxSpeed = playerSpeedModifier  # Moves the players character right
        playerMovementCheck = True

    if event.keysym == "Up":
        playerySpeed = - playerSpeedModifier  # Moves the players character up
        playerMovementCheck = True

    if event.keysym == "Down":
        playerySpeed = playerSpeedModifier  # Moves the players character down
        playerMovementCheck = True

    if event.keysym == "x" or event.keysym == "X":  # Triggers a player attack
        playerAttack()


def keyUpHandler(event):
    global playerxSpeed, playerySpeed, playerMovementCheck

    playerxSpeed = 0
    playerySpeed = 0
    playerMovementCheck = False


# --------- MAIN GAME LOOP ---------#
def runGame():
    global backgroundx, timeFinish, timeStart, bossTimeDifference, playerTimeDifference, fireballx, fireball1, fireball2, fireball3, rocks, rockNum

    if currentBoss == 4:  # If all three bosses are dead, the player wins!
        win()

    else:

        setInitalValues()
        drawBackground()

        while playerDeath == False:  # while the player is alive, run the game

            if currentBoss == 4:
                root.bind("<Button-1>", gameOverClick)  # setting up for player victory.
                break

            createPlayer()
            movePlayer()
            checkPlayerBoundries()  # PLAYER FUNCTIONS
            movePlayerProjectiles()
            drawWindblades()

            timeFinish = time()
            bossTimeDifference = timeFinish - timeStart  # TIME CALCULATIONS
            playerTimeDifference = timeFinish - windbladeDelay

            createBoss()
            moveBoss()
            bossAttack()
            moveProjectiles()  # BOSS FUNCTIONS
            createRocks()
            createSnakes()
            checkSnakes()
            createArrows()
            checkArrows()

            nextBoss()

            screen.update()
            sleep(0.01)  # UPDATE, SLEEP AND DELETE FUNCTIONS
            screen.delete(player, playerHitbox, boss, bossText, bossHealthBox, bossHitbox, fireball1, fireball2,
                          fireball3)
            deleteWindblades()
            deleteRocks()
            deleteSnakes()
            deleteArrows()

            root.bind("<Button-1>", nothingClick)

        if playerDeath == True:
            gameOver()  # player dead = game over


# --------- STATE OF THE GAME FUNCTIONS ---------#
def startScreen():
    global currentBoss

    currentBoss = 1

    setInitalValues()  # Creates the starting screen

    screen.create_image(400, 250, image=startImage)
    root.bind("<Button-1>", startScreenClick)


def startScreenClick(event):
    xMouse = event.x
    yMouse = event.y

    if 230 <= xMouse <= 580 and 80 <= yMouse <= 140:  # Mouse control for the intro screen
        runGame()
    elif 230 <= xMouse <= 580 and 160 <= yMouse <= 210:
        instructions()


def instructions():
    screen.create_image(400, 250, image=instructionsImage)  # Make the instructions screen
    root.bind("<Button-1>", instructionsClick)


def instructionsClick(event):
    xMouse = event.x
    yMouse = event.y

    if 10 <= xMouse <= 175 and 10 <= yMouse <= 60:  # Mouse control for instruction screen
        startScreen()


def gameOver():
    screen.delete(background, player, playerHitbox, boss, bossText, bossHealthBox, bossHitbox, fireball1, fireball2,
                  fireball3)
    deleteWindblades()
    deleteRocks()
    deleteSnakes()  # Deleting everything because the game is over
    deleteArrows()

    screen.update()

    screen.create_image(400, 250, image=gameOverImage)  # Makes the game over image. Also sets the mouse up.
    root.bind("<Button-1>", gameOverClick)


def gameOverClick(event):
    xMouse = event.x
    yMouse = event.y

    if 0 <= xMouse <= 800 and 0 <= yMouse <= 500:  # Game over mouse. Click anywhere are returns to the intro screen.
        startScreen()


def nextBoss():
    global bossCountdown, currentBoss

    if bossHealth <= 0:
        bossCountdown = bossCountdown + 1

    if bossHealth <= 0 and bossCountdown == 500:  # Transitioning from one boss to another
        currentBoss = currentBoss + 1
        screen.delete(bossText, bossHealthBox)
        runGame()


def nothingClick(event):
    xMouse = event.x
    yMouse = event.y

    1 + 1


def win():
    screen.create_image(400, 250, image=victoryImage)

    root.bind("<Button-1>", gameOverClick)  # Victory screen


root.after(0, startScreen)

screen.bind("<Key>", keyDownHandler)
screen.bind("<KeyRelease>", keyUpHandler)

screen.focus_set()
root.mainloop()
