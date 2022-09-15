import pygame

#Khởi tạo
pygame.init()
screen=pygame.display.set_mode((600, 300))
pygame.display.set_caption('No wifi Dino')
running=True

# Các biến
screen_color=(255, 255, 255)
Grey=(160, 160, 160)
background_x=0
background_y=0
dino_x=0
dino_y=230
tree_x=550
tree_y=230
tree=pygame.image.load('./assets/tree.png')
background=pygame.image.load('./assets/background.jpg')
dino=pygame.image.load('./assets/dinosaur.png')
clock=pygame.time.Clock()
jump=False

pausing=False

#Thay đổi x, y
change_x=4
change_y=5

dino_jump=pygame.mixer.Sound('assets/dino_jump.wav')
game_over_sound=pygame.mixer.Sound('assets/game_over.wav')

score=0
game_font=pygame.font.SysFont('san', 20)
game_font2=pygame.font.SysFont('san', 40)

while running:
    #60 fps
    clock.tick(60)

    screen.fill(screen_color)
    background1_rect=screen.blit(background, (background_x, background_y))
    background2_rect=screen.blit(background, (background_x+600, background_y))

    score_txt=game_font.render("Score: "+str(score),True, Grey)
    screen.blit(score_txt, (5, 5))

    if background_x+600<=0:
        background_x=0

#Di chuyển Cây
    tree_x-=change_x
    if tree_x<=-20:
        tree_x=550
        score+=1

#Khủng long nhảy
    if 230>=dino_y>=100:
        if jump==True:
            dino_y-=change_y
    else:
        jump=False
    if dino_y<230:
        if jump==False:
            dino_y+=change_y

#Vẽ khủng long
    dino_rect=screen.blit(dino, (dino_x, dino_y))
    tree_rect=screen.blit(tree, (tree_x, tree_y))

#Background di chuyển
    background_x-=change_x

#Game Over
    if dino_rect.colliderect(tree_rect):
        pygame.mixer.Sound.play(game_over_sound)
        pausing=True
        game_over=game_font2.render('GAME OVER', True, Grey)
        Play_again=game_font2.render('Press Space to play again!', True, Grey)
        screen.blit(game_over, (200, 150))
        screen.blit(Play_again, (130, 180))
        change_x=0
        change_y=0

#Các Sự kiện
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if dino_y==230:
                    pygame.mixer.Sound.play(dino_jump)
                    jump=True
                if pausing==True:
                    score=0
                    background_x=0
                    background_y=0
                    dino_x=0
                    dino_y=230
                    tree_x=550
                    tree_y=230
                    change_x=4
                    change_y=5
                    pausing=False
    
    pygame.display.flip()
pygame.quit()