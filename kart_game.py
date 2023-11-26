import pygame
import sys
import random
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
        self.font = pygame.font.Font('PKMN_RBYGSC.ttf', 32)

        self.clock = pygame.time.Clock()


        self.img_pos = [160, 260]
        self.movement = [False, False]
        
        self.scroll = [0, 0] 

        vel = 2
        x = 50
        y = 50
        player_width = 14
        player_height = 16

        class All_Objects:
            def __init__(self, path: str, width: int, height: int):
                self.image = pygame.image.load(path)
                self.width = width
                self.height = height
                self.obstacles = []


        class Maps(All_Objects):
            def __init__(self, path: str, width: int, height: int, obs_count: int, obs_size: int):
                super().__init__(path, width, height)
                self.background = pygame.image.load(path)
                self.background = pygame.transform.scale(self.background, (self.width, self.height)) 
                # self.obstacles = []
                # self.obs_x = random.uniform((self.width/2)-(self.width/4)+ 10, (self.width/2)+(self.width/4)) -10
                # self.obs_y = random.randint(-self.height, self.height)
                # self.obs_size = obs_size

                
            #     for i in range(obs_count):
            #         self.obs = pygame.image.load(f"Assets/{random.randint(1,40)}.png").convert_alpha()
            #         self.obs = pygame.transform.scale(self.obs, (obs_size, obs_size))
            #         self.obs.set_colorkey((0,0,0))
            #         self.obs_rect = self.obs.get_rect()
            #         self.background.blit(self.obs, (self.obs_x, self.obs_y))
            #         self.obstacles.append(self.obs_rect)
            # def rect(self):
            #     return pygame.Rect(self.obs_x, self.obs_y, self.obs_size, self.obs_size)


        class Kart(All_Objects):
            def __init__(self, path: str, width: int, height: int, scale: int, x: int, y: int, direction: str, vel: float):
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

            def rect(self):
                return pygame.Rect(self.x, self.y, self.width, self.height)
        

        self.camera_x = 0
        self.camera_y = 0

        self.map = [Maps(f"maps/1.jpg", 898, 1324, 30, 50),Maps(f"maps/2.jpg", 898, 1324, 4, 50),Maps(f"maps/3.jpg", 898, 1324, 5, 50),Maps(f"maps/4.jpg", 898, 1324, 6, 50),Maps(f"maps/5.jpg", 898, 1324, 7, 50)]
        direction = 'forward'
        self.player = Kart('mini_pixel/Cars/Player_blue.png', player_width, player_height, 3, self.camera_x, self.camera_y, direction, vel)
        self.score = 0
        self.up_score = False
       

    def run(self):
        while True:
            # self.camera_rect = pygame.Rect(self.camera_x + self.map[0].width/2, self.camera_y+self.map[0].height/2, self.player.width, self.player.height)
            


            self.keys = pygame.key.get_pressed()
            
            if self.keys[pygame.K_RIGHT] and self.keys[pygame.K_UP]:
                self.player.direction = 'forward_steer_right'
                self.camera_x += self.player.vel - 1
                self.camera_y-= self.player.vel
                self.score += 1
            elif self.keys[pygame.K_LEFT] and self.keys[pygame.K_UP]:
                self.player.direction = 'forward_steer_left'
                self.camera_x -= self.player.vel - 1
                self.camera_y -= self.player.vel
                self.score += 1
            elif self.keys[pygame.K_RIGHT] and self.keys[pygame.K_DOWN]:
                self.player.direction = 'reverse_steer_right'
                self.camera_x += self.player.vel - 1
                self.camera_y += self.player.vel
                self.score -= 1
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
                self.score += 1
                self.player.vel += 0.005

            elif self.keys[pygame.K_DOWN]:
                self.camera_y += self.player.vel
                self.player.direction = 'reverse'
                self.score -= 1
            if self.camera_x < -74 or self.camera_x > 102:
                pygame.quit()
                sys.exit()
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
            
            # print(self.camera_rect, self.map[0].rect())
            
            self.display.blit(self.map[0].background, ((WIDTH-self.map[0].width)- self.camera_x, (HEIGHT-self.map[0].height) -self.camera_y))
            self.display.blit(self.map[0].background, ((WIDTH-self.map[1].width)- self.camera_x, (-HEIGHT-self.map[0].height) -self.camera_y-self.player.height))
            
            for i in range(1,5):
                if self.camera_y < (-680-1320*i+ self.player.height):
                    self.display.blit(self.map[0].background, ((WIDTH-self.map[1].width)- self.camera_x, (-HEIGHT-self.map[0].height*(i+1)) -self.camera_y-self.player.height))
            for i in range(5,13):
                if self.camera_y < (-680-1320*i+ self.player.height):
                    self.display.blit(self.map[1].background, ((WIDTH-self.map[1].width)- self.camera_x, (-HEIGHT-self.map[0].height*(i+1)) -self.camera_y-self.player.height))
                    # for obs in self.map[1].obs_rect:
                    #     if self.player.rect().colliderect(obs):
                    #         pygame.quit()
                    #         sys.exit()
            for i in range(13,22):
                if self.camera_y < (-680-1320*i+ self.player.height):
                    self.display.blit(self.map[2].background, ((WIDTH-self.map[1].width)- self.camera_x, (-HEIGHT-self.map[0].height*(i+1)) -self.camera_y-self.player.height))
                    # for obs in self.map[2].obs_rect:
                    #     if self.player.rect().colliderect(obs):
                    #         pygame.quit()
                    #         sys.exit()
            for i in range(22,35):
                if self.camera_y < (-680-1320*i+ self.player.height):
                    self.display.blit(self.map[3].background, ((WIDTH-self.map[1].width)- self.camera_x, (-HEIGHT-self.map[0].height*(i+1)) -self.camera_y-self.player.height))
                    # for obs in self.map[3].obs_rect:
                    #     if self.player.rect().colliderect(obs):
                    #         pygame.quit()
                    #         sys.exit()
            for i in range(35,51):
                if self.camera_y < (-680-1320*i+ self.player.height):
                    self.display.blit(self.map[4].background, ((WIDTH-self.map[1].width)- self.camera_x, (-HEIGHT-self.map[0].height*(i+1)) -self.camera_y-self.player.height))
                    # for obs in self.map[4].obs_rect:
                    #     if self.player.rect().colliderect(obs):
                    #         pygame.quit()
                    #         sys.exit()
            self.display.blit(self.player.get_image(), (self.display.get_width()/2, self.display.get_height()-self.player.height*4))
            self.display.blit(self.font.render(f'{self.score}', True, 'white') , (0,0))
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.flip()
            
            self.clock.tick(FPS)




Game().run()