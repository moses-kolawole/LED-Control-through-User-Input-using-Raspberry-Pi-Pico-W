from machine import Pin
import time

led = Pin(6, Pin.OUT)

while True:
    CMD = input('what is your command? (ON/OFF/TOGGLE): ').strip()    
    if (CMD.upper() == 'ON'):
        led.value(1)
    if (CMD.upper() == 'OFF'):
        led.value(0)
    if (CMD.upper() == 'TOGGLE'):
        led.toggle()