import pygame
import sys
# from scripts.karts import Kart
from random import randint


KART_POS = {'forward': [4,2],
            'forward_steer_right': [18, 2],
            'right': [34,4],
            'reverse_steer_right': [49, 2],
            'reverse': [68, 2],
            'reverse_steer_left': [82, 2],
            'left': [98, 4],
            'forward_steer_left': [113, 2],
            }


FPS = 60
WIDTH = 800
HEIGHT = 640
TILESIZE = 25

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Kart Sim")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.display = pygame.Surface((640,480))
        
        self.clock = pygame.time.Clock()


        self.img_pos = [160, 260]
        self.movement = [False, False]
        
        self.scroll = [0, 0] 

        self.sprite_sheet_image = pygame.image.load('mini_pixel/Cars/Player_blue.png')

        
        class Camera(object):
            def __init__(self, camera_func, width, height):
                self.camera_func = camera_func
                self.state = pygame.Rect(0, 0, width, height)
                
            def apply(self, target):
                return target.rect.move(self.state.topleft)
                
            def update(self, target):
                self.state = self.camera_func(self.state, target.rect)
            
            def simple_camera(camera, target_rect):
                l, t, _, _ = target_rect # l = left,  t = top
                _, _, w, h = camera      # w = width, h = height
                return pygame.Rect(-l+(WIDTH/2), -t+(HEIGHT/2), w, h)


        vel = 2
        x = 50
        y = 50
        p1_width = 14
        p1_height = 16

        class All_Objects:
            def __init__(self, path, width, height):
                self.image = pygame.image.load(path)
                self.width = width
                self.height = height

        class Maps(All_Objects):
            def __init__(self, path, width, height):
                super().__init__(path, width, height)
                self.backhground = pygame.image.load(path).convert()
                self.backhground = pygame.transform.scale(self.backhground, (self.width, self.height))
        
        self.map = Maps(f"maps/{randint(1,5)}.jpg", 898, 1324)
        

        class Kart(All_Objects):
            def __init__(self, path, width, height, scale, x, y, direction, vel):
                super().__init__(path, width, height )
                self.scale = scale 
                self.direction = direction
                self.vel = vel
                self.flip = True
                self.anim_offset = (-3, -3)
                self.x = x
                self.y = y

            def get_image(self):
                image= pygame.Surface((self.width, self.height))
                image.blit(self.image, (0,0), (KART_POS[self.direction][0], KART_POS[self.direction][1], self.width, self.height) )
                image = pygame.transform.scale(image, (self.width * self.scale, self.height * self.scale))
                image.set_colorkey((0,0,0))
                return image
                # trail.blit(, (0,0), self.width, self.height)

            def rect(self):
                return pygame.Rect(x, y, self.width, self.height)
            
        self.camera_x = 0
        self.camera_y = 0
            
        direction = 'forward'
        self.player = Kart('mini_pixel/Cars/Player_blue.png', p1_width, p1_height, 3, self.camera_x, self.camera_y, direction, vel)
        
        
    # def draw_grid(self):
    #     for i_x in range(0, WIDTH, TILESIZE):
    #         pygame.draw.line(self.display, 'black', (i_x, 0), (i_x, HEIGHT))
        
    #     for i_y in range(0, HEIGHT, TILESIZE):
    #         pygame.draw.line(self.display, 'white', (0,i_y), (WIDTH, i_y))
        

    def run(self):
        while True:
            
           
            # self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            # self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            # render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            # self.
            self.keys = pygame.key.get_pressed()

            
            if self.keys[pygame.K_RIGHT] and self.keys[pygame.K_UP]:
                self.player.direction = 'forward_steer_right'
                self.camera_x += self.player.vel - 1
                self.camera_y-= self.player.vel
                

            elif self.keys[pygame.K_LEFT] and self.keys[pygame.K_UP]:
                self.player.direction = 'forward_steer_left'
                self.camera_x -= self.player.vel - 1
                self.camera_y -= self.player.vel

            elif self.keys[pygame.K_RIGHT] and self.keys[pygame.K_DOWN]:
                self.player.direction = 'reverse_steer_right'
                self.camera_x += self.player.vel - 1
                self.camera_y += self.player.vel
            elif self.keys[pygame.K_LEFT] and self.keys[pygame.K_DOWN]:
                self.player.direction = 'reverse_steer_left'
                self.camera_x -= self.player.vel - 1
                self.camera_y += self.player.vel
            elif self.keys[pygame.K_RIGHT]:
                self.camera_x += self.player.vel
                self.player.direction = 'right'
            elif self.keys[pygame.K_LEFT]:
                self.camera_x -= self.player.vel
                self.player.direction = 'left'
            elif self.keys[pygame.K_UP]:
                self.camera_y -= self.player.vel
                self.player.direction = 'forward'
            elif self.keys[pygame.K_DOWN]:
                self.camera_y += self.player.vel
                self.player.direction = 'reverse'


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()

            # self.player.render(self.display, offset = render_scroll)


            self.display.blit(self.map.backhground, (0 - self.camera_x, 0 -self.camera_y))
            self.display.blit(self.player.get_image(), (self.display.get_width()/2, self.display.get_height()-self.player.height*4))
            # self.camera.update(self.map)

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.flip()
            
            self.clock.tick(FPS)




Game().run()