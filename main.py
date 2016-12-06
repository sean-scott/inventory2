import time
import RPi.GPIO as GPIO
import zbar

from SimpleCV import Color, Camera, Display
from neopixel import *

ADD_PIN		= 24		# PIN for add button
REMOVE_PIN	= 23		# PIN for remove button

# LED setup
LED_COUNT 	= 24		# Number of LED pixels
LED_PIN  	= 18		# GPIO pin connected to the pixels
LED_FREQ_HZ	= 800000	# Frequency in Hertz (usually 800kHz)
LED_DMA		= 5		# DMA channel for signal (usually 5)
LED_BRIGHTNESS	= 10		# 0-255 dark to brightest (blinding)
LED_INVERT	= False		# No inverters here...

class Operation(object):
	def __init__(self):
		self.waiting = False;

def search(barcode):
	# do something with the barcode
	# while searching, do this...
	display_search()
	# if-else for displaying success/fail LEDs

def scan():
	cam = Camera()
	img = cam.getImage()
	barcode = img.findBarcode()
	if (barcode is not None):
		barcode = barcode[0]
		result = str(barcode.data)
		print result
		barcode = []
		search(result)

def display_clear():
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))
	strip.show()

def display_search(wait_ms=50):
	for i in range(strip.numPixels()):	
		strip.setPixelColor(i, Color(255,255,255))
		if i > 2:
			strip.setPixelColor(i - 2, Color(0,0,0))
		strip.show()
		time.sleep(wait_ms/1000.0)
		

def display_add():
	for i in range(strip.numPixels()/2):
		strip.setPixelColor(i, Color(255,0,0))
	strip.show()		

def display_remove():
	for i in range(strip.numPixels()/2, strip.numPixels()):
		strip.setPixelColor(i, Color(0,255,0))
	strip.show()

def on_press(channel):
	if operation.waiting:
		operation.waiting = False
		display_clear()
	else:
		operation.waiting = True
		if channel == ADD_PIN:
			print "add"
			display_add()	
		elif channel == REMOVE_PIN:
			print "remove"
			display_remove()
		scan()

# GPIO setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Add Button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Subtract Button

GPIO.add_event_detect(24, GPIO.FALLING, callback=on_press, bouncetime=250)
GPIO.add_event_detect(23, GPIO.FALLING, callback=on_press, bouncetime=250)

if __name__ == '__main__':
	operation = Operation()

	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()

	try:
		print "Inventory 2.0"
		while True:
			pass
	except KeyboardInterrupt:
		GPIO.cleanup()
GPIO.cleanup()
