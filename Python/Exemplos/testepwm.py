import Adafruit_BBIO.PWM as PWM
import time

pwm = 0

while True:
    PWM.start("P1_36",pwm,1000,0)
    pwm = int(input('Digite o valor do PWM: '))
    time.sleep(0.04)
    
