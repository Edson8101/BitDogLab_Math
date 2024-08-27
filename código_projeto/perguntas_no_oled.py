from machine import ADC, Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import neopixel, time

adc_vry = ADC(Pin(27)) # inicializa analog_y
button_a = Pin(5, Pin.IN, Pin.PULL_UP) # inicializa
button_b = Pin(6, Pin.IN, Pin.PULL_UP) # inicializa
i2c = SoftI2C(scl=Pin(15), sda=Pin(14)) # inicializa display oled
oled = SSD1306_I2C(128, 64, i2c) # cabe 6*16 caracteres
NUM_LEDS = 25 # inicializa matriz leds
obj_leds5x5 = neopixel.NeoPixel(Pin(7), NUM_LEDS) # inicializa matriz leds

# Constantes
lim_min_y =15000 # limiar inferior do joystick analogico 
lim_max_y =45000 # limiar superior do joystick analogico
num_texto = 0 # inicializacao do indice do texto
espera = 0.20 # tempo entre leituras do analogico em seg

def logica_circular(entrada,maxi):
    if entrada > maxi:
        entrada = 0
    if entrada < 0:
        entrada = maxi
    return entrada

def string_A():
    oled.fill(0)
    #led.text("6543210987654321", 0, 70) #referencia 16 caracteres
    oled.text("Qual e o tipo de",0,0)
    oled.text("funcao mostrada?",0,10)
    oled.text("A: parabola",0,20)

def string_B():
    oled.fill(0)
    oled.text("Qual e o tipo de",0,0)
    oled.text("funcao mostrada?",0,10)
    oled.text("B: exponencial",0,20)

def string_C():
    oled.fill(0)
    oled.text("Qual e o tipo de",0,0)
    oled.text("funcao mostrada?",0,10)
    oled.text("C: linear",0,20)

def string_D():
    oled.fill(0)
    oled.text("Qual e o tipo de",0,0)
    oled.text("funcao mostrada?",0,10)
    oled.text("D: circulo",0,20)

def string_E():
    oled.fill(0)
    oled.text("Qual e o tipo de",0,0)
    oled.text("funcao mostrada?",0,10)
    oled.text("E: cosseno",0,20)

def exibe_texto_oled(string1a5):
    if string1a5 == 0:
        string_A()
    elif string1a5 == 1:
        string_B()
    elif string1a5 == 2:
        string_C()
    elif string1a5 == 3:
        string_D()
    elif string1a5 == 4:
        string_E()

# Menu de selecao de numero da alternativa
while True:
    analog_Y = adc_vry.read_u16() # le joystick
    if analog_Y < lim_min_y: # compara com limiar
        num_texto+=1
        num_texto = logica_circular(num_texto,4)
    elif analog_Y > lim_max_y: # compara com limiar
        num_texto-=1
        num_texto = logica_circular(num_texto,4)
    exibe_texto_oled(num_texto)
    oled.show()
    time.sleep(espera)


