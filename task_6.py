import machine
import time
import neopixel

"""
MicroPython v1.19.1/ESP32-C3-DevKitM-1 exercise:
Simple testing on onboard RGB LED (Neopixel).
"""

# On Espreffif ESP32-C3-DevKitM-1:
# The onboard RGB LED (WS2812) is connected to GPIO8

np = neopixel.NeoPixel(machine.Pin(2), 1)

while True:
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)
    np[0] = (255, 0, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 255, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 0, 255)
    np.write()
    time.sleep(1)
    np[0] = (255, 255, 255)
    np.write()
    time.sleep(1)