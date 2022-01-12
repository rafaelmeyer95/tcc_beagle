#########################################################################
#                                                                       #
#    UTILIZANDO O SENSOR ADAFRUIT VL5310X PARA REALIZAR A MEDIÇÃO DA    #
#    DISTÂNCIA DO SENSOR ATÉ A ESFERA (MENOR) EM POSIÇÃO DE REPOUSO     #
#                                                                       #
#########################################################################

#Importando bibliotecas necessárias

import time
import board
import busio
import adafruit_vl6180x

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl6180x.VL6180X(i2c)

#sensor.measurement_timing_budget = 20000 #maior velocidade e menor precisão
sensor.measurement_timing_budget = 200000 #menor velocidade e maior precisão

for y in range(10):                              #Loop que informa o valor das médias obtidas

    soma=0                                       # Zerando a variável auxiliar para calcular uma nova média
    
    for x in range(100):                       #Loop que realiza 10.000 medições
        soma=soma+sensor.range                     #Variável auxiliar para calculo da média
        time.sleep(.001)                         #Intervalo de um milésimo entre as medições
    
    media=soma/100                             #Calculando a média entre as 10000 medições realizadas
    print("A média é: {0}mm".format(media))      #Informa o valor de cada média calculada
    
    #Chegou-se com esse código a uma distância de 88 mm