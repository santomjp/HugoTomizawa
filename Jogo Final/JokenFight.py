import pygame
from random import randint

pygame.init()
relogio = pygame.time.Clock()
tamanhoTela = (1200, 720)
tela = pygame.display.set_mode(tamanhoTela)

pygame.display.set_caption("Jokenpo Fight")

dt = 0

tempoP1Acao = 0.0
tempoP2Acao = 0.0

duracaoAcao = 0.0

#Sprites do jogador 1 (Samurai)
spriteP1Idle = pygame.image.load("Sprites/Samurais/Samurai/Idle.png").convert_alpha()
spriteP1Run = pygame.image.load("Sprites/Samurais/Samurai/Run.png").convert_alpha()
spriteP1Attack = pygame.image.load("Sprites/Samurais/Samurai/Attack_2.png").convert_alpha()
spriteP1Hurt = pygame.image.load("Sprites/Samurais/Samurai/Hurt.png").convert_alpha()
spriteP1Dead = pygame.image.load("Sprites/Samurais/Samurai/Dead.png").convert_alpha()
spriteP1Def = pygame.image.load("Sprites/Samurais/Samurai/Protection.png").convert_alpha()

listP1FramesIdle = []
listP1FramesAttack = []
listP1FramesHurt = []
listP1FramesDead = []
listP1FramesDef = []

# Cria os frames do personagem 1 na lista de listFramesIdle
for i in range(6):
    # Pega um frame da folha de sprites na posição i * 0, 0 com tamanho 128x128
    frameP1 = spriteP1Idle.subsurface(i * 128, 0, 128, 128)
    # Redimensiona o frame para 2 vezes o tamanho original
    frameP1 = pygame.transform.scale2x(frameP1)
    # Adiciona o frame na lista de listFramesIdle
    listP1FramesIdle.append(frameP1)

for i in range (5):
    frameP1 = spriteP1Attack.subsurface(i * 128, 0, 128, 128)
    frameP1 = pygame.transform.scale2x(frameP1)
    listP1FramesAttack.append(frameP1)

for i in range (3):
    frameP1 = spriteP1Hurt.subsurface(i * 128, 0, 128, 128)
    frameP1 = pygame.transform.scale2x(frameP1)
    listP1FramesHurt.append(frameP1)

for i in range (6):
    frameP1 = spriteP1Dead.subsurface(i * 128, 0, 128, 128)
    frameP1 = pygame.transform.scale2x(frameP1)
    listP1FramesDead.append(frameP1)

for i in range (2):
    frameP1 = spriteP1Def.subsurface(i * 128, 0, 128, 128)
    frameP1 = pygame.transform.scale2x(frameP1)
    listP1FramesDef.append(frameP1)

indexP1FramesIdle = 0
tempoP1AnimacaoIdle = 0.0
velocidadeP1AnimacaoIdle = 5

indexP1FramesAttack = 0
tempoP1AnimacaoAttack = 0.0
velocidadeP1AnimacaoAttack = 7

indexP1FramesHurt = 0
tempoP1AnimacaoHurt = 0.0
velocidadeP1AnimacaoHurt = 4

indexP1FramesDead = 0
tempoP1AnimacaoDead = 0.0
velocidadeP1AnimacaoDead = 6

indexP1FramesDef = 0
tempoP1AnimacaoDef = 0.0
VelocidadeP1AnimacaoDef = 2


# Retangulo do personagem na tela para melhor controle e posicionamento do personagem
personagem1Rect = listP1FramesIdle[0].get_rect(midbottom=(540, 680))
personagem1ColisaoRect = pygame.Rect(personagem1Rect.x, personagem1Rect.y, 80, 120)

direcaoPersonagem1 = 1 # Direção que o personagem está olhando (1 = Direita, -1 = Esquerda)

#Sprites do jogador 2 (Yokai)
spriteP2Idle = pygame.image.load("Sprites/Yokais/Yamabushi_tengu/Idle_2.png").convert_alpha()
spriteP2Run = pygame.image.load("Sprites/Yokais/Yamabushi_tengu/Run.png").convert_alpha()
spriteP2Attack = pygame.image.load("Sprites/Yokais/Yamabushi_tengu/Attack_2.png").convert_alpha()
spriteP2Hurt = pygame.image.load("Sprites/Yokais/Yamabushi_tengu/Hurt.png").convert_alpha()
spriteP2Dead = pygame.image.load("Sprites/Yokais/Yamabushi_tengu/Dead.png").convert_alpha()

listP2FramesIdle = []
listP2FramesAttack = []
listP2FramesHurt = []
listP2FramesDead = []

