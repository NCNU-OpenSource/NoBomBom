# ultrasonic.py
# Measure distance using an ultrasonic module
#
# Author : Matt Hawkins
# Date   : 10/01/2018

# Import required Python libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi (LED)
GPIO_TRIGGER_LED = 4
GPIO.setup(GPIO_TRIGGER_LED,GPIO.OUT)  # Trigger

def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(0.05)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.05)
	return

# Define GPIO to use on Pi (Ultrasonic)
GPIO_TRIGGER_1 = 23 # first out
GPIO_ECHO_1 = 24 #first in

GPIO_TRIGGER_2 = 17 # second out
GPIO_ECHO_2 = 18 # second in

GPIO_TRIGGER_3 = 27 # third out
GPIO_ECHO_3 = 22 # third in

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER_1,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_1,GPIO.IN)      # Echo
GPIO.setup(GPIO_TRIGGER_2,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_2,GPIO.IN)      # Echo
GPIO.setup(GPIO_TRIGGER_3,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_3,GPIO.IN)      # Echo

def send_trigger_pulse(test2):
	GPIO.output(test2, True)
	# Allow module to settle
	time.sleep(0.1)
	# Set trigger to False (Low)
	GPIO.output(test2, False)

def wait_for_echo(test,value,timeout):
	count = timeout
	while GPIO.input(test)!=value and count > 0:
		count = count-1
	# while GPIO.input(GPIO_ECHO_1)!=value and count > 0:
		# count = count-1
def get_distance(test,test2):
	
	send_trigger_pulse(test2) # Send 10us pulse to trigger

	wait_for_echo(test,True,500)
	start = time.time() 
	wait_for_echo(test,False,500)
	#wait_for_echo(False, 5000)
	finish = time.time() 
	elapsed = finish-start # Calculatsdasdsae pulse length
	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	# That was the distance there and back so halve the value
	distance = elapsed * 34000 / 2
	return (distance)

while True:
	print("no.1 devices:cm=%f" % get_distance(GPIO_ECHO_1,GPIO_TRIGGER_1))
	print("no.2 devices:cm=%f" % get_distance(GPIO_ECHO_2,GPIO_TRIGGER_2))
	print("no.3 devices:cm=%f" % get_distance(GPIO_ECHO_3,GPIO_TRIGGER_3))
	danger = 10
	if get_distance(GPIO_ECHO_1,GPIO_TRIGGER_1) < danger:
		blink(4) # first
	if get_distance(GPIO_ECHO_2,GPIO_TRIGGER_2) < danger:
		blink(5) # second
	if get_distance(GPIO_ECHO_3,GPIO_TRIGGER_3) < danger:
		blink(6) # third
	time.sleep(0.1)

# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
# Reset GPIO settings
GPIO.cleanup()
