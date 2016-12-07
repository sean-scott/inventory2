import time
import RPi.GPIO as GPIO
#import zbar
import lightshow

#from SimpleCV import Color, Camera, Display

ADD_PIN		= 24		# PIN for add button
REMOVE_PIN	= 23		# PIN for remove button

class Operation(object):
	def __init__(self):
		self.waiting = False;

def search(barcode):
	# do something with the barcode
	# while searching, do this...
	#display_search()
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

def on_press(channel):
	if operation.waiting:
		operation.waiting = False
		#display_clear()
	else:
		operation.waiting = True
		if channel == ADD_PIN:
			print "add"
			#display_add()	
		elif channel == REMOVE_PIN:
			print "remove"
			#display_remove()
		scan()

# GPIO setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Add Button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Subtract Button

GPIO.add_event_detect(24, GPIO.FALLING, callback=on_press, bouncetime=250)
GPIO.add_event_detect(23, GPIO.FALLING, callback=on_press, bouncetime=250)

if __name__ == '__main__':
	operation = Operation()

	try:
		while True:
			#Demo mode
			lightshow.display_add()
			time.sleep(1)
			lightshow.display_clear()
			lightshow.display_remove()
			time.sleep(1)
			lightshow.display_clear()
			lightshow.display_search()
			lightshow.display_search()
			lightshow.display_search()			
			lightshow.display_clear()
			time.sleep(1)
			lightshow.display_success_add()
			lightshow.display_clear()
			time.sleep(1)
			lightshow.display_success_remove()
			lightshow.display_clear()
			time.sleep(1)
			lightshow.display_failure()
			lightshow.display_clear()
			time.sleep(3)

			#pass
	except KeyboardInterrupt:
		GPIO.cleanup()
GPIO.cleanup()
