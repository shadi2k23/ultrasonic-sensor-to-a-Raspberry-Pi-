import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG = 17
ECHO = 27

# Setup GPIO
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Function to measure distance
def measure_distance():
    # Set trigger to HIGH
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    # Measure the start time
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Measure the stop time
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Calculate the distance
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Speed of sound is 343 m/s

    return distance

if __name__ == '__main__':
    try:
        while True:
            distance = measure_distance()
            print("Distance: %.1f cm" % distance)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
