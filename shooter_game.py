from pygame import *
from random import randint

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

font.init()
font2 = font.SysFont('Arial', 35)
font1 = font.SysFont('Arial', 70)
win = font1.render('YOU WIN!', True, (0,255,0))
lose = font1.render('YOU LOSE!', True, (255,0,0))
score = 0
lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15,20,15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,620)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill() 

display.set_caption("Shooter")
window = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

ship = Player('rocket.png', 5, 400, 80, 100, 7)

bullets = sprite.Group()
monsters = sprite.Group()
for i in range(5):
    monster = Enemy('ufo.png', randint(0,620), -40, 80,50, randint(1,3))
    monsters.add(monster)


finish = False

run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()



    if not finish:
        window.blit(background,(0,0))
        ship.reset()
        ship.update()
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()

        text_lose = font2.render('Пропущено: '+str(lost), True, (255,255,255))
        window.blit(text_lose, (10,50))
        text = font2.render("Счет: " + str(score), True, (255, 255, 255))
        window.blit(text, (10, 20))

        if sprite.spritecollide(ship, monsters, False)
            finish = True
            window.blit(lose, (200,200))
        if lost > 2:
            finish = True
            window.blit(lose, (200,200))
        if sprite.groupcollide(monsters, bullets, True, True):
            score += 1
            monster = Enemy('ufo.png', randint(0,620), -40, 80,50, randint(1,3))
            monsters.add(monster)
        if score > 9:
            finish = True
            window.blit(win, (200,200))


    display.update()
    time.delay(30)

