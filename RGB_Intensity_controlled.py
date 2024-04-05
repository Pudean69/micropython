import machine
import time
import neopixel

"""
MicroPython v1.19.1/ESP32-C3-DevKitM-1 exercise:
Control onboard RGB LED (Neopixel), with level control.
"""

# On Espreffif ESP32-C3-DevKitM-1:
# The onboard RGB LED (WS2812) is connected to GPIO8

np = neopixel.NeoPixel(machine.Pin(2), 1)

def setNeoPixel(level, enable):
    np[0] = (level * enable[0],
             level * enable[1],
             level * enable[2])
    np.write()
    
def testNeoPixel(enable):
    for l in range(0, 256):
        setNeoPixel(l, enable)
        time.sleep(0.02)

while True:
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)

    testNeoPixel([True, False, False])
    testNeoPixel([False, True, False])
    testNeoPixel([False, False, True])
    
    testNeoPixel([True, True, False])