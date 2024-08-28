from machine import Pin, ADC, PWM, SoftI2C
from ssd1306 import SSD1306_I2C
import neopixel, time, utime

# ==========================  INICIALIZACAO DE PERIFERICOS =========================
adc_vrx = ADC(Pin(26)) # inicializa pino VRx (GPIO26)
adc_vry = ADC(Pin(27)) # inicializa pino VRx (GPIO27)
button_a = Pin(5, Pin.IN, Pin.PULL_UP) # configura botao A
button_b = Pin(6, Pin.IN, Pin.PULL_UP) # configura botao B
led_red = PWM(Pin(13)) # inicializa LED RGB no pino GP13
led_green = PWM(Pin(12)) # inicializa LED RGB no pino GP12
#led_blue = PWM(Pin(14)) # inicializa no pino GP14, nao pode, sera usado por oled
i2c = SoftI2C(scl=Pin(15), sda=Pin(14)) # configura Display oled no GP14
oled = SSD1306_I2C(128, 64, i2c) # configura Display oled 128x64 pixels
NUM_LEDS = 25 # Número de LEDs na sua matriz 5x5
np = neopixel.NeoPixel(Pin(7), NUM_LEDS) # Inicializa matriz LEDs no GPIO7
alto_falante = PWM(Pin(21)) # inicializa buzzer passivo no pino GP4
# ==========================  INICIALIZACAO DE PERIFERICOS =========================

# ============================  DEFINIÇÃO DE CONSTANTES ============================
cont_pergunta=0
lista_pergunta = [0,1,2,3,4]

# Referencia para matriz de LEDs, Atenção, é um Zig-Zag!!
#  4, 3, 2, 1, 0
#  5, 6, 7, 8, 9
# 14,13,12,11,10
# 15,16,17,18,19
# 24,23,22,21,20

# LEDS das Alternativas
A = [23,2,21,16,13,6,3,18,11,8,1,12]
B = [23,22,21,16,13,6,3,18,8,1,12,2]
C = [23,22,21,16,13,6,3,1,2]
D = [23,22,16,13,6,3,18,11,8,2]
E = [23,22,21,16,13,6,3,1,12,2]

alternativa = [A,B,C,D,E]

rosto_feliz = [6,8,15,23,22,21,19]
rosto_triste = [6,8,24,16,17,18,20]

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
    ('E4',5),('E4',8),('E4',10),('C4',4),('E4',8),('G4',20),('G3',16)]
tempo_mario = 32
volume = 1000 # Era 32768
# ===========================  DEFINIÇÃO DE CONSTANTES =========================


# ==========================  FUNCOES PARA APRESENTACAO =========================
def tocar_musica(musica):
    for nota, duracao in musica:
        freq = notas[nota]
        alto_falante.freq(freq)
        alto_falante.duty_u16(volume if freq > 0 else 0) # era 32768
        time.sleep_ms(tempo_mario*duracao)  # Controla a duração das notas
        alto_falante.duty_u16(0)
        time.sleep_ms(50)  # Pequena pausa entre as notas

# Funcoes da apresentacao
def limpa_matriz_leds():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)

def preenche_matriz_led_zig_zag():
    for i in range(NUM_LEDS):
        np[i] = (2, 2, 2)
        np.write()
        time.sleep(0.045)

def ola_aluno_bem_vindo():
    oled.fill(0)  # Limpar display
    oled.text("OLA, ALUNO!", 0, 0)
    oled.text("BEM VINDO!", 0, 10)
    oled.show()

def letra_m():
    mat = [24,15,14,5,4,6,12,8,0,9,10,19,20]
    for i in mat:
        np[i] = (0,2,0)
        np.write()
        time.sleep(0.1)

def rosto_feliz_piscando():
    for i in rosto_feliz:
        np[i] = (0,2,0)
        np.write()
    time.sleep(0.5)
    # Piscada
    np[6] = (0,0,0)
    np.write()
    time.sleep(0.2)
    np[6] = (0,2,0)
    np.write()
# ==========================  FUNCOES PARA APRESENTACAO =========================


# ===========================  SEQUENCIA DE APRESENTAÇÃO ========================
limpa_matriz_leds()
preenche_matriz_led_zig_zag()
ola_aluno_bem_vindo()
tocar_musica(musica_super_mario)
letra_m()
limpa_matriz_leds()
rosto_feliz_piscando()
time.sleep(3)

#Eh necessário fazer essa configuração novamente porque o pino do oled coincide com o pino do buzzer
i2c = SoftI2C(scl=Pin(15), sda=Pin(14)) # configura Display oled no GP14
oled = SSD1306_I2C(128, 64, i2c) # configura Display oled 128x64 pixels

# ===========================  SEQUENCIA DE APRESENTAÇÃO ========================


# =============================  CLASSE PARA PERGUNTAS ==========================
class Question(): 
    
    def pergunta01(self):
        # Suponha que a matriz de LED seja um gráfico com coordenadas (x,y), qual é o tipo de função apresentada? 
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

pergunta = Question()
# =============================  CLASSE PARA PERGUNTAS ==========================


# ===========================   ESCOLHA DAS ALTERNATIVAS =========================
def contagem(eixo_y):
    global cont_pergunta
    
    if eixo_y < 20000:
        cont_pergunta+=1
        if cont_pergunta>4:
            cont_pergunta=0
    elif eixo_y > 40000:
        cont_pergunta-=1
        if cont_pergunta<0:
            cont_pergunta=4
    return cont_pergunta  

def opcoes(alternativa_correta):
    escolha = True
    while escolha:
    # Ler valores analógicos de VRx e VRy
        vrx_value = adc_vrx.read_u16()
        vry_value = adc_vry.read_u16()
        b = contagem(vry_value)

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
# ===========================   ESCOLHA DAS ALTERNATIVAS =========================


# ============================== INTERFACE PRINCIPAL==============================
def mostrando_pergunta(question):
    if question==0:
        pergunta.pergunta01()
        time.sleep(10)
        opcoes(0)
    elif question==1:
        pergunta.pergunta02()
        time.sleep(10)
        opcoes(1)
    elif question==2:
        pergunta.pergunta03()
        time.sleep(10)
        opcoes(2)
    elif question==3:
        pergunta.pergunta04()
        time.sleep(10)
        opcoes(3)
    elif question==4:
        pergunta.pergunta05()
        time.sleep(10)
        opcoes(4)
def mensagem_menu():
        # Teste OLED
    oled.fill(0)  # Limpar display
    oled.text("PERGUNTA", 0, 0)
    oled.text("(A) Selecionar", 0, 20)
    oled.text("(B) Voltar", 0, 30)
    
def seleciona_pergunta(ordem_pergunta):
    mensagem_menu()
    for i in lista_pergunta:
        if i == ordem_pergunta:
            oled.text("Questao {}".format(ordem_pergunta+1), 0, 10)
            oled.show()
            if button_a.value() == 0:
                mostrando_pergunta(ordem_pergunta)

while True:
    # Ler valores analógicos de VRx e VRy
    vrx_value = adc_vrx.read_u16()
    vry_value = adc_vry.read_u16()
    
    num_pergunta = contagem(vry_value)
    seleciona_pergunta(num_pergunta)
    
    # Esperar um pouco antes da próxima leitura
    time.sleep(0.1)
# ============================== INTERFACE PRINCIPAL==============================
