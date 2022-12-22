# Initialize and import stuff.

from neopixel import Neopixel
from time import sleep
import random
import max7219
from machine import Pin, SPI


# Define some parameters. These dictonaries include all of the lights ordered by x-position, y-position, and the last has each light's coordinates.

lightAmount = 50

rows = {0: (0, 24, 25), 1: (1, 23, 26, 49), 2: (2, 22, 27, 48), 3: (3, 21, 28, 47), 4: (4, 20, 29, 46), 5: (5, 19, 30, 45), 6: (6, 18, 43, 44), 7: (7, 16, 17, 31, 32, 42), 8: (8, 15, 33, 41), 9: (9, 13, 14, 34, 40), 10: (10, 35, 39), 11: (11, 12, 36, 37, 38)}
cols = {0: (49, 48, 47, 46, 45, 37), 1: (44, 43, 42, 41, 40, 3, 5, 9, 11, 0, 38), 2: (1, 2, 4, 6, 7, 10, 39), 3: (8, 12, 13, 31, 32, 34, 35, 36), 4: (29, 30, 27, 26, 14), 5: (15, 18, 28, 33), 6: (16, 17, 19, 24, 25), 7: (20, 21, 22, 23)}
coords = {0: (1, 0), 1: (2, 1), 2: (2, 2), 3: (1, 3), 4: (2, 4), 5: (1, 5), 6: (2, 6), 7: (2, 7), 8: (3, 8), 9: (1, 9), 10: (2, 10), 11: (1, 11), 12: (3, 11), 13: (3, 9), 14: (4, 9), 15: (5, 8), 16: (6, 7), 17: (6, 7), 18: (5, 6), 19: (6, 5), 20: (7, 4), 21: (7, 3), 22: (7, 2), 23: (7, 1), 24: (6, 0), 25: (6, 0), 26: (4, 1), 27: (4, 2), 28: (5, 3), 29: (4, 4), 30: (4, 5), 31: (3, 7), 32: (3, 7), 33: (5, 8), 34: (3, 9), 35: (3, 10), 36: (3, 11), 37: (0, 11), 38: (1, 11), 39: (2, 10), 40: (1, 9), 41: (1, 8), 42: (1, 7), 43: (1, 6), 44: (1, 6), 45: (0, 5), 46: (0, 4), 47: (0, 3), 48: (0, 2), 49: (0, 1)}

keys = (coords.keys())
vals = (coords.values())

states = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 5: [0, 0, 0], 6: [0, 0, 0], 7: [0, 0, 0], 8: [0, 0, 0], 9: [0, 0, 0], 10: [0, 0, 0], 11: [0, 0, 0], 12: [0, 0, 0], 13: [0, 0, 0], 14: [0, 0, 0], 15: [0, 0, 0], 16: [0, 0, 0], 17: [0, 0, 0], 18: [0, 0, 0], 19: [0, 0, 0], 20: [0, 0, 0], 21: [0, 0, 0], 22: [0, 0, 0], 23: [0, 0, 0], 24: [0, 0, 0], 25: [0, 0, 0], 26: [0, 0, 0], 27: [0, 0, 0], 28: [0, 0, 0], 29: [0, 0, 0], 30: [0, 0, 0], 31: [0, 0, 0], 32: [0, 0, 0], 33: [0, 0, 0], 34: [0, 0, 0], 35: [0, 0, 0], 36: [0, 0, 0], 37: [0, 0, 0], 38: [0, 0, 0], 39: [0, 0, 0], 40: [0, 0, 0], 41: [0, 0, 0], 42: [0, 0, 0], 43: [0, 0, 0], 44: [0, 0, 0], 45: [0, 0, 0], 46: [0, 0, 0], 47: [0, 0, 0], 48: [0, 0, 0], 49: [0, 0, 0]}
store = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 5: [0, 0, 0], 6: [0, 0, 0], 7: [0, 0, 0], 8: [0, 0, 0], 9: [0, 0, 0], 10: [0, 0, 0], 11: [0, 0, 0], 12: [0, 0, 0], 13: [0, 0, 0], 14: [0, 0, 0], 15: [0, 0, 0], 16: [0, 0, 0], 17: [0, 0, 0], 18: [0, 0, 0], 19: [0, 0, 0], 20: [0, 0, 0], 21: [0, 0, 0], 22: [0, 0, 0], 23: [0, 0, 0], 24: [0, 0, 0], 25: [0, 0, 0], 26: [0, 0, 0], 27: [0, 0, 0], 28: [0, 0, 0], 29: [0, 0, 0], 30: [0, 0, 0], 31: [0, 0, 0], 32: [0, 0, 0], 33: [0, 0, 0], 34: [0, 0, 0], 35: [0, 0, 0], 36: [0, 0, 0], 37: [0, 0, 0], 38: [0, 0, 0], 39: [0, 0, 0], 40: [0, 0, 0], 41: [0, 0, 0], 42: [0, 0, 0], 43: [0, 0, 0], 44: [0, 0, 0], 45: [0, 0, 0], 46: [0, 0, 0], 47: [0, 0, 0], 48: [0, 0, 0], 49: [0, 0, 0]}

rowstates = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 5: [0, 0, 0], 6: [0, 0, 0], 7: [0, 0, 0], 8: [0, 0, 0], 9: [0, 0, 0], 10: [0, 0, 0], 11: [0, 0, 0]}

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
LIME = (50, 205, 50)
GREEN = (0, 255, 0)
CYAN = (0, 100, 100)
LIGHT_BLUE = (173, 216, 230)
BLUE = (0, 0, 255)
PURPLE = (160, 32, 240)
MAGENTA = (255, 0, 255)
PINK = (255, 192, 203)
BROWN = (150, 75, 0)
BLACK = (0, 0, 0)
LIGHT_GRAY = (170, 170, 170)
GRAY = (85, 85, 85)
WHITE = (255, 255, 255)

