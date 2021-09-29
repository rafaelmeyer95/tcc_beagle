import Adafruit_BBIO.PWM as PWM
import time

while True:
    PWM.start("P1_36",0,1000,0)
    time.sleep(0.04)
    
