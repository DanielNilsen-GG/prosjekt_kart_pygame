import pygame

class Tile:  # klasse for alle tiles
    def __init__(self, area):
        self.img = pygame.image.load(area).convert_alpha()
        self.rect = self.img.get_rect()
    
    def draw(self, surface):
        surface.blit(self.img, self.rect)
        
        


class Offgrid(Tile): # ikke mulig å kjøre her
    def __init__(self, area):
        super().__init__(area)
    
    
        


class Ongrid(Tile): # mulig å kjøre her
    def __init__(self, area):
        super().__init__(area)