# Cria os frames do personagem 2 na lista de listFramesIdle
for i in range(5):
    # Pega um frame da folha de sprites na posição i * 0, 0 com tamanho 128x128
    frameP2 = spriteP2Idle.subsurface(i * 128, 0, 128, 128)
    # Redimensiona o frame para 2 vezes o tamanho original
    frameP2 = pygame.transform.scale(frameP2, (256, 256))
    frameP2 = pygame.transform.flip((frameP2), True, False)
    # Adiciona o frame na lista de listFramesIdle
    listP2FramesIdle.append(frameP2)

for i in range(6):
    frameP2 = spriteP2Attack.subsurface(i * 128, 0, 128, 128)
    frameP2 = pygame.transform.scale(frameP2, (256, 256))
    frameP2 = pygame.transform.flip((frameP2), True, False)
    listP2FramesAttack.append(frameP2)

for i in range(3):
    frameP2 = spriteP2Hurt.subsurface(i * 128, 0, 128, 128)
    frameP2 = pygame.transform.scale(frameP2, (256, 256))
    frameP2 = pygame.transform.flip((frameP2), True, False)
    listP2FramesHurt.append(frameP2)

for i in range(6):
    frameP2 = spriteP2Dead.subsurface(i * 128, 0, 128, 128)
    frameP2 = pygame.transform.scale(frameP2, (256, 256))
    frameP2 = pygame.transform.flip((frameP2), True, False)
    listP2FramesDead.append(frameP2)

indexP2FramesIdle = 0
tempoP2AnimacaoIdle = 0.0
velocidadeP2AnimacaoIdle = 3

indexP2FramesAttack = 0
tempoP2AnimacaoAttack = 0.0
velocidadeP2AnimacaoAttack = 5

indexP2FramesHurt = 0
tempoP2AnimacaoHurt = 0.0
velocidadeP2AnimacaoHurt = 4

indexP2FramesDead = 0
tempoP2AnimacaoDead = 0.0
velocidadeP2AnimacaoDead = 5

# Retangulo do personagem na tela para melhor controle e posicionamento do personagem
personagem2Rect = listP2FramesIdle[0].get_rect(midbottom=(660, 680))
personagem2ColisaoRect = pygame.Rect(personagem2Rect.x, personagem2Rect.y, 80, 120)

direcaoPersonagem1 = 1 # Direção que o personagem está olhando (1 = Direita, -1 = Esquerda)

#Sprite pedra (escudo), papel (magia) ou tesoura (espada)
spritePedra = pygame.image.load("Sprites/Icones/PNG/Icon16.png").convert_alpha()
spritePedra = pygame.transform.scale(spritePedra, (80, 80))

spritePapel = pygame.image.load("Sprites/Icones/PNG/Icon13.png").convert_alpha()
spritePapel = pygame.transform.scale(spritePapel, (80, 80))

spriteTesoura = pygame.image.load("Sprites/Icones/PNG/Icon23.png").convert_alpha()
spriteTesoura = pygame.transform.scale(spriteTesoura, (80, 80))

#Sprites do background
listBgSprites = [pygame.image.load("Sprites/BackgroundMontanhas/PNG/background_2/background2.png").convert_alpha()]

for i in range(len(listBgSprites)):
    listBgSprites[i] = pygame.transform.scale(listBgSprites[i], tamanhoTela)

vidaP1 = 5
vidaP2 = 5
gameOver = False

