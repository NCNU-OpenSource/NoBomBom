# Import required Python libraries
import time
import RPi.GPIO as GPIO
# blinking function
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return
# try
GPIO.setmode(GPIO.BCM)
# to use Raspberry Pi board pin numbers
# GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel, we set GPIO4 (pin 7) to OUTPUT
GPIO_TRIGGER = 4
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)


# blink GPIO4 (Pin 7) 50 times
#for i in range(0,50):
#   blink(4)
# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24

print "Ultrasonic Measurement"
blink(4)

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle
time.sleep(0.5)

# Send 10us pulse to trigger
GPIO.output(GPIO_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)
start = time.time()
while GPIO.input(GPIO_ECHO)==0:
  start = time.time()

while GPIO.input(GPIO_ECHO)==1:
  stop = time.time()

# Calculate pulse length
elapsed = stop-start

# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
distance = elapsed * 34000

# That was the distance there and back so halve the value
distance = distance / 2

print "Distance : %.1f" % distance

# Reset GPIO settings
GPIO.cleanup()
