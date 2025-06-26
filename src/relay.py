import time

import RPi.GPIO as GPIO


def toggle(pin, timeout: int = 1):
  """
  Toggle the relay connected to the specified GPIO pin.
  This function turns the relay on, waits for 1 second, and then turns it off.
  """
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(timeout)
  GPIO.output(pin, GPIO.LOW)
