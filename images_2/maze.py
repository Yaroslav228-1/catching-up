usikovfrom pygame import *



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, player_x, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 567:
            self.rect.y += self.speed

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < 1200:
            self.rect.x += self.speed


class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 600:
            self.direction = 'right'
        if self.rect.x >= 851:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        
class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

        
player = Player('son.png', 100, 200, 50, 60, 10)
enemy = Enemy('mom.png', 328, 859, 60, 70, 5)
final = GameSprite('treasure.png', 400, 859, 70, 70, 0)


wall_1 = Wall((252, 3, 3), 234, 416, 696, 5)

wall_2 = Wall((252, 3, 3), 234, 232, 150, 5)

wall_3 = Wall((252, 3, 3), 529, 138, 5, 177)

wall_4 = Wall((252, 3, 3), 380, 18, 5, 300)

wall_5 = Wall((252, 3, 3), 382, 19, 696, 5)

wall_6 = Wall((252, 3, 3), 532, 136, 430, 5)

wall_7 = Wall((252, 3, 3), 529, 313, 403, 5)

wall_8 = Wall((252, 3, 3), 930, 316, 5, 102)

wall_9 = Wall((252, 3, 3), 1077, 24, 5, 477)

wall_10 = Wall((252, 3, 3), 816, 505, 263, 5)

wall_11 = Wall((252, 3, 3), 959, 138, 5, 279)

wall_12 = Wall((252, 3, 3), 930, 418, 31, 5)

wall_13 = Wall((252, 3, 3), 819, 420, 5, 88)



win_width = 1250
win_height = 650

window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')


backgraund = transform.scale(image.load('background.jpg'), (win_width, win_height))


clock = time.Clock()


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (225, 215, 0))
loser = font.render('YOU LOSER!', True, (225, 215, 0))


finish = False


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                sys.exit()
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            print(f"Кордината x: {x}\nКордината y: {y}\n")
    if finish != True:
        window.blit(backgraund,(0, 0))
        


        player.reset()
        player.update()


        enemy.reset()
        enemy.update()


        final.reset()
        


        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        wall_9.draw_wall()
        wall_10.draw_wall()
        wall_11.draw_wall()
        wall_12.draw_wall()
        wall_13.draw_wall()
        




        if sprite.collide_rect(player, final):
            window.blit(win, (225, 215))
            finish = True
            money.play()


        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wall_4) or sprite.collide_rect(player, wall_5) or sprite.collide_rect(player, wall_6) or sprite.collide_rect(player, wall_7) or sprite.collide_rect(player, wall_8) or sprite.collide_rect(player, wall_9) or sprite.collide_rect(player, wall_10) or sprite.collide_rect(player, wall_11) or sprite.collide_rect(player, wall_12) or sprite.collide_rect(player, wall_13):
            window.blit(loser, (225, 215))
            finish = True
            kick.play()

        

    
    
    
    clock.tick(60)
    display.update()

