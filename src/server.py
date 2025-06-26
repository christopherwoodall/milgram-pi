from tools.relay import toggle as toggle_relay

import RPi.GPIO as GPIO


def main(pin: int = 22):
  print()
  # print("DO NOT ATTEMPT THIS OR MODIFY THIS FILE")
  PIN = pin
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)


  toggle_relay(PIN, timeout=9)


  print("test")
  GPIO.cleanup()


if __name__ == "__main__":
  main()
