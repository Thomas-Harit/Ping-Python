import pygame
from bar import Bar
from ball import Ball

class Game:
    Launched: bool = True
    Screen: pygame.surface.Surface
    Score1: int
    Score2: int
    ScreenWidth: int
    ScreenHeight: int
    filetWidth: int
    filetHeight: int
    Bar1: Bar = Bar(ScreenWidth, ScreenHeight, "right")
    Bar2: Bar = Bar(ScreenWidth, ScreenHeight, "left")
    ball: Ball = Ball(ScreenWidth, ScreenHeight)
    Font: pygame.font.Font

    def __init__(self) -> None:
        pygame.init()
        self.Font = pygame.font.Font("./font/Minecraft.ttf", 100)
        self.Screen = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight))
        pygame.display.set_caption("Kim Pong Un")

# Partie III ↓
        self.Score1 = 0
        self.Score2 = 0
        self.ScreenWidth = 1280
        self.ScreenHeight = 720
        self.filetWidth = 20
        self.filetHeight = 5
# Partie III ↑

    def Event(self) -> None:
        eventKey = pygame.key.get_pressed()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.Launched = False

# Partie IV ↓
        if (eventKey[pygame.K_z]):
            self.Bar1.moveUp()
        if (eventKey[pygame.K_s]):
            self.Bar1.moveDown()
        if (eventKey[pygame.K_UP]):
            self.Bar2.moveUp()
        if (eventKey[pygame.K_DOWN]):
            self.Bar2.moveDown()
# Partie IV ↑



    def Drawfilet(self) -> None:
        varX: int = int(self.ScreenWidth / 2 - self.filetWidth / 2)
        varY: int = int(self.filetHeight / 2)

        while (varY < self.ScreenHeight):
            pygame.draw.rect(self.Screen, (200, 200, 200), [varX, varY, self.filetWidth, self.filetHeight])
            varY += self.filetHeight * 2

    def DrawGame(self) -> None:
            self.Drawfilet()
            self.DrawScore()
            self.ball.Draw(self.Screen)
            self.Bar1.Draw(self.Screen)
            self.Bar2.Draw(self.Screen)

    def DrawScore(self) -> None:
        PosY: int = int(self.ScreenHeight / 15)
        PosX: int = int(self.ScreenWidth / 2 - self.ScreenWidth / 15)
        SurfaceTmp: pygame.surface.Surface

        SurfaceTmp = self.Font.render(str(self.Score1), True, (255, 255, 255))
        self.Screen.blit(SurfaceTmp, [PosX - SurfaceTmp.get_width(), PosY, SurfaceTmp.get_width(), SurfaceTmp.get_height()])
        SurfaceTmp = self.Font.render(str(self.Score2), True, (255, 255, 255))
        PosX = int(self.ScreenWidth / 2 + self.ScreenWidth / 15)
        self.Screen.blit(SurfaceTmp, [PosX, PosY, SurfaceTmp.get_width(), SurfaceTmp.get_height()])

    def Loop(self) -> None:
        while (self.Launched):
            self.Screen.fill((0,0,0))
            pygame.time.Clock().tick(60)
            self.Event()
            self.DrawGame()
            self.ball.Collision(self.Bar1.rect, self.Bar2.rect, self.ScreenHeight)
            self.ball.Move()

# Partie VI - 2 ↓
            if (self.ball.outOfBorder(self.ScreenWidth) == 1):
                self.Score1 += 1
                self.ball.Reset(self.ScreenWidth, self.ScreenHeight)
            elif (self.ball.outOfBorder(self.ScreenWidth) == 2):
                self.Score2 += 1
                self.ball.Reset(self.ScreenWidth, self.ScreenHeight)
# Partie VI - 2 ↑

            pygame.display.flip()

def main_loop():
    myGame: Game = Game()

    myGame.Loop()

if __name__ == "__main__":
    main_loop()