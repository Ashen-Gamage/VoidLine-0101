import sys
import pygame

class Game:  # use object-oriented
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('VoidLine-0101')  # name for the game window
        self.screen = pygame.display.set_mode((650, 450))  # initialize the window
        self.clock = pygame.time.Clock()  # clock rate
        self.img = pygame.image.load('../assets/images/Cloud.png')  # give location of the image
        self.img.set_colorkey((255,255,255))# remove background from picture its like chromo key in video editing
        self.img_pos = [11, 26]
        self.img_pos =[160,260]
        self.movement=[False,False]#enable movement function

        self.collision_area = pygame.Rect(50,50,300,50)# open collision rectangle

    def run(self):
        while True:
            self.screen.fill ((0,51,12))

            img_r = pygame.Rect(self.img_pos[0],self.img_pos[1],self.img.get_width(),self.img.get_height())# react to collision box , first two is the position second two is parameters for rectangle
            if img_r.colliderect(self.collision_area):#Now its collision test
                pygame.draw.rect(self.screen,(00,100,255),self.collision_area)
            else:
                pygame.draw.rect(self.screen,(00,50,105),self.collision_area)

            self.img_pos[1] += (self.movement[1]-self.movement[0]) *5
            self.screen.blit(self.img, self.img_pos)# put the image in specific place like on screen serface put the image  serface

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # check wheather key is press or not if press movement gonna work
                    if event.key == pygame.K_UP:# If the UP arrow key is pressed
                        self.movement [0] =True  # Set upward movement to True
                    if event.key == pygame.K_DOWN:    # If the DOWN arrow key is pressed
                        self.movement[1] = True # Set downward movement to True
                if event.type == pygame.KEYUP: # Check if any key is not press
                    if event.key == pygame.K_UP: # Check if any key is released
                        self.movement [0]= False # Stop upward movement
                    if event.key == pygame.K_DOWN: # If the DOWN arrow key is released
                        self.movement [1] = False  # Stop downward movement

            pygame.display.update()
            self.clock.tick(60)

Game().run()  # creates Game object and runs the game loop
