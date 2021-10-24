import pygame
import os
import random
import neat

ai_jogando = True
geracao = 0

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_METORO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'meteoro.png')))
IMAGEM_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'fundo.png')))
IMAGENS_BABY_YODA = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'baby1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'baby2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'baby3.png'))),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Baby_yoda:
    IMGS = IMAGENS_BABY_YODA
    # animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(this, x, y):
        this.x = x
        this.y = y
        this.angulo = 0
        this.velocidade = 0
        this.altura = this.y
        this.tempo = 0
        this.contagem_imagem = 0
        this.imagem = this.IMGS[0]

    def pular(this):
        this.velocidade = -10.5
        this.tempo = 0
        this.altura = this.y

    def mover(this):
        # calcular o deslocamento
        this.tempo += 1
        deslocamento = 1.5 * (this.tempo**2) + this.velocidade * this.tempo

        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        this.y += deslocamento

        # o angulo do baby_yoda
        if deslocamento < 0 or this.y < (this.altura + 50):
            if this.angulo < this.ROTACAO_MAXIMA:
                this.angulo = this.ROTACAO_MAXIMA
        else:
            if this.angulo > -90:
                this.angulo -= this.VELOCIDADE_ROTACAO

    def desenhar(this, tela):
        # definir qual imagem do baby_yoda vai usar
        this.contagem_imagem += 1

        if this.contagem_imagem < this.TEMPO_ANIMACAO:
            this.imagem = this.IMGS[0]
        elif this.contagem_imagem < this.TEMPO_ANIMACAO*2:
            this.imagem = this.IMGS[1]
        elif this.contagem_imagem < this.TEMPO_ANIMACAO*3:
            this.imagem = this.IMGS[2]
        elif this.contagem_imagem < this.TEMPO_ANIMACAO*4:
            this.imagem = this.IMGS[1]
        elif this.contagem_imagem >= this.TEMPO_ANIMACAO*4 + 1:
            this.imagem = this.IMGS[0]
            this.contagem_imagem = 0


        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(this.imagem, this.angulo)
        pos_centro_imagem = this.imagem.get_rect(topleft=(this.x, this.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(this):
        return pygame.mask.from_surface(this.imagem)







def desenhar_tela(tela, baby_yodas, metoros, base, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for baby_yoda in baby_yodas:
        baby_yoda.desenhar(tela)
    for metoro in metoros:
        metoro.desenhar(tela)



    if ai_jogando:
        texto = FONTE_PONTOS.render(f"Geração: {geracao}", 1, (255, 255, 255))
        tela.blit(texto, (10, 10))

    base.desenhar(tela)
    pygame.display.update()






if __name__ == '__main__':
    caminho = os.path.dirname(__file__)
    caminho_config = os.path.join(caminho, 'config.txt')
    rodar(caminho_config)
