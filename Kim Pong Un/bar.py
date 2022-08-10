import pygame

class Bar():
     
    #sprite: pygame.image = pygame.image.load('ha.gif')
    rect: pygame.Rect
    speed: int = 10
    width: int = 20
    height: int = 100
    color: pygame.Color = pygame.Color(255, 255, 255)

    def __init__(self, ScreenWidth: int, ScreenHeight: int, position: str) -> None:
        posX: int = 0
        posY: int = int(ScreenHeight / 2 - self.height / 2)

        if (position == "right"):
            posX = int(ScreenWidth / 10)
        elif (position == "left"):
            posX = int(ScreenWidth - ScreenWidth / 10 - self.width)
        self.rect = pygame.Rect(posX, posY, self.width, self.height)

    def Draw(self, Screen) -> None:
        pygame.draw.rect(Screen, self.color, self.rect)

    def moveUp(self) -> None:
        self.rect.move_ip(0, -self.speed)
    
    def moveDown(self) -> None:
        self.rect.move_ip(0, self.speed)