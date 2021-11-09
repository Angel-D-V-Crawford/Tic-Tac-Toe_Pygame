#!/usr/bin/env python
"""
    Tic Tac Toe
    By: Angel David Vazquez Crawford
"""

# Disabling prompt message at import
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
import sys
from random import randint

pygame.init()
 
# RGB Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

LINE_COLOR = (250, 29, 102)
CIRCLE_COLOR = (18, 226, 255)
CROSS_COLOR = (255, 0, 0)

DARK_CIRCLE_COLOR = (20, 142, 159)
DARK_CROSS_COLOR = (166, 38, 38)

screen_width = 500
screen_height = 500

size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tic Tac Toe")

done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont("", 45, False, False)

EMPTY = 0
CIRCLE = 1
CROSS = 2

PLAYER_ONE = 1
PLAYER_TWO = 2
TIE = 3
NOT_FULL = 0

playerOneAction = False
playerTwoAction = False
randomPlayer = True

space = 75
gameAreaWidth = screen_width - 75 * 2
gameAreaHeight = screen_height - 75 * 2
gameArea = (space, space, gameAreaWidth, gameAreaHeight)
cellAreas = (
    (space, space, gameAreaWidth // 3, gameAreaHeight // 3), 
    (space + gameAreaWidth // 3, space, gameAreaWidth // 3, gameAreaHeight // 3),
    (space + gameAreaWidth // 3 * 2, space, gameAreaWidth // 3, gameAreaHeight // 3),

    (space, space + gameAreaHeight // 3, gameAreaWidth // 3, gameAreaHeight // 3),
    (space + gameAreaWidth // 3, space + gameAreaHeight // 3, gameAreaWidth // 3, gameAreaHeight // 3),
    (space + gameAreaWidth // 3 * 2, space + gameAreaHeight // 3, gameAreaWidth // 3, gameAreaHeight // 3),

    (space, space + gameAreaHeight // 3 * 2, gameAreaWidth // 3, gameAreaHeight // 3),
    (space + gameAreaWidth // 3, space + gameAreaHeight // 3 * 2, gameAreaWidth // 3, gameAreaHeight // 3),
    (space + gameAreaWidth // 3 * 2, space + gameAreaHeight // 3 * 2, gameAreaWidth // 3, gameAreaHeight // 3)
)



class Player():
    def __init__(self, mode):
        self.mode = mode



class Cell():
    def __init__(self, posX, posY, width, height, state = 0):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = state
        self.changeable = True

    def draw(self):
        if self.state == CIRCLE:
            pygame.draw.circle(screen, CIRCLE_COLOR, (self.posX + self.width // 2, self.posY + self.height // 2), 50, 2)
        elif self.state == CROSS:
            pygame.draw.line(screen, CROSS_COLOR, (self.posX + 10, self.posY + 10), (self.posX + self.width - 10, self.posY + self.height - 10), 2)
            pygame.draw.line(screen, CROSS_COLOR, (self.posX + 10, self.posY + self.height - 10), (self.posX + self.width - 10, self.posY + 10), 2)

    def drawWithColor(self, color, player):
        if player.mode == CIRCLE:
            pygame.draw.circle(screen, color, (self.posX + self.width // 2, self.posY + self.height // 2), 50, 2)
        else:
            pygame.draw.line(screen, color, (self.posX + 10, self.posY + 10), (self.posX + self.width - 10, self.posY + self.height - 10), 2)
            pygame.draw.line(screen, color, (self.posX + 10, self.posY + self.height - 10), (self.posX + self.width - 10, self.posY + 10), 2)



class Board():
    def __init__(self):
        self.cells = []
        for c in range(9):
            temp = Cell(cellAreas[c][0], cellAreas[c][1], cellAreas[c][2], cellAreas[c][3])
            self.cells.append(temp)

    def draw(self):
        pygame.draw.line(screen, LINE_COLOR, [gameAreaWidth // 3 + space, space], 
            [gameAreaWidth // 3 + space, screen_height - space], 5)
        pygame.draw.line(screen, LINE_COLOR, [gameAreaWidth // 3 * 2 + space, space], 
            [gameAreaWidth // 3 * 2 + space, screen_height - space], 5)
        pygame.draw.line(screen, LINE_COLOR, [space, gameAreaHeight // 3 + space], 
            [gameAreaWidth + space, gameAreaHeight // 3 + space], 5)
        pygame.draw.line(screen, LINE_COLOR, [space, gameAreaHeight // 3 * 2 + space], 
            [gameAreaWidth + space, gameAreaHeight // 3 * 2 + space], 5)

    def changeCell(self, cell, state):
        self.cells[cell].state = state

    def drawCells(self):
        for c in self.cells:
            c.draw()

    def clear(self):
        for c in self.cells:
            c.state = EMPTY
            c.changeable = True



# Functions

def checkMouseCollition():
    cursor_pos = pygame.mouse.get_pos()
    numCell = 0
    global playerOneAction
    for c in board.cells:
        if c.changeable and cursor_pos[0] > c.posX and cursor_pos[0] < c.posX + c.width and cursor_pos[1] > c.posY and cursor_pos[1] < c.posY + c.height:
            board.changeCell(numCell, playerOne.mode)
            board.cells[numCell].changeable = False
            playerOneAction = True
        numCell += 1

def detectMouseInCell(board, player):
    cursor_pos = pygame.mouse.get_pos()
    if player.mode == CIRCLE:
        color = DARK_CIRCLE_COLOR
    else:
        color = DARK_CROSS_COLOR

    for c in board.cells:
        if c.state == EMPTY and c.changeable and cursor_pos[0] > c.posX and cursor_pos[0] < c.posX + c.width and cursor_pos[1] > c.posY and cursor_pos[1] < c.posY + c.height:
            c.drawWithColor(color, player)

def checkAction():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            checkMouseCollition()

def drawSelection():
    if selection == CIRCLE:
        pygame.draw.rect(screen, GREEN, (screen_width // 2 - question.get_width() // 2 - 3, screen_height // 2, 30, 30), 3)
    else:
        pygame.draw.rect(screen, GREEN, (screen_width // 2 + question.get_width() // 2 - 24, screen_height // 2, 30, 30), 3)

def selectionAnimation():
    if selection == CIRCLE:
        for i in range(6):
            if i % 2 == 0:
                pygame.draw.rect(screen, BLACK, (screen_width // 2 - question.get_width() // 2 - 3, screen_height // 2, 30, 30), 3)
            else:
                pygame.draw.rect(screen, GREEN, (screen_width // 2 - question.get_width() // 2 - 3, screen_height // 2, 30, 30), 3)
            pygame.display.flip()
            pygame.time.delay(250)
    else:
        for i in range(6):
            if i % 2 == 0:
                pygame.draw.rect(screen, BLACK, (screen_width // 2 + question.get_width() // 2 - 24, screen_height // 2, 30, 30), 3)
            else:
                pygame.draw.rect(screen, GREEN, (screen_width // 2 + question.get_width() // 2 - 24, screen_height // 2, 30, 30), 3)
            pygame.display.flip()
            pygame.time.delay(250)

def checkBoardFull():
    for c in board.cells:
        if c.state == EMPTY:
            return False
    return True

def checkWinner():
    if playerOne.mode == CIRCLE:
        modeTwo = CROSS
    else:
        modeTwo = CIRCLE

    rowOne = board.cells[0].state == playerOne.mode and board.cells[1].state == playerOne.mode and board.cells[2].state == playerOne.mode
    rowTwo = board.cells[3].state == playerOne.mode and board.cells[4].state == playerOne.mode and board.cells[5].state == playerOne.mode
    rowThree = board.cells[6].state == playerOne.mode and board.cells[7].state == playerOne.mode and board.cells[8].state == playerOne.mode
    columnOne = board.cells[0].state == playerOne.mode and board.cells[3].state == playerOne.mode and board.cells[6].state == playerOne.mode
    columnTwo = board.cells[1].state == playerOne.mode and board.cells[4].state == playerOne.mode and board.cells[7].state == playerOne.mode
    columnThree = board.cells[2].state == playerOne.mode and board.cells[5].state == playerOne.mode and board.cells[8].state == playerOne.mode
    diagonalOne = board.cells[0].state == playerOne.mode and board.cells[4].state == playerOne.mode and board.cells[8].state == playerOne.mode
    diagonalTwo = board.cells[2].state == playerOne.mode and board.cells[4].state == playerOne.mode and board.cells[6].state == playerOne.mode

    rowEnemyOne = board.cells[0].state == modeTwo and board.cells[1].state == modeTwo and board.cells[2].state == modeTwo
    rowEnemyTwo = board.cells[3].state == modeTwo and board.cells[4].state == modeTwo and board.cells[5].state == modeTwo
    rowEnemyThree = board.cells[6].state == modeTwo and board.cells[7].state == modeTwo and board.cells[8].state == modeTwo
    columnEnemyOne = board.cells[0].state == modeTwo and board.cells[3].state == modeTwo and board.cells[6].state == modeTwo
    columnEnemyTwo = board.cells[1].state == modeTwo and board.cells[4].state == modeTwo and board.cells[7].state == modeTwo
    columnEnemyThree = board.cells[2].state == modeTwo and board.cells[5].state == modeTwo and board.cells[8].state == modeTwo
    diagonalEnemyOne = board.cells[0].state == modeTwo and board.cells[4].state == modeTwo and board.cells[8].state == modeTwo
    diagonalEnemyTwo = board.cells[2].state == modeTwo and board.cells[4].state == modeTwo and board.cells[6].state == modeTwo

    if rowOne or rowTwo or rowThree or columnOne or columnTwo or columnThree or diagonalOne or diagonalTwo:
        return PLAYER_ONE
    elif rowEnemyOne or rowEnemyTwo or rowEnemyThree or columnEnemyOne or columnEnemyTwo or columnEnemyThree or diagonalEnemyOne or diagonalEnemyTwo:
        return PLAYER_TWO
    elif checkBoardFull():
        return TIE
    else:
        return NOT_FULL

def close():
    pygame.quit()
    sys.exit()

def detectRandomPlayerAction():
    global playerOneAction
    if randomPlayer and playerOneAction and not checkBoardFull():
        randCell = randint(0, 8)
        while not board.cells[randCell].changeable:
            randCell = randint(0, 8)

        board.changeCell(randCell, playerTwo.mode)
        board.cells[randCell].changeable = False
        playerOneAction = False



# Main program

board = Board()
setted = False
selected = False
selection = CIRCLE
enterPushed = False

while not selected:
    clock.tick(10)
    screen.fill(BLACK)
    question = font.render("O <--  --> X", 1, WHITE)
    screen.blit(question, (screen_width // 2 - question.get_width() // 2, screen_height // 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selected = True
            done = True
            close()

    drawSelection()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        selection = CIRCLE
    elif keys[pygame.K_RIGHT]:
        selection = CROSS
    elif keys[pygame.K_RETURN]:
        if selection == CIRCLE:
            playerOne = Player(CIRCLE)
            playerTwo = Player(CROSS)
        else:
            playerOne = Player(CROSS)
            playerTwo = Player(CIRCLE)
        selectionAnimation()
        selected = True

    pygame.display.flip()

while not done:

    clock.tick(10)
    screen.fill(BLACK)

    checkAction()

    board.draw()
    board.drawCells()
    detectMouseInCell(board, playerOne)

    pygame.display.flip()

    if checkWinner() == PLAYER_ONE:
        enterPushed = False
        while not enterPushed:
            pygame.event.clear()
            message = font.render("Winner: Player One!", 1, WHITE)
            screen.blit(message, (screen_width // 2 - message.get_width() // 2, 20))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                enterPushed = True
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    close()
        board.clear()
        pygame.display.flip()

    elif checkWinner() == PLAYER_TWO:
        enterPushed = False
        while not enterPushed:
            pygame.event.clear()
            message = font.render("Winner: Player Two!", 1, WHITE)
            screen.blit(message, (screen_width // 2 - message.get_width() // 2, 20))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                enterPushed = True
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    close()
        board.clear()
        pygame.display.flip()

    elif checkWinner() == TIE:
        enterPushed = False
        while not enterPushed:
            pygame.event.clear()
            message = font.render("Tie!", 1, WHITE)
            screen.blit(message, (screen_width // 2 - message.get_width() // 2, 20))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                enterPushed = True
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    close()
        board.clear()
        pygame.display.flip()

    detectRandomPlayerAction()

    pygame.event.clear()
 
pygame.quit()

