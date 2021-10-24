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


class Metoro:
    DISTANCIA = 190
    VELOCIDADE = 5

    def __init__(this, x):
        this.x = x
        this.altura = 0
        this.pos_topo = 0
        this.pos_base = 0
        this.METORO_TOPO = pygame.transform.flip(IMAGEM_METORO, False, True)
        this.METORO_BASE = IMAGEM_METORO
        this.passou = False
        this.definir_altura()

    def definir_altura(this):
        this.altura = random.randrange(50, 450)
        this.pos_topo = this.altura - this.METORO_TOPO.get_height()
        this.pos_base = this.altura + this.DISTANCIA

    def mover(this):
        this.x -= this.VELOCIDADE

    def desenhar(this, tela):
        tela.blit(this.METORO_TOPO, (this.x, this.pos_topo))
        tela.blit(this.METORO_BASE, (this.x, this.pos_base))

    def colidir(this, baby_yoda):
        baby_yoda_mask = baby_yoda.get_mask()
        topo_mask = pygame.mask.from_surface(this.METORO_TOPO)
        base_mask = pygame.mask.from_surface(this.METORO_BASE)

        distancia_topo = (this.x - baby_yoda.x, this.pos_topo - round(baby_yoda.y))
        distancia_base = (this.x - baby_yoda.x, this.pos_base - round(baby_yoda.y))

        topo_ponto = baby_yoda_mask.overlap(topo_mask, distancia_topo)
        base_ponto = baby_yoda_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False


class Base:
    VELOCIDADE = 0
    LARGURA = IMAGEM_BASE.get_width()
    IMAGEM = IMAGEM_BASE

    def __init__(this, y):
        this.y = y
        this.x1 = 0
        this.x2 = this.LARGURA

    def mover(this):
        this.x1 -= this.VELOCIDADE
        this.x2 -= this.VELOCIDADE

        if this.x1 + this.LARGURA < 0:
            this.x1 = this.x2 + this.LARGURA
        if this.x2 + this.LARGURA < 0:
            this.x2 = this.x1 + this.LARGURA

    def desenhar(this, tela):
        tela.blit(this.IMAGEM, (this.x1, this.y))
        tela.blit(this.IMAGEM, (this.x2, this.y))


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


def main(genomas, config): # fitness function

    pygame.mixer.init()
    pygame.mixer.music.load("./music/tema.mp3")
    pygame.mixer.music.play()


    global geracao
    geracao += 1

    if ai_jogando:
        redes = []
        lista_genomas = []
        baby_yodas = []
        for _, genoma in genomas:
            rede = neat.nn.FeedForwardNetwork.create(genoma, config)
            redes.append(rede)
            genoma.fitness = 0
            lista_genomas.append(genoma)
            baby_yodas.append(Baby_yoda(230, 350))
    else:
        baby_yodas = [Baby_yoda(230, 350)]
    base = Base(730)
    metoros = [Metoro(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)

        # interação com o usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if not ai_jogando:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        for baby_yoda in baby_yodas:
                            baby_yoda.pular()

        indice_metoro = 0
        if len(baby_yodas) > 0:
            if len(metoros) > 1 and baby_yodas[0].x > (metoros[0].x + metoros[0].METORO_TOPO.get_width()):
                indice_metoro = 1
        else:
            rodando = False
            break

        # mover as coisas
        for i, baby_yoda in enumerate(baby_yodas):
            baby_yoda.mover()
            # aumentar um pouquinho a fitness do baby_yoda
            lista_genomas[i].fitness += 0.1
            output = redes[i].activate((baby_yoda.y,
                                        abs(baby_yoda.y - metoros[indice_metoro].altura),
                                        abs(baby_yoda.y - metoros[indice_metoro].pos_base)))
            # -1 e 1 -> se o output for > 0.5 então o baby_yoda pula
            if output[0] > 0.5:
                baby_yoda.pular()
        base.mover()

        adicionar_metoro = False
        remover_metoros = []
        for metoro in metoros:
            for i, baby_yoda in enumerate(baby_yodas):
                if metoro.colidir(baby_yoda):
                    baby_yodas.pop(i)
                    if ai_jogando:
                        lista_genomas[i].fitness -= 1
                        lista_genomas.pop(i)
                        redes.pop(i)
                if not metoro.passou and baby_yoda.x > metoro.x:
                    metoro.passou = True
                    adicionar_metoro = True
            metoro.mover()
            if metoro.x + metoro.METORO_TOPO.get_width() < 0:
                remover_metoros.append(metoro)

        if adicionar_metoro:
            pontos += 1
            metoros.append(Metoro(600))
            for genoma in lista_genomas:
                genoma.fitness += 5
        for metoro in remover_metoros:
            metoros.remove(metoro)

        for i, baby_yoda in enumerate(baby_yodas):
            if (baby_yoda.y + baby_yoda.imagem.get_height()) > base.y or baby_yoda.y < 0:
                baby_yodas.pop(i)
                if ai_jogando:
                    lista_genomas.pop(i)
                    redes.pop(i)

        desenhar_tela(tela, baby_yodas, metoros, base, pontos)


def rodar(caminho_config):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                caminho_config)

    populacao = neat.Population(config)
    populacao.add_reporter(neat.StdOutReporter(True))
    populacao.add_reporter(neat.StatisticsReporter())

    if ai_jogando:
        populacao.run(main)
    else:
        main(None, None)


if __name__ == '__main__':
    caminho = os.path.dirname(__file__)
    caminho_config = os.path.join(caminho, 'config.txt')
    rodar(caminho_config)
