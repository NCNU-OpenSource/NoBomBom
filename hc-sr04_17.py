# ultrasonic_1.py
# Measure distance using an ultrasonic module
#
# Author : Matt Hawkins
# Date   : 09/01/2013

# Import required Python libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi (LED)
GPIO_TRIGGER = 4
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger

def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(0.05)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(0.05)
	return

# Define GPIO to use on Pi (Ultrasonic)
GPIO_TRIGGER = 17
GPIO_ECHO = 18

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

def send_trigger_pulse():
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

def wait_for_echo(value,timeout):
	count = timeout
	while GPIO.input(GPIO_ECHO)!=value and count > 0:
		count = count-1
def get_distance():
	send_trigger_pulse()
	wait_for_echo(True, 5000)
	start = time.time()
	wait_for_echo(False, 5000)
	finish = time.time()
	elapsed = finish-start
	distance = elapsed * 34000 / 2
	return (distance)

while True:
    print("cm=%f" % get_distance())
    if get_distance() < 10:
        blink(4)
    time.sleep(0.1)


# Set trigger to False (Low)
# GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
# time.sleep(0.5)

# Send 10us pulse to trigger

# start = time.time()
# while GPIO.input(GPIO_ECHO)==0:
#   start = time.time()

# while GPIO.input(GPIO_ECHO)==1:
#   stop = time.time()

# Calculate pulse length
# elapsed = stop-start

# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
# distance = elapsed * 34000

# That was the distance there and back so halve the value
# distance = distance / 2

# print "Distance : %.1f" % distance

# Reset GPIO settings
GPIO.cleanup()
