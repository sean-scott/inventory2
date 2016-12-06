import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Add Button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Subtract Button

def add_barcode(channel):
	print "Adding item..."

def minus_barcode(channel):
	print "Removing item..."

GPIO.add_event_detect(24, GPIO.FALLING, callback=add_barcode, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=minus_barcode, bouncetime=300)

try:
	print "Inventory 2.0"
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()
