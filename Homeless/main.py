import pygame

pygame.init()
relogio = pygame.time.Clock()

tamanho = (1200, 500)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homeless Walker")
dt = 0

#Carrega a spritesheet para o programa
folhaSpritesIdle = pygame.image.load("Assets/Homeless_1/Idle.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("Assets/Homeless_1/Walk.png").convert_alpha()

#Define os frames
framesIdle = []
framesWalk = []

for i in range(6):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesIdle.append(frame)

for i in range (8):
    frame = folhaSpritesWalk.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesWalk.append(frame)
    
#Variáveis da animação do personagem parado
indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 10

indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

#Retangulo do personagem
personagemRect = framesIdle[0].get_rect(midbottom=(100, 480))
personagemRectWalk = framesWalk[0].get_rect(midbottom=(100, 480))

gravidade = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))


    #Atualiza a animação do personagem parado
    tempoAnimacaoIdle += dt
    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        indexFrameIdle = (indexFrameIdle + 1) % len(framesIdle)
        tempoAnimacaoIdle = 0.0

    tempoAnimacaoWalk += dt
    if tempoAnimacaoWalk >=1 / velocidadeAnimacaoWalk:
        indexFrameWalk = (indexFrameWalk + 1) % len(framesWalk)
        tempoAnimacaoWalk = 0.0

    #Movimenta o personagem no eixo X
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        personagemRect.x -= 100 * dt
    if teclas[pygame.K_RIGHT]:
        personagemRect.x += 100 * dt
    if teclas[pygame.K_SPACE]:
        if personagemRect.centery == 352:
            gravidade = -30
            
    #Gravidade aumenta
    gravidade += 3

    personagemRect.y += gravidade

    if personagemRect.centery >= 352:
        personagemRect.centery = 352

    #Desenha o personagem andando
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_LEFT] == True:
        tela.blit(framesWalk[indexFrameWalk], personagemRectWalk)
    else:
        tela.blit(framesIdle[indexFrameIdle], personagemRect)


    #Desenha um retangulo em volta do personagem
    #pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)

    pygame.display.update()
    dt = relogio.tick(60) / 1000