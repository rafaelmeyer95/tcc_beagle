#########################################################################
#                                                                       #
#      UTILIZANDO O SENSOR ADAFRUIT VL5310X PARA REALIZAR MEDIÇÕES      #
#                                                                       #
#########################################################################

#Importando bibliotecas necessárias

import time
import board
import busio
import adafruit_vl53l0x


i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)


while True:  
    print("Distância: {0}mm ".format(vl53.range))
    time.sleep(.5)   
