import pygame
import sys
# from scripts.karts import Kart


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


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Kart Sim")
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320,240))
        
        self.clock = pygame.time.Clock()


        self.img_pos = [160, 260]
        self.movement = [False, False]
        
        self.scroll = [0, 0] 

        self.sprite_sheet_image = pygame.image.load('mini_pixel/Cars/Player_blue.png')
        # def get_image(sheet, width, height, scale, state):
        #     image = pygame.Surface((width, height))
        #     image.blit(sheet, (0,0), (KART_POS[state][0], KART_POS[state][1], width, height) )
        #     image = pygame.transform.scale(image, (width * scale, height * scale))
        #     image.set_colorkey((0,0,0))
        #     return image
        
        # self.kart = get_image(self.sprite_sheet_image, 14, 19, 3, 'reverse')
        




        class Kart:
            def __init__(self, path, width, height, scale, state):
                
                self.sheet = pygame.image.load(path)
                self.width = width
                self.height = height
                self.scale = scale 
                self.state = state

            def get_image(self):
                image = pygame.Surface((self.width, self.height))
                image.blit(self.sheet, (0,0), (KART_POS[self.state][0], KART_POS[self.state][1], self.width, self.height) )
                image = pygame.transform.scale(image, (self.width * self.scale, self.height * self.scale))
                image.set_colorkey((0,0,0))
                return image
            
            
            
       
        state = 'forward'
        self.player = Kart('mini_pixel/Cars/Player_blue.png', 14, 19, 3, state)
        # self.player = self.player.get_image()
        
                
                
        
        

    def run(self):
        while True:
            self.display.fill('white')
            self.display.blit(self.player.get_image(), (0,0))
            self.display.blit(self.sprite_sheet_image, (0, 50))
            
            # self.display(self.kart.get_sprite(-4, -2, 14, 14), (0,0))
            # self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            # self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            # render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            # self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            # self.player.render(self.display, offset = render_scroll)

            self.keys = pygame.key.get_pressed()
            if pygame.key.get_pressed():
                if self.keys[pygame.QUIT]:
                    pygame.quit()
                    sys.exit()
                if self.keys[pygame.K_UP] and self.keys[pygame.K_RIGHT]:
                    self.player.state = 'forward_steer_right'
                    
                if self.keys[pygame.K_UP] and self.keys[pygame.K_LEFT]:
                    self.player.state = 'forward_steer_left'
                if self.keys[pygame.K_UP]:
                    self.player.state = 'forward'
                if self.keys[pygame.K_DOWN] and self.keys[pygame.K_RIGHT]:
                    self.player.state = 'reverse_steer_right'
                if self.keys[pygame.K_DOWN] and self.keys[pygame.K_LEFT]:
                    self.player.state = 'reverse_steer_left'
                if self.keys[pygame.K_UP]:
                    self.player.state = 'forward'
                pygame.event.pump()
                pygame.event.clear()

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_UP:
            #             if event.key == pygame.K_LEFT:
            #                 self.player.state = 'forward_steer_left'
            #             if event.key == pygame.K_RIGHT:
            #                 self.player.state = 'forward_steer_right'
            #             else:
            #                 self.player.state = 'forward'
            #         if event.key == pygame.K_LEFT:
            #             self.player.state = 'left'
            #             # self.movement[0] = True
            #         if event.key == pygame.K_LEFT and event.key == pygame.K_UP:
            #             self.player.state = 'forward_steer_left'
            #             # self.movement[0] = True
            #         if event.key == pygame.K_RIGHT and event.key == pygame.K_UP:
            #             self.player.state = 'forward_steer_right'
            #             # self.movement[1] = True
            #         if event.key == pygame.K_RIGHT:
            #             self.player.state = 'right'
            #             # self.movement[1] = True
            #         if event.key == pygame.K_UP:
            #             self.player.state = 'forward'
            #             # self.player.velocity[1] = -3
            #         if event.key == pygame.K_DOWN:
            #             self.player.state = 'reverse'
            #         if event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
            #             self.player.state = 'reverse_steer_right'
            #         if event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
            #             self.player.state = 'reverse_steer_left'
            #             # self.player.velocity[1] = -3
            #     if event.type == pygame.KEYUP:
            #         if event.key == pygame.K_LEFT:
            #             self.player.state = 'left'
            #             # self.movement[0] = True
            #         if event.key == pygame.K_LEFT and event.key == pygame.K_UP:
            #             self.player.state = 'forward_steer_left'
            #             # self.movement[0] = True
            #         if event.key == (pygame.K_RIGHT and pygame.K_UP):
            #             self.player.state = 'forward_steer_right'
            #             # self.movement[1] = True
            #         if event.key == pygame.K_RIGHT:
            #             self.player.state = 'right'
            #             # self.movement[1] = True
            #         if event.key == pygame.K_UP:
            #             self.player.state = 'forward'
            #             # self.player.velocity[1] = -3
            #         if event.key == pygame.K_DOWN:
            #             self.player.state = 'reverse'
            #         if event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
            #             self.player.state = 'reverse_steer_right'
            #         if event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
            #             self.player.state = 'reverse_steer_left'
            #             # self.player.velocity[1] = -3

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            
            pygame.display.flip()
            self.clock.tick(FPS)




Game().run()