import pygame

pygame.init() #Inicializa o pygame

tamanho = (900, 500) #Cria uma tela com tamanho especificado

tela = pygame.display.set_mode(tamanho)
posicaoBola = pygame.Vector2(450, 250)
dt = 0
direcaoY = 1
direcaoX = 1

pygame.display.set_caption("Hello Games!") #Define o título da janela

relogio = pygame.time.Clock() #Define um relógio para controlar o FPS

while True: #Lida com os eventos da aplicação
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit() #Fecha o pygame

    tela.fill((40, 200, 100)) #Preenche a tela com uma cor

    #Desenha um círculo na tela
    pygame.draw.circle(tela, (255, 0, 0), posicaoBola, 50)

    posicaoBola.y += 150 * dt * direcaoY

    if posicaoBola.y >= 450 or posicaoBola.y <= 50:
        direcaoY *= -1
#    elif posicaoBola.y <= 50:
#        direcaoY = 1
    
    posicaoBola.x += 150 * dt * direcaoX

    if posicaoBola.x >= 850 or posicaoBola.x <= 50:
        direcaoX *= -1

    pygame.display.update() #Atualiza a tela
    dt = relogio.tick(60) / 1000 #Define a quantidade de FPS