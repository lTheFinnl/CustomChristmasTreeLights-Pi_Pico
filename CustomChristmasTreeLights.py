# Initialize and import stuff.

from neopixel import Neopixel
from time import sleep
import random
import max7219
from machine import Pin, SPI


# Define some parameters. These dictonaries include all of the lights ordered by x-position, y-position, and the last has each light's coordinates.

lightAmount = 50

rows = {0: (0, 24, 25, 49, 23), 1: (1, 26, 48), 2: (47, 2, 27, 22), 3: (21, 28, 3, 46), 4: (45, 4, 29, 19, 20), 5: (44, 5, 30), 6: (43, 6, 18, 31), 7: (32, 42, 7, 17), 8: (8, 16, 33, 41), 9: (15, 34, 9, 40), 10: (14, 35, 39, 10), 11: (13, 30, 11, 38, 37, 36, 12)}
cols = {0: (49, 48, 47, 46, 45), 1: (44, 43, 42), 2: (41, 40, 39), 3: (38, 10, 1, 3, 5, 7, 11), 4: (37, 9, 8, 6, 4, 2, 0), 5: (12, 36, 32, 30, 27, 35), 6: (13, 34, 33, 31, 29, 26), 7: (14, 15, 17, 25, 18, 28), 8: (24, 22, 19, 16), 9: (20, 21, 23)}
coords = {0: (4, 0), 1: (3, 1), 2: (4, 2), 3: (3, 3), 4: (4, 4), 5: (3, 5), 6: (4, 6), 7: (3, 7), 8: (4, 8), 9: (4, 9), 10: (3, 10), 11: (3, 11), 12: (5, 11), 13: (6, 11), 14: (7, 10), 15: (7, 9), 16: (8, 8), 17: (7, 7), 18: (7, 6), 19: (8, 4), 20: (9, 4), 21: (9, 3), 22: (8, 2), 23: (9, 0), 24: (8, 0), 25: (7, 0), 26: (6, 1), 27: (5, 2), 28: (7, 3), 29: (6, 4), 30: (5, 5), 31: (6, 6), 32: (5, 7), 33: (6, 8), 34: (6, 9), 35: (5, 10), 36: (5, 11), 37: (4, 11), 38: (3, 11), 39: (2, 10), 40: (2, 9), 41: (2, 8), 42: (1, 7), 43: (1, 6), 44: (1, 5), 45: (0, 4), 46: (0, 3), 47: (0, 2), 48: (0, 1), 49: (0, 0)}

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

def coordkeyget(value):
    for k, v in coords.items():
        if value == v:
            return k

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
    
def pixcoord(x, y, r, g, b):
    for pixel in coords:
        coordinates = coords.get(pixel)
        if coordinates[0] == x and coordinates[1] == y:
            pix(pixel, r, g, b)
            
def pixregion(x1, y1, x2, y2, r, g, b):
    width = x2 - x1 + 1
    height = y2 - y1 + 1
    print((width, height))
    pixels = []
    x = x1
    y = y1
    while y <= y2:
        while x <= x2:
            pixcoord(x, y, r, g, b)
            x += 1
        x = x1
        y += 1

def chase(r, g, b, delay):
    pixel = 0
    while pixel < lightAmount:
        pix(pixel, r, g, b)
        pixel += 1
        sleep(delay)
        pixels.clear()

def setrow(row, r, g, b):
    for coord in coords.values():
        if coord[1] == row:
            index = coordkeyget(coord)
            pix(index, r, g, b)

def setcol(col, r, g, b):
    for coord in coords.values():
        if coord[0] == col:
            index = coordkeyget(coord)
            pix(index, r, g, b)

def scan(direction, delay, r, g, b):
    if direction == 'up':
        row = 0
        while row <= 11:
            setrow(row, r, g, b)
            sleep(delay)
            clear()
            row += 1
    elif direction == 'down':
        row = 11
        while row >= 0:
            setrow(row, r, g, b)
            sleep(delay)
            clear()
            row -= 1
    elif direction == 'right':
        col = 0
        while col <= 9:
            setcol(col, r, g, b)
            sleep(delay)
            clear()
            col += 1
    elif direction == 'left':
        col = 9
        while col >= 0:
            setcol(col, r, g, b)
            sleep(delay)
            clear()
            col -= 1

    sleep(delay)
    clear()

def getlight(x, y):
    coordinate = (x, y)
    light = coordkeyget(coordinate)
    return light

def fallingparticle(particletype, starty, endy):
    if particletype == 'snow':
        xpos = random.randint(0, 9)
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
            while layers <= 11:
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
        
def graphline(thickness, m, b, r, g, bl):
    for index in coords:
        coord = coords[index]
        x = coord[0]
        y = coord[1]
        if (x * m) + b == y:
            pix(index, r, g, bl)
            sleep(.001)
        elif abs(((x * m) + b) - y) < thickness:
            pix(index, r, g, bl)
            sleep(.01)
    displayprint('y={}x+{}'.format(m, b), .5)
            
def graphparabola(thickness, a, h, k, r, g, b):
    for index in coords:
        coord = coords[index]
        x = coord[0]
        y = coord[1]
        if a * (x - h)**2 + k == y:
            pix(index, r, g, b)
            sleep(.001)
        elif abs((a * (x - h)**2 + k) - y) < thickness:
            pix(index, r, g, b)
            sleep(.01)
    displayprint('y={}(x-{})^2+{}'.format(a, h, k), .5)

clear()
displayclear()

###################################################


