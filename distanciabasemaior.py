#########################################################################
#                                                                       #
#    UTILIZANDO O SENSOR ADAFRUIT VL5310X PARA REALIZAR A MEDIÇÃO DA    #
#    DISTÂNCIA DO SENSOR ATÉ A ESFERA (MAIOR) EM POSIÇÃO DE REPOUSO     #
#                                                                       #
#########################################################################

#Importando bibliotecas necessárias

import time
import board
import busio
import adafruit_vl53l0x


i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

for y in range(10):                              #Loop que informa o valor das médias obtidas

    soma=0                                       # Zerando a variável auxiliar para calcular uma nova média
    
    for x in range(10000):                       #Loop que realiza 10.000 medições
        soma=soma+vl53.range                     #Variável auxiliar para calculo da média
        time.sleep(.001)                         #Intervalo de um milésimo entre as medições
    
    media=soma/10000                             #Calculando a média entre as 10000 medições realizadas
    print("A média é: {0}mm".format(media))      #Informa o valor de cada média calculada
    
    #Chegou-se com esse código a uma distância de 129,2 mm