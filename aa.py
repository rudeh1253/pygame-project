import pygame, sys
from pygame.locals import *
import time
import random

pygame.init()

width = 960
height = 720

screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
pygame.display.set_caption('alstroemeria')
clock = pygame.time.Clock()

class button :


    def draw(self, screen, x, y, color, width, height, text = ''):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.width = width
        self.height = height

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '' :
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, True, (0, 0, 0))
            screen.blit(text, (self.x + int(self.width / 2 - text.get_width()/2), self.y + int(self.height / 2 - text.get_height() / 2)))

select_button = button()

finish = False
select1 = False # I will
select2 = False # Do not~
select3 = False # Let it be~
select4 = False # yesterday
speed1 = True # 1 second
speed2 = False # x 2
speed3 = False


def __drawButton(x, y, color, width, height, text = '') :
    select_button.draw(screen, x, y, color, width, height, text)

def initGame() :
    global finish, select1, select2, select3, select4, speed1, speed2, speed3
    sa = (255, 0, 0)
    sb = (255, 255, 255)
    sc = (255, 255, 255)
    while not finish :
        screen.fill((255, 255, 255))
        __drawButton(60, 60, (200, 200, 200), 360, 240, 'I will')
        __drawButton(480, 60, (200, 200, 200), 360, 240, 'Do Not Go Gentle into That Good Night')
        __drawButton(60, 420, (200, 200, 200), 360, 240, 'Do-Re-Mi')
        __drawButton(480, 420, (200, 200, 200), 360, 240, 'Yesterday')
        __drawButton(150, 300, sa, 200, 120, 'slow')
        __drawButton(350, 300, sb, 200, 120, 'fast')
        __drawButton(550, 300, sc, 200, 120, 'fastest')
        pygame.display.flip()
        clock.tick(120)

        for event in pygame.event.get() :
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT :
                finish = True
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if 60 < pos[0] < 420 :
                    if 60 < pos[1] < 300 :
                        select1 = True
                        finish = True
                    elif 420 < pos[1] < 660 :
                        select3 = True
                        finish = True
                elif 480 < pos[0] < 840 :
                    if 60 < pos[1] < 300 :
                        select2 = True
                        finish = True
                    elif 420 < pos[1] < 660 :
                        select4 = True
                        finish = True

                if 300 < pos[1] < 420 :
                    if 150 < pos[0] < 350 :
                        sa = (255, 0, 0)
                        sb = (255, 255, 255)
                        sc = (255, 255, 255)
                        speed1 = True
                        speed2 = False
                        speed3 = False

                    elif 350 < pos[0] < 550 :
                        sa = (255, 255, 255)
                        sb = (255, 0, 0)
                        sc = (255, 255, 255)
                        speed1 = False
                        speed2 = True
                        speed3 = False

                    elif 550 < pos[0] < 750 :
                        sa = (255, 255, 255)
                        sb = (255, 255, 255)
                        sc = (255, 0, 0)
                        speed1 = False
                        speed2 = False
                        speed3 = True



