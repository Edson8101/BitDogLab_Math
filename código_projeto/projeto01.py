from machine import Pin, ADC, PWM, SoftI2C
import neopixel
import time
from ssd1306 import SSD1306_I2C
import utime

# Inicializar ADC para os pinos VRx (GPIO26) e VRy (GPIO27)
adc_vrx = ADC(Pin(26))
adc_vry = ADC(Pin(27))

# Configuração dos botões
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

c=0
lista = [0,1,2,3,4,5,6,7,8,9]


# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Definindo a matriz de LEDs
LED_MATRIX = [
    [24, 23, 22, 21, 20],
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

alternativa = [[23,2,21,16,13,6,3,18,11,8,1,12],[23,22,21,16,13,6,3,18,8,1,12,2],[23,22,21,16,13,6,3,1,2],[23,22,16,13,6,3,18,11,8,2],[23,22,21,16,13,6,3,1,12,2]]

rosto_feliz = [6,8,15,23,22,21,19]
rosto_triste = [6,8,24,16,17,18,20]

def pergunta01():
    # Desligar todos os LEDs
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)

    question01 = [20, 18, 12, 6, 4]

    for i in question01:
        np[i] = (20, 20, 20)
        np.write()
        time.sleep(15)


def opcoes():
    b=0
    escolha = True
    while escolha:
    # Ler valores analógicos de VRx e VRy
        vrx_value = adc_vrx.read_u16()
        vry_value = adc_vry.read_u16()

        if vry_value < 20000:
            b+=1
            if b>4:
                b=0
        elif vry_value > 40000:
            b-=1
            if b<0:
                b=4

    # Desligar todos os LEDs
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)
 
        for i in alternativa[b]:
            np[i] = (0, 20, 0)
            np.write()
            
        if button_a.value() == 0:
            for i in range(NUM_LEDS):
                np[i] = (0, 0, 0)
            if b==3:
                for i in rosto_feliz:
                    np[i]=(0,20,0)
                    np.write()
                time.sleep(2)
            else:
                for i in rosto_triste:
                    np[i]=(20,0,0)
                    np.write()
                time.sleep(2)
                    
        if button_b.value() == 0:
            escolha = False
    # Esperar um pouco antes da próxima leitura
        time.sleep(0.1)

while True:
    # Ler valores analógicos de VRx e VRy
    vrx_value = adc_vrx.read_u16()
    vry_value = adc_vry.read_u16()
    
    if vry_value < 20000:
        c+=1
        if c>9:
            c=0
    elif vry_value > 40000:
        c-=1
        if c<0:
            c=9
    # Teste OLED
    oled.fill(0)  # Limpar display
    oled.text("PERGUNTA", 0, 0)

    for i in lista:
        if i == c:
            oled.text("Questao {}".format(c+1), 0, 10)
            oled.show()
            if button_a.value() == 0:
                pergunta01()
                opcoes()
    
    # Esperar um pouco antes da próxima leitura
    time.sleep(0.1)
