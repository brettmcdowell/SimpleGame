from colour import Colour
import pygame

class Player:
    def __init__(self, x, y, size, colour=Colour.RED):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size))

    def detect_collision(self, other):
        if (other.x >= self.x and other.x < (self.x + self.size)) or (self.x >= other.x and self.x < (other.x + other.size)):
            if (other.y >= self.y and other.y < (self.y + self.size)) or (self.y >= other.y and self.y < (other.y + self.size )):
                return True
        return False

class Enemy(Player):
    img1 = pygame.image.load("/Users/brettmcdowell/Downloads/enemy.jpg")
    def __init__(self, x, y):
        super().__init__(x, y, size=50, colour=Colour.BLUE)

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.size,self.size)
        scaled_img1 = pygame.transform.scale(self.img1, rect.size)
        scaled_img1 = scaled_img1.convert()
        screen.blit(scaled_img1,rect)

class Large_Enemy(Player):
    img1 = pygame.image.load("/Users/brettmcdowell/Downloads/enemy.jpg")
    def __init__(self, x, y):
        super().__init__(x, y, size=70, colour=Colour.BLUE)

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.size,self.size)
        scaled_img1 = pygame.transform.scale(self.img1, rect.size)
        scaled_img1 = scaled_img1.convert()
        screen.blit(scaled_img1,rect)

class BossEnemy(Player):
    img1 = pygame.image.load("/Users/brettmcdowell/Downloads/enemy.jpg")
    def __init__(self, x, y):
        super().__init__(x, y, size=80, colour=Colour.BLUE)

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.size,self.size)
        scaled_img1 = pygame.transform.scale(self.img1, rect.size)
        scaled_img1 = scaled_img1.convert()
        screen.blit(scaled_img1,rect)

class Human_Player(Player):
    img2 = pygame.image.load("/Users/brettmcdowell/Downloads/MarioFinal.png")
    def __init__(self, x, y):
        super().__init__(x, y, size=90, colour=Colour.RED)

    def draw(self, screen):
        rect2 = pygame.Rect(self.x, self.y, self.size, self.size)
        scaled_img2 = pygame.transform.scale(self.img2, rect2.size)
        scaled_img2 = scaled_img2.convert()
        screen.blit(scaled_img2, rect2)
