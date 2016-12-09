import lightshow
import lookup
import RPi.GPIO as GPIO
#from SimpleCV import Color, Camera, Display
import time
#import zbar

ADD_PIN		= 24		# PIN for add button
REMOVE_PIN	= 23		# PIN for remove button

BARCODE = "640522710386"	# test barcode

class Operation(object):
	def __init__(self):
		self.waiting = False;

def search(barcode):
	lightshow.search()
	lightshow.clear()
	product = lookup.getProductJSON(barcode)
	name = lookup.getProductName(product)	
	print(name)

def scan():
	cam = Camera()
	img = cam.getImage()
	barcode = img.findBarcode()
	if (barcode is not None):
		barcode = barcode[0]
		result = str(barcode.data)
		print(result)
		barcode = []
		search(result)

def on_press(channel):
	if operation.waiting:
		operation.waiting = False
		#clear()
	else:
		operation.waiting = True
		if channel == ADD_PIN:
			print("add")
			#add()	
		elif channel == REMOVE_PIN:
			print("remove")
			#remove()
		scan()

def demo_mode():
	#Demo mode
	lightshow.add()
	time.sleep(1)
	lightshow.clear()
	lightshow.remove()
	time.sleep(1)
	lightshow.clear()
	lightshow.search()
	lightshow.search()
	lightshow.search()			
	lightshow.clear()
	time.sleep(1)
	lightshow.success_add()
	lightshow.clear()
	time.sleep(1)
	lightshow.success_remove()
	lightshow.clear()
	time.sleep(1)
	lightshow.failure()
	lightshow.clear()
	time.sleep(3)

# GPIO setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Add Button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Subtract Button

GPIO.add_event_detect(24, GPIO.FALLING, callback=on_press, bouncetime=250)
GPIO.add_event_detect(23, GPIO.FALLING, callback=on_press, bouncetime=250)

if __name__ == '__main__':
	operation = Operation()
	search(BARCODE) # search demo

	try:
		while True:
			pass
	except KeyboardInterrupt:
		GPIO.cleanup()
GPIO.cleanup()
