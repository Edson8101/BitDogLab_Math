# BitDogLab_Math

BitDogLab_Math é um jogo de perguntas e respostas sobre matemática para a placa [BitDogLab](https://github.com/BitDogLab/BitDogLab). O jogo foi desenvolvido como projeto 1 da disciplina da FEEC/Unicamp IE323 - Sistemas Embarcados para ensino com abordagem STEM
<details>
  <summary>Clique para saber mais sobre a disciplina.</summary>
  Sistemas Embarcados para ensino com abordagem STEM é uma disciplina da pós-graduação da FEEC-UNICAMP ofertada pelo professor Fabiano Fruett. O objetivo da matéria é desenvolver projetos que envolva IoT, eletrônica e IA com o intuito de levar ferramentas para os alunos do ensino fundamental e médio utilizando a abordagem STEM (Science, Technology, Engineering and Mathematics). [BitDogLab](https://cpg.fee.unicamp.br/lista/caderno_horario_show.php?id=1932).
</details>
O objetivo do projeto 1 da disciplina é familiarizar-se com a placa e ganhar autonomia para desenvolver o primeiro programa.<br><br>

## Manual de Instruções

Esta primeira versão do BitDogLab_Math contém 5 perguntas com 5 alternativas cada. Primeiramente são exibidas animações quando o software iniciado. Em seguida seleciona-se a questão pode meio do joystick analógico com movimentos esquerda/direita, a questão é exibida no display Oled. Pressiona-se a tecla A para confirmar a escolha e então o gráfico da questão é exibido na matriz de LEDs por um tempo. Quando a contagem regressina no display Oled acaba, passa-se à seleção de alterativas para resposta. Então, com movimentos esquerda/direita no joystick a matriz de LEDs exibe as letras A até E correspondentes às alternativas, e simultaneamente o display Oled exibe o texto da resposta. O usuário confirma a seleção pressionando o botão A. Finalmente são exibidas na matrix de LEDs imagens :) ou :( dependendo se a resposta foi correta ou errada. Após isso o programa volta para a seleção de perguntas e o processo se repete indefinidamente. Para encerrar, deve-se pressionar 2 vezes o botão próximo à bateria na parte traseira da BitDogLab.<br><br>
O fluxograma abaixo ilustra o funcionamento do programa:

[<img src="./fluxograma.png" alt="Description of the image" width="500"/>](https://github.com/Edson8101/BitDogLab_Math/issues/1#issue-2500995584)

## Itens da BNCC contemplados

A Base Nacional Comum Curricular (BNCC) é um documento criado pelo Ministério da Educação (MEC) que estabelece as diretrizes e conteúdos essenciais que devem ser abordados nas escolas brasileiras, desde a educação infantil até o ensino médio. A criação da BNCC remonta à Constituição de 1988 que prevê em seu artigo 210 a Base Nacional Comum Curricular. Ao longo dos anos essa necessidade vem sendo discutida e amadurecida, e em 2015 foi publicada a primeira versão da BNCC. Mais recentemente, em 14 de dezembro de 2018, foi homologada pela ministra da educação Rossiele Soares a versão atual da BNCC, documento de 470 páginas que pode ser baixado em http://basenacionalcomum.mec.gov.br/ (BNCC - Histórico, 2024). O presente projeto visa contemplar os seguintes itens abordados na BNCC:

1. (EM13MAT301) Resolver e elaborar problemas do cotidiano, da Matemática e de outras áreas do conhecimento, que envolvem equações lineares simultâneas, usando técnicas algébricas e gráficas, com ou sem apoio de tecnologias digitais.
2. (EM13MAT302) Construir modelos empregando as funções polinomiais de 1º ou 2º graus, para resolver problemas em contextos diversos, com ou sem apoio de tecnologias digitais.
3. (EM13MAT309) Resolver e elaborar problemas que envolvem o cálculo de áreas totais e de volumes de prismas, pirâmides e corpos redondos em situações reais (como o cálculo do gasto de material para revestimento ou pinturas de objetos cujos formatos sejam composições dos sólidos estudados), com ou sem apoio de tecnologias digitais.
4. (EM13MAT405) Utilizar conceitos iniciais de uma linguagem de programação na implementação de algoritmos escritos em linguagem corrente e/ou matemática.

Em 17 de fevereiro de 2022, o parecer CNE/CEB nº 2/2022 estabeleceu as normas sobre Computação na Educação Básica como um complemento à BNCC. Posteriormente, a Resolução CNE/CEB nº 1/2022, de 4 de outubro de 2022, reforçou essas normas, definindo os conteúdos e habilidades relacionados à Educação Digital que devem ser abordados nas escolas, o documento de 75 páginas ficou conhecido como BNCC Computação, que pode ser baixada em http://basenacionalcomum.mec.gov.br/historico (BNCC Histórico, 2024) (COUTINHO, 2024). O presente projeto relaciona-se à BNCC Computação, especificamente às habilidade do 8º e 9º anos do Ensino Fundamental, e ao Ensino Médio nos seguintes itens:

* A criação do jogo e sua programação em MicroPython estimulam habilidades essenciais de Pensamento Computacional, como:
  
5. (EF08CO02): Criar soluções de problemas para os quais seja adequado o uso de listas para descrever suas informações e automatizá-las usando uma linguagem de programação, empregando ou não a recursão como uma técnica de resolver o problema.
(EF09CO01): Criar soluções de problemas para os quais seja adequado o uso de árvores e grafos para descrever suas informações e automatizá-las usando uma linguagem de programação.
6. (EF69CO02): Descrever a estrutura de um algoritmo e traduzi-lo para uma linguagem de programação.
  
* A lógica do jogo, com perguntas aleatórias, exige a aplicação de algoritmos, seleção condicional e repetições, conectando-se com as habilidades:
  
7. (EM13CO01): Explorar e construir a solução de problemas por meio da reutilização de partes de soluções existentes.
8. (EM13CO02): Explorar e construir a solução de problemas por meio de refinamentos, utilizando diversos níveis de abstração desde a especificação até a implementação.
  
* O desenvolvimento do jogo e a interação com a plataforma BitDogLab abrem espaço para discutir:

9. (EM13CO20): Criar conteúdos, disponibilizando-os em ambientes virtuais para publicação e compartilhamento, avaliando a confiabilidade e as consequências da disseminação dessas informações.
  
* A utilização de um sistema de quiz, com feedback imediato, incentiva a autonomia e o aprendizado de:
10. (EM13CO15): Analisar a interação entre usuários e artefatos computacionais, abordando aspectos da experiência do usuário e promovendo reflexão sobre a qualidade do uso dos artefatos nas esferas do trabalho, do lazer e do estudo.


## Hardware 

O projeto está autocontido na placa denominada BitDogLab. A BitDogLab é uma placa de desenvolvimento de código aberto com uma variedade de sensores e atuadores embutidos, facilitando a criação de projetos em sistemas embarcados. Ela é baseada no microcontrolador Raspberry Pi Pico. A placa pode ser vista na figura abaixo. 

<img src="![bitdoglab_plac](https://github.com/user-attachments/assets/756dcdd5-7c66-4085-9bf0-4e50287c2c9f)" alt="Description of the image" width="500"/>

1. **Microcontrolador: RaspBerry Pi Pico**

O Raspberry Pi Pico é o cérebro do projeto, responsável por controlar os demais componentes e executar o código do jogo. Ele é programado em MicroPython e se comunica com todos os periféricos embarcados na BitDogLab.

2. **Joystick**

O joystick é utilizado para navegação entre as questões e as alternativas do quiz. Sua função principal é permitir que o jogador possa pular para a próxima questão ou alternativa.

3. **Matriz de LEDs 5x5**

A matriz de LEDs 5x5 é usada para exibir desenhos simples relacionados às perguntas do quiz. Esses desenhos podem servir como ilustrações ou dicas visuais para as perguntas.

4. **Display OLED**

O display OLED é utilizado para apresentar as perguntas e alternativas textualmente. Ele exibe o conteúdo principal do jogo, como as perguntas e as opções de respostas.

5. **Botões A e B**

Os botões A e B são usados como controles para confirmar a seleção de uma alternativa e para voltar a uma questão anterior ou desfazer uma escolha.

6. **Buzzer** 

O buzzer é utilizado para gerar o som de animação da interface de apresentação.

## Software 

Descrever aqui o software

## Desafios 

## Como instalar?

1. Instale a IDE Thonny a partir de [https://thonny.org/](https://thonny.org/).
2. Conecte a placa BitDogLab ao computador através de um cabo micro-USB.
3. Siga as instruções em [Introdução prática a BitDogLab](https://escola-4-ponto-zero.notion.site/Cap-tulo-02-Usando-o-IDE-Thonny-para-desenvolvimento-d5dce52947244cd6a64da4ba77831c7a) para certificar-se que a BitDogLab está sendo reconhecida no Thonny.
4. Baixe o código `projeto01.py` neste repositório.
5. No Thonny, acesse `Arquivo > Abrir` e localize o arquivo `projeto01.py` (por exemplo, na pasta Downloads).
6. Pressione o botão "play" (triângulo verde) para executar o programa na BitDogLab temporariamente.
7. Se a execução estiver correta e você quiser salvar o código na BitDogLab para executá-lo posteriormente, então:
8. se você desejar preservar o programa atual de sua BitDogLab, antes de prosseguir, salve o arquivo main.py existente em uma pasta de seu computador.
9. Agora, com a guia que contém `projeto01.py` ativa no Thonny vá em `Arquivo > Salvar como`.
10. Quando a caixa de seleção aparecer com "Raspberry Pi e Computador", selecione Raspberry Pi, clique sobre `main.py` para sobrescrever.
11. Pronto, você pode desconectar a BitDogLab e o programa pode ser executado (ou reiniciado) apertando o botão próximo à bateria.

## Referências