teclaP1 = 0
teclaP2 = 1

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for i in range(len(listBgSprites)): #Background
        tela.blit(listBgSprites[i], (0, 0))

    listTeclas = pygame.key.get_pressed()

    dt = relogio.tick(60) / 1000

    if teclaP1 != 0:
        tempoP1Acao += dt

    if teclaP2 != 1:
        tempoP2Acao += dt

    if tempoP1Acao >= duracaoAcao:
        teclaP1 = 0
        tempoP1Acao = 0.0

    if tempoP2Acao >= duracaoAcao:
        teclaP2 = 1
        tempoP2Acao = 0.0

    tempoP1AnimacaoIdle += dt

    if tempoP1AnimacaoIdle >= 1 / velocidadeP1AnimacaoIdle:
        indexP1FramesIdle = (indexP1FramesIdle + 1) % len(listP1FramesIdle)
        tempoP1AnimacaoIdle = 0.0

    tempoP1AnimacaoAttack += dt

    if tempoP1AnimacaoAttack >= 1 / velocidadeP1AnimacaoAttack:
        indexP1FramesAttack = (indexP1FramesAttack + 1) % len(listP1FramesAttack)
        tempoP1AnimacaoAttack = 0.0

    tempoP1AnimacaoHurt += dt

    if tempoP1AnimacaoHurt >= 1 / velocidadeP1AnimacaoHurt:
        indexP1FramesHurt = (indexP1FramesHurt + 1) % len(listP1FramesHurt)
        tempoP1AnimacaoHurt = 0.0

    tempoP1AnimacaoDead += dt

    if tempoP1AnimacaoDead >= 1 / velocidadeP1AnimacaoDead:
        indexP1FramesDead = (indexP1FramesDead + 1) % len(listP1FramesDead)
        tempoP1AnimacaoDead = 0.0
    
    tempoP2AnimacaoIdle += dt

    if tempoP2AnimacaoIdle >= 1 / velocidadeP2AnimacaoIdle:
        indexP2FramesIdle = (indexP2FramesIdle + 1) % len(listP2FramesIdle)
        tempoP2AnimacaoIdle = 0.0

    tempoP2AnimacaoAttack += dt

    if tempoP2AnimacaoAttack >= 1 / velocidadeP2AnimacaoAttack:
        indexP2FramesAttack = (indexP2FramesAttack + 1) % len(listP2FramesAttack)
        tempoP2AnimacaoAttack = 0.0

    tempoP2AnimacaoHurt += dt

    if tempoP2AnimacaoHurt >= 1 / velocidadeP2AnimacaoHurt:
        indexP2FramesHurt = (indexP2FramesHurt + 1) % len(listP2FramesHurt)
        tempoP2AnimacaoHurt = 0.0

    tempoP2AnimacaoDead += dt

    if tempoP2AnimacaoDead >= 1 / velocidadeP2AnimacaoDead:
        indexP2FramesDead = (indexP2FramesDead + 1) % len(listP2FramesDead)
        tempoP2AnimacaoDead = 0.0

    if not gameOver:
        if listTeclas[pygame.K_a]:
           teclaP1 = 100
        
        if listTeclas[pygame.K_s]:
           teclaP1 = 200

        if listTeclas[pygame.K_d]:
            teclaP1 = 300

        if listTeclas[pygame.K_KP1]:
            teclaP2 = 100

        if listTeclas[pygame.K_KP2]:
            teclaP2 = 200

        if listTeclas[pygame.K_KP3]:
            teclaP2 = 300

    if teclaP1 == 0 and teclaP2 == 1:
        frameP1 = listP1FramesDef[indexP1FramesDef]
        frameP2 = listP2FramesIdle[indexP2FramesIdle]

    if teclaP1 == teclaP2:
        frameP1 = listP1FramesDef[indexP1FramesDef]
        frameP2 = listP2FramesHurt[indexP2FramesHurt]

    if teclaP1 == 100 and teclaP2 == 200:
        frameP1 = listP1FramesDef[indexP1FramesDef]
        frameP2 = listP2FramesAttack[indexP2FramesAttack]

    if teclaP1 == 100 and teclaP2 == 300:
        frameP1 = listP1FramesAttack[indexP1FramesAttack]
        frameP2 = listP2FramesHurt[indexP2FramesHurt]

    if teclaP1 == 200 and teclaP2 == 100:
        frameP1 = listP1FramesAttack[indexP1FramesAttack]
        frameP2 = listP2FramesHurt[indexP2FramesHurt]

    if teclaP1 == 200 and teclaP2 == 300:
        frameP1 = listP1FramesDef[indexP1FramesDef]
        frameP2 = listP2FramesAttack[indexP2FramesAttack]

    if teclaP1 == 300 and teclaP2 == 100:
        frameP1 = listP1FramesDef[indexP1FramesDef]
        frameP2 = listP2FramesAttack[indexP2FramesAttack]

    if teclaP1 == 300 and teclaP2 == 200:
        frameP1 = listP1FramesAttack[indexP1FramesAttack]
        frameP2 = listP2FramesHurt[indexP2FramesHurt]

    if teclaP1 == 100:
        tela.blit(spritePedra, (420, 300))

    if teclaP1 == 200:
        tela.blit(spritePapel, (420, 300))

    if teclaP1 == 300:
        tela.blit(spriteTesoura, (420, 300))

    if teclaP2 == 100:
        tela.blit(spritePedra, (720, 300))

    if teclaP2 == 200:
        tela.blit(spritePapel, (720, 300))

    if teclaP2 == 300:
        tela.blit(spriteTesoura, (720, 300))

    tela.blit(frameP1, personagem1Rect)
    tela.blit(frameP2, personagem2Rect)


#    print(teclaP1)
#    print(teclaP2)
#    pygame.draw.rect(tela, (255, 0, 0), personagem1ColisaoRect, 2)
#    pygame.draw.rect(tela, (255, 0, 0), personagem2ColisaoRect, 2)
#    pygame.draw.rect(tela, (0, 0, 255), personagem1Rect, 2)
#    pygame.draw.rect(tela, (0, 0, 255), personagem2Rect, 2)

    pygame.display.update()