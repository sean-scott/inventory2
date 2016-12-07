import time
from neopixel import *

# LED setup
LED_COUNT       = 24            # Number of LED pixels
LED_PIN         = 18            # GPIO pin connected to the pixels
LED_FREQ_HZ     = 800000        # Frequency in Hertz (usually 800kHz)
LED_DMA         = 5             # DMA channel for signal (usually 5)
LED_BRIGHTNESS  = 10            # 0-255 dark to brightest (blinding)
LED_INVERT      = False         # No inverters here...

# Animations

# Clear
# Turns off all LEDs
def clear():
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, Color(0,0,0))
        strip.show()

# Add
# Top half lit green
def add():
        for i in range(strip.numPixels()/2):
                strip.setPixelColor(i, Color(255,0,0))
        strip.show()

# Remove
# Bottom half lit red
def remove():
        for i in range(strip.numPixels()/2, strip.numPixels()):
                strip.setPixelColor(i, Color(0,255,0))
        strip.show()

# Search
# A chasing white wheel
def search(wait_ms=50):
	lit_leds = [0, 1, 2]
	for i in range(strip.numPixels()):
		clear()
		for j in range(len(lit_leds)):
			lit_leds[j] += 1
			if (lit_leds[j] == strip.numPixels()):
				lit_leds[j] = 0
			strip.setPixelColor(lit_leds[j], Color(255,255,255))
                strip.show()
                time.sleep(wait_ms/1000.0)		

# Success - Add
# Three green blinks
def success_add(wait_ms=250):
	for i in range(3):

		for j in range(strip.numPixels()):
			strip.setPixelColor(j, Color(255,0,0))
		strip.show()
		time.sleep(wait_ms/1000.0)

		clear()
		time.sleep(wait_ms/1000.0)

# Success - Remove
# Three red blinks
def success_remove(wait_ms=250):
        for i in range(3):

                for j in range(strip.numPixels()):
                        strip.setPixelColor(j, Color(0,255,0))
                strip.show()
                time.sleep(wait_ms/1000.0)

                clear()
                time.sleep(wait_ms/1000.0)

# Failure
# Three yellow blinks
def failure(wait_ms=250):
        for i in range(3):

                for j in range(strip.numPixels()):
                        strip.setPixelColor(j, Color(255,255,0))
                strip.show()
                time.sleep(wait_ms/1000.0)

		clear()
                time.sleep(wait_ms/1000.0)

# Initialization
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()
