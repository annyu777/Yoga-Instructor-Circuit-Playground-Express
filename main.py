# CircuitPlaygroundExpress_Yoga_Insturctor 
import board
import neopixel
import time
import math
from math import sqrt
import array
from adafruit_circuitplayground.express import cpx

#set up LEDs
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.1)
pixels.fill((0,0,0))
pixels.show()


#simpleCircle: purple led goes around as a loop, providing a peaceful visual effect
def simpleCircle(wait):
    PURPLE1 = (59,18,97) #darkest
    PURPLE2 = (76,23,125) #medium
    PURPLE3 = (102,48,150) #lighest
    BLACK = (0, 0, 0) #LED turns off

    for i in range(len(pixels)):
        pixels[i] = PURPLE3
        if i+1 > 9:
            pixels[i+1-10] = PURPLE2
        else:
            pixels[i+1] = PURPLE2
        if i+2 > 9:
            pixels[i+2-10] = PURPLE1
        else:
            pixels[i+2] = PURPLE1
        time.sleep(wait)
        pixels[i] = BLACK

#standard_deviation helper function
def standard_deviation(lst):
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / num_items
    sd = sqrt(variance)
    return sd
    
#set up array for storing x,y,z from acceleration
x = [None] * 10
y = [None] * 10
z = [None] * 10

am_i_peaceful = False
peaceful_count = 0

while True:
    #run simpleCircle in the bg
    simpleCircle(0.05)
    
    #capture acceleration x,y,z every 0.01 sec
    for i in range(10):
        x[i],y[i],z[i] = cpx.acceleration
        print(i)
        print(len(x))
        print("X={:6.2f}\tY={:6.2f}\tZ={:6.2f}".format(x[i],y[i],z[i]))
        time.sleep(0.01)
    
    #calculate std for x,y,z in the past 0.1 sec
    x_std = standard_deviation(x)
    y_std = standard_deviation(y)
    z_std = standard_deviation(z)
    print("Xstd={:6.2f}\tYstd={:6.2f}\tZstd={:6.2f}".format(x_std,y_std,z_std))
    

    if ((x_std < 0.1) & (y_std < 0.1) & (z_std < 0.1)):
        pixels.fill((102,48,150))
        print("Peace detected!")
        time.sleep(1)
        cpx.play_file("Hermit Thrush-SoundBible.com-912282438 1.wav")




