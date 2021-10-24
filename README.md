Temas:
 - Grafos1
 - Grafos2
 - PD
 - D&C
 - Greed
 - Final 
 

 
# Flappy-Baby-Yoda

**Conteúdo da Disciplina**: Final<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0142329  | Francisco Emanoel Ferreira da Penha |


## Sobre 
Essa última entrega foi baseada em um game bem famoso(que gosto de jogar quando estou de boas), o Flappy Bird, só que decidi fazer uma versão própria com personagens e diferentes e um trilha sonora que acho muito top. Para essa nova versão pegamos o tema star wars 😁, nesse contexto o principal objetivo é desviar dos meteoritos que se encontram no espaço, e nesse momento você está controlando a nave do baby yoda. Ok, nesse sentido como precisamos aplicar algumas estruturas que aprendemos da entregas passadas, iremos adicionar uma coisa a mais no nosso game, seria uma IA para jogar esse jogo, usando o conceito de rede neural( que por trás funciona como grafos com pesos, e de acordo com esses pesos decisões serão tomadas), para isso iremos usar um método bem famoso para esse tipo de aplicação que seria o método de  aprendizado de máquina denominado Redes Neurais em Evolução por meio de Topologias Aumentadas (NEAT). Simplificado, o NEAT descreve conceitos algorítmicos de máquinas de autoaprendizagem que são inspiradas pela modificação genética no processo de evolução, na prática um geração n é selecionada para fazer os primeiros testes, desses testes os genomas que conseguirem o melhor desempenhos serão reproduzido nas geração n+1, assim quantos maio o números de testes, maiores são a probabilidade de fazer uma geração “perfeita”. [Para um melhor entendimento do projeto foi criado uma page com mais informações.](https://projeto-de-algoritmos.github.io/Final-Flappy-Baby-Yoda/#/README)

## Screenshots

![](https://raw.githubusercontent.com/projeto-de-algoritmos/Final-Countdown/master/imgs/image1.png)


![](https://raw.githubusercontent.com/projeto-de-algoritmos/Final-Countdown/master/imgs/image2.png)

## Instalação 
**Linguagem**: Python3<br>

### Pré-requisitos
- SO: Linux (Ubuntu, Debian,...)
- [python3](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)
    - pygame
    
            sudo pip3 install pygame
    
    - neat

            sudo pip3 install neat-python


- [Makefile](https://zoomadmin.com/HowToInstall/UbuntuPackage/make)
    


## Uso 

**Para executar o software:**
 
``make start``
 
**Caso você não tenha o make instalado pode usar os seguintes comandos:**
 
``python3 ./src/baby-yoda-IA.py``

Depois que você execultar esse comando a IA vai começar a fazer os testes de seleção, até achar a melhor geração.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.