def game_select(spd, select_game = '') :
    global finish
    font = pygame.font.SysFont('comicsans', 30)
    f1 = open(select_game, 'r')
    line = f1.read()
    line = line.split()
    i = 0
    score = 0
    answer = []
    is_right = False
    corr = False
    __time = time.time()
    timing_num = 2
    process = False


    while not finish :

        clock.tick(120)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_a :
                    answer.append('a')
                elif event.key == pygame.K_b :
                    answer.append('b')
                elif event.key == pygame.K_c:
                    answer.append('c')
                elif event.key == pygame.K_d:
                    answer.append('d')
                elif event.key == pygame.K_f:
                    answer.append('f')
                elif event.key == pygame.K_g:
                    answer.append('g')
                elif event.key == pygame.K_h:
                    answer.append('h')
                elif event.key == pygame.K_i:
                    answer.append('i')
                elif event.key == pygame.K_j:
                    answer.append('j')
                elif event.key == pygame.K_k:
                    answer.append('k')
                elif event.key == pygame.K_m:
                    answer.append('m')
                elif event.key == pygame.K_n:
                    answer.append('n')
                elif event.key == pygame.K_o:
                    answer.append('o')
                elif event.key == pygame.K_p:
                    answer.append('p')
                elif event.key == pygame.K_q:
                    answer.append('q')
                elif event.key == pygame.K_r:
                    answer.append('r')
                elif event.key == pygame.K_s:
                    answer.append('s')
                elif event.key == pygame.K_t:
                    answer.append('t')
                elif event.key == pygame.K_u:
                    answer.append('u')
                elif event.key == pygame.K_v:
                    answer.append('v')
                elif event.key == pygame.K_w:
                    answer.append('w')
                elif event.key == pygame.K_x:
                    answer.append('x')
                elif event.key == pygame.K_e:
                    answer.append('e')
                elif event.key == pygame.K_l:
                    answer.append('l')
                elif event.key == pygame.K_y:
                    answer.append('y')
                elif event.key == pygame.K_z:
                    answer.append('z')
                elif event.key == pygame.K_SPACE :
                    is_right = True
                elif event.key == pygame.K_BACKSPACE :
                    if answer :
                        del answer[-1]

        if not process :
            if (time.time() - __time) >= random.randrange(1, 4):
                text = font.render(line[i], True, (255, 255, 255))
                text_num = font.render(str(timing_num), True, (255, 255, 255))
                text_x = random.randrange(100, 830)
                text_y =  random.randrange(120, 570)
                timing_num_timing = time.time()
                process = True
                __time = time.time()

        if process :
            if (time.time() - timing_num_timing) >= spd :
                if timing_num != 0 :
                    timing_num -= 1
                    text_num = font.render(str(timing_num), True, (255, 255, 255))
                    timing_num_timing = time.time()
            screen.blit(text, (text_x, text_y))
            screen.blit(text_num, (text_x - 20, text_y))
            if (time.time() - __time) >= spd * 3 :
                line[i] = ''
                timing_num = 2
                timing_num_timing = time.time()
                i += 1
                process = False


        tt = ''.join(answer)
        answer_text = font.render(tt, True, (255, 255, 255))
        screen.blit(answer_text, (430, 620))

        if is_right :
            answer = []
            if line[i].lower() == tt :
                corr = True
                line[i] = ''
                is_right = False
            elif line[i] == '' :
                is_right = False
                process = False
                timing_num = 2
                i += 1
            else :
                line[i] = ''
                is_right = False
                process = False
                timing_num = 2
                i += 1

            if corr :
                if timing_num == 0 :
                    score += 10

                    process = False
                    timing_num = 2
                    i += 1
                    corr = False
                else :
                    process = False
                    timing_num = 2
                    i += 1
                    corr = False

        score_text = font.render(str(score), True, (255, 255, 255))
        screen.blit(score_text, (0, 0))

        if i == len(line) :
            scorere = 'your score = ' + str(score) + ' / ' + str(len(line) * 10)
            font = pygame.font.SysFont('comicsans', 50)
            text_score = font.render(scorere, True, (255, 255, 255))
            screen.blit(text_score, (400, 300))
            finish = True

        pygame.display.flip()

    finish = False
    return score, len(line)

while not finish :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            finish = True

            quit()
    initGame()
    finish = False

    if select1 == True :
        if (speed1 == True) and (speed2 == False) and (speed3 == False) :
            score, length = game_select(1, 'select1.txt')
            select1 = False
        elif (speed1 == False) and (speed2 == True) and (speed3 == False) :
            score, length = game_select(0.5, 'select1.txt')
            select1 = False
        elif (speed1 == False) and (speed2 == False) and (speed3 == True) :
            score, length = game_select(0.2, 'select1.txt')
            select1 = False
    if select2 == True :
        if (speed1 == True) and (speed2 == False) and (speed3 == False) :
            score, length = game_select(1, 'select2.txt')
            select2 = False
        elif (speed1 == False) and (speed2 == True) and (speed3 == False) :
            score, length = game_select(0.5, 'select2.txt')
            select2 = False
        elif (speed1 == False) and (speed2 == False) and (speed3 == True) :
            score, length = game_select(0.2, 'select2.txt')
            select2 = False
    if select3 == True :
        if (speed1 == True) and (speed2 == False) and (speed3 == False) :
            score, length = game_select(1, 'select3.txt')
            select3 = False
        elif (speed1 == False) and (speed2 == True) and (speed3 == False) :
            score, length = game_select(0.5, 'select3.txt')
            select3 = False
        elif (speed1 == False) and (speed2 == False) and (speed3 == True) :
            score, length = game_select(0.2, 'select3.txt')
            select3 = False
    if select4 == True :
        if (speed1 == True) and (speed2 == False) and (speed3 == False) :
            score, length = game_select(1, 'select4.txt')
            select4 = False
        elif (speed1 == False) and (speed2 == True) and (speed3 == False) :
            score, length = game_select(0.5, 'select4.txt')
            select4 = False
        elif (speed1 == False) and (speed2 == False) and (speed3 == True) :
            score, length = game_select(0.2, 'select4.txt')
            select4 = False


    time.sleep(5)
    pygame.display.flip()