import RPi.GPIO as GPIO
import time

current_state = 0

def setup():
  pir_sensor = 11
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pir_sensor, GPIO.IN)

def check_motion():
  global current_state
  try:
    current_state = GPIO.input(pir_sensor)
  except:
    print('Problem Occurred while checking state of sensor!')
  finally:
    return current_state

def reset_state():
  global current_state
  current_state = 0
  return ''
