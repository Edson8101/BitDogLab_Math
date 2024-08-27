from machine import Pin, ADC, PWM, SoftI2C
import neopixel
import time
from ssd1306 import SSD1306_I2C
import utime

# ==============================  DECLARAÇÃO DE VARIÁVEIS =======================================

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

# =====================================  INTERFACE DE APRESENTAÇÃO ==================================

for i in range(NUM_LEDS):
    np[i] = (0, 0, 0)

for i in range(NUM_LEDS):
    np[i] = (2, 2, 2)
    np.write()
    time.sleep(0.1)

oled.fill(0)  # Limpar display
oled.text("OLA, ALUNO!", 0, 0)
oled.text("BEM VINDO!", 0, 10)
oled.show()

# Conecte o alto-falante ou buzzer passivo ao pino GP4
alto_falante = PWM(Pin(21))

# Conecte o LED RGB aos pinos GP13, GP12 e GP14
led_red = PWM(Pin(13))
led_green = PWM(Pin(12))
led_blue = PWM(Pin(14))

# Frequências das notas musicais (escala temperada)
notas = {
    'C4': 261,
    'D4': 294,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523,
    'G3': 196,  # Sol uma oitava abaixo
    'A#4': 466, # Lá sustenido
    'PAUSA': 0
}

# Música "Super Mario Bros" - Parte Inicial
musica_super_mario = [
    ('E4', 1), ('E4', 1), ('E4', 1), ('C4', 1), ('E4', 1), ('G4', 2), ('G3', 4)
]

def tocar_musica(musica):
    for nota, duracao in musica:
        freq = notas[nota]
        alto_falante.freq(freq)
        alto_falante.duty_u16(32768 if freq > 0 else 0)
        time.sleep_ms(170 * duracao)  # Controla a duração das notas
        alto_falante.duty_u16(0)
        time.sleep_ms(50)  # Pequena pausa entre as notas

tocar_musica(musica_super_mario)

mat = [24,15,14,5,4,6,12,8,0,9,10,19,20]

for i in mat:
    np[i] = (0,2,0)
    np.write()
    time.sleep(0.1)
    
for i in range(NUM_LEDS):
    np[i] = (0, 0, 0)

for i in rosto_feliz:
    np[i] = (0,2,0)
    np.write()

time.sleep(0.5)

np[6] = (0,0,0)
np.write()
time.sleep(0.2)
np[6] = (0,2,0)
np.write()

time.sleep(3)

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# ==============================  CLASSE PARA PERGUNTAS ==============================================

class Question(): 
    
    def pergunta01(self):
        # Suponhando que a matriz de LED seja um gráfico com coordenadas (x,y), qual é o tipo de função apresentada? 
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)

        question01 = [24, 16, 12, 8, 0]

        for i in question01:
            np[i] = (2, 2, 2)
            np.write()
    
    def pergunta02(self):
        # Qual é a probabilidade de escolher um LED com a cor vermelha entre todas as cores apresentadas na matriz de LED?
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)

        red = [0,2,5,7,8,12]
        green = [1,3,4,6,9,15,18,19,20,21]
        blue = [10,11,13,14,16,17,22,23,24]
        
        for i in red:
            np[i] = (2, 0, 0)
            np.write()
        for i in green:
            np[i] = (0, 2, 0)
            np.write()
        for i in blue:
            np[i] = (0, 0, 2)
            np.write()   
                
    def pergunta03(self):
        
        print("Espaço da Pergunta 03")
 
    def pergunta04(self):
        
        print("Espaço da Pergunta 04")
        
    def pergunta05(self):
        
        print("Espaço da Pergunta 05")
        
    def pergunta06(self):
        
        print("Espaço da Pergunta 06")
        
    def pergunta07(self):
        
        print("Espaço da Pergunta 07")
        
    def pergunta08(self):
        
        print("Espaço da Pergunta 08")
        
    def pergunta09(self):
        
        print("Espaço da Pergunta 09")
               
    def pergunta10(self):
        
        print("Espaço da Pergunta 10")            

pergunta = Question()

# ===============================   ESCOLHA DAS ALTERNATIVAS =============================
def opcoes(alternativa_correta):
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
            np[i] = (0, 2, 0)
            np.write()
            
        if button_a.value() == 0:
            for i in range(NUM_LEDS):
                np[i] = (0, 0, 0)
            if b==alternativa_correta:
                for i in rosto_feliz:
                    np[i]=(0,2,0)
                    np.write()
                time.sleep(2)
                for i in range(NUM_LEDS):
                    np[i] = (0, 0, 0)
                    np.write()
                escolha = False
            else:
                for i in rosto_triste:
                    np[i]=(2,0,0)
                    np.write()
                time.sleep(2)
                for i in range(NUM_LEDS):
                    np[i] = (0, 0, 0)
                    np.write()
                escolha = False
                    
        if button_b.value() == 0:
            escolha = False
    # Esperar um pouco antes da próxima leitura
        time.sleep(0.1)

# =================================== INTERFACE PRINCIPAL ==========================================

escolhidas = []

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
    oled.text("(A) Selecionar", 0, 20)
    oled.text("(B) Voltar", 0, 30)

    for i in lista:
        if i == c:
            oled.text("Questao {}".format(c+1), 0, 10)
            oled.show()
            if button_a.value() == 0:
                if c==0:
                    pergunta.pergunta01()
                    time.sleep(10)
                    opcoes(0)
                elif c==1:
                    pergunta.pergunta02()
                    time.sleep(10)
                    opcoes(1)
                elif c==2:
                    pergunta.pergunta03()
                    time.sleep(10)
                    opcoes(2)
                elif c==3:
                    pergunta.pergunta04()
                    time.sleep(10)
                    opcoes(3)
                elif c==4:
                    pergunta.pergunta05()
                    time.sleep(10)
                    opcoes(4)
                elif c==5:
                    pergunta.pergunta06()
                    time.sleep(10)
                    opcoes(0)
                elif c==6:
                    pergunta.pergunta07()
                    time.sleep(10)
                    opcoes(1)
                elif c==7:
                    pergunta.pergunta08()
                    time.sleep(10)
                    opcoes(2)
                elif c==8:
                    pergunta.pergunta09()
                    time.sleep(10)
                    opcoes(3)
                elif c==9:
                    pergunta.pergunta10()
                    time.sleep(10)
                    opcoes(4)
                escolhidas.append(c)       
    # Esperar um pouco antes da próxima leitura
    time.sleep(0.1)
