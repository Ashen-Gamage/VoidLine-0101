import sys
import pygame

class Game:  # use object-oriented
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('VoidLine-0101')  # name for the game window
        self.screen = pygame.display.set_mode((650, 450))  # initialize the window
        self.clock = pygame.time.Clock()  # clock rate
        self.img = pygame.image.load('../assets/images/Cloud.jpg')  # give location of the image
        self.img_pos = [11, 26]

    def run(self):
        while True:
            self.screen.blit(self.img, (100, 100))# put the image in specific place
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

Game().run()  # creates Game object and runs the game loop