COLORS = (RED, ORANGE, YELLOW, LIME, GREEN, CYAN, LIGHT_BLUE, BLUE, PURPLE, MAGENTA, PINK, BROWN, BLACK, LIGHT_GRAY, GRAY, WHITE)
RAINBOW = (RED, ORANGE, YELLOW, LIME, GREEN, CYAN, LIGHT_BLUE, BLUE, PURPLE, MAGENTA, PINK)
WATER = (CYAN, LIGHT_BLUE, BLUE)
CLASSIC = (RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

# Initialize strip of lights. 50 means I have 50 lights, 0 means something, 27 means pin 27 on my Rasberry Pi Pico, and "RGB" is RGB mode, of coursedar.

pixels = Neopixel(lightAmount, 0, 28, "RGB")
pixels.brightness(10)

spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 1)

# Define basic commands that can be used to make the lights do stuff.

def displayprint(message, delay):
    display.fill(0)
    length = len(message)
    char = 0
    while char < length:
        display.text(message[char] ,0, 0, 1)
        display.show()
        sleep(delay)
        display.fill(0)
        display.show()
        char += 1
        
def displayclear():
    displayprint(' ', .001)

def rpt(function, times):
    for i in range(times):
        function
        
def fill(r, g, b):
    pixels.fill((r, g, b))
    pixels.show()

def clear():
    pixels.clear()
    pixels.show()

def storepix(index):
    colors = states[index]
    r = colors[0]
    g = colors[1]
    b = colors[2]
    return [index, r, g, b]

def pix(index, r, g, b):
    pixels.set_pixel(index, (r, g, b))
    pixels.show()
    states[index] = [r, g, b]

def chase(r, g, b, delay):
    pixel = 0
    while pixel < lightAmount:
        pix(pixel, r, g, b)
        pixel += 1
        sleep(delay)
        pixels.clear()

def setrow(row, r, g, b):
    for index in rows[row]:
        pix(index, r, g, b)
        
def setcol(col, r, g, b):
    for index in cols[col]:
        pix(index, r, g, b)

def scan(direction, delay, r, g, b):
    if direction == 'up':
        row = -1
        while row < 11:
            row += 1
            clear()
            setrow(row, r, g, b)
            sleep(delay)
    elif direction == 'down':
        row = 12
        while row > 0:
            row -= 1
            clear()
            setrow(row, r, g, b)
            sleep(delay)
    elif direction == 'right':
        col = 0
        while col < 7:
            col += 1
            clear()
            setcol(col, r, g, b)
            sleep(delay)
    elif direction == 'left':
        col = 8
        while col > 0:
            col -= 1
            clear()
            setcol(col, r, g, b)
            sleep(delay)
    sleep(delay)
    clear()

def getlight(x, y):
    for light in cols[x]:
        if light in rows[y]:
            return light

def fallingparticle(particletype, starty, endy):
    if particletype == 'snow':
        xpos = random.randint(0, 7)
        ypos = starty
        prevlight = storepix(0)
        while ypos > endy:
            light = getlight(xpos, ypos)
            if light != None:
                prevlight = storepix(light)
                pix(light, 255, 255, 255)
                sleep(.1)
                pix(prevlight[0], prevlight[1], prevlight[2], prevlight[3])
            else:
                sleep(.1)
                pix(prevlight[0], prevlight[1], prevlight[2], prevlight[3])
            ypos -= 1
            
def updatesnowlayer(layers):
    for layer in range(layers):
        setrow(layer, 255, 255, 255)

def snow(intensity, fill, layersize):
    layers = -1
    fallenflakes = 0
    while True:
        if fill == False:
            sleep(1/intensity)
            fallingparticle('snow', 11, 0)
        elif fill == True:
            while layers < 11:
                while fallenflakes < layersize:
                    sleep(1/intensity)
                    fallingparticle('snow', 11, layers)
                    fallenflakes += 1
                fallenflakes = 0
                layers += 1
                updatesnowlayer(layers)

def rainbow(cycles, delay):
    cycle = 0
    while cycle < cycles:
        for stage in range(12):
            row = stage
            for color in RAINBOW:
                setrow(row, color[0], color[1], color[2])
                if row < 11:
                    row += 1
                else:
                    row = 0
                sleep(delay)
        cycle += 1

def watertree():
    pixel = 0
    while True:
        pix(pixel, 0, 0, random.randint(10, 255))
        if pixel < lightAmount - 3:
            pixel += random.randint(2, 3)
        else:
            pixel = 0
            
def classic(lighttype):
    if lighttype == 'colors':
        index = 0
        while index < lightAmount:
            color = CLASSIC[random.randint(0, 5)]
            pix(index, color[0], color[1], color[2])
            index += 1
            sleep(.001)
    elif lighttype == 'white':
        color = (255, 255, 255)
        fill(color[0], color[1], color[2])
    elif lighttype == 'green':
        color = (0, 255, 0)
        fill(color[0], color[1], color[2])
    elif lighttype == 'red':
        color = (255, 0, 0)
        fill(color[0], color[1], color[2])

clear()

###################################################
##        v    PROGRAM THE SHOW HERE  v          ##
###################################################


