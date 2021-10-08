#########################################################################
#                                                                       #
#         UTILIZANDO O SENSOR ADAFRUIT VL5310X PARA REALIZAR A          #
#          MEDIÇÃO DA DISTÂNCIA DA BOBINA ATÉ A ESFERA (MAIOR)          #
#                                                                       #
#########################################################################

#Importando bibliotecas necessárias

import time
import board
import busio
import adafruit_vl53l0x
import Adafruit_BBIO.PWM as PWM

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

PWM.start("P1_36",100,1000,0)

while True:
    print("Distância: {:.2f}".format(129.2 - vl53.range))
    time.sleep(.004)
    