#########################################################################
#                                                                       #
#         UTILIZANDO O SENSOR ADAFRUIT VL6180X PARA REALIZAR A          #
#          MEDIÇÃO DA DISTÂNCIA DA BOBINA ATÉ A ESFERA (MENOR)          #
#                                                                       #
#########################################################################

#Importando bibliotecas necessárias

import time
import board
import busio
import adafruit_vl6180x
import Adafruit_BBIO.PWM as PWM

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl6180x.VL6180X(i2c)

#sensor.measurement_timing_budget = 20000 #maior velocidade e menor precisão
sensor.measurement_timing_budget = 200000 #menor velocidade e maior precisão

PWM.start("P1_36",80,1000,0) #Com DC de 80% a esfera começa a tripidar em 12,7 mm

while True:
    print("Distância: {:.2f}".format(88 - sensor.range))
    time.sleep(.4)
    
