import pygame
from random import randrange

class Ball:
    rect: pygame.Rect
    directionX: float = 0
    directionY: float = 0
    angle: float = 0
    width: int = 20
    height: int = 20
    speed: float = 10
    color: pygame.Color = pygame.Color(255, 255, 255)
    colliding: bool = False

    def __init__(self, ScreenWidth: int, ScreenHeight: int) -> None:
        posX: int = int(ScreenWidth / 2 - self.width / 2)
        posY: int = int(ScreenHeight / 2 - self.height / 2)
        self.rect = pygame.Rect(posX, posY, self.width, self.height)
        self.randomDir()

    def randomDir(self) -> None:
        self.directionX = randrange(-99, 99, 1) / 100
        self.directionY = randrange(-99, 99, 1) / 100

    def Reset(self, ScreenWidth: int, ScreenHeight: int) -> None:
        posX: int = int(ScreenWidth / 2 - self.width / 2)
        posY: int = int(ScreenHeight / 2 - self.height / 2)
        self.rect.left = posX 
        self.rect.top = posY
        self.randomDir()
        self.speed = 10

    def Draw(self, Screen) -> None:
        pygame.draw.rect(Screen, (255, 255, 255), self.rect)

    def Bounce(self, Bar: pygame.Rect):
# Partie V ↓
        self.directionX *= -1
        if (self.speed < 50):
            self.speed += 1
# Partie V ↑

    def Collision(self, Bar1: pygame.Rect, Bar2: pygame.Rect, ScreenHeight: int) -> None:
# Partie IV ↓
        if (self.rect.top <= 0 or self.rect.top + self.rect.height >= ScreenHeight):
            self.directionY *= -1
# Partie IV ↑

        if (Bar1.colliderect(self.rect)):
            if (self.colliding == False):
                self.Bounce(Bar1)
            self.colliding = True
        elif (Bar2.colliderect(self.rect)):
            if (self.colliding == False):
                self.Bounce(Bar2)
            self.colliding = True
        else:
            self.colliding = False

    def outOfBorder(self, ScreenWidth: int) -> int:
# Partie VI - 1 ↓
        if (self.rect.left + self.rect.width > ScreenWidth):
            return 1
        elif (self.rect.left < 0):
            return 2
        return 0
# Partie VI - 1 ↑

    def Move(self) -> None:
        self.rect.move_ip(self.directionX * self.speed, self.directionY * self.speed)