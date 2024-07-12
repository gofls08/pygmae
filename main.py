import pygame
import sys
from pygame.locals import QUIT

import os
import random

import random
from pygame.locals import *


FPS = 10
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption('GAMES')
SURFACE = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
FPSCLOCK = pygame.time.Clock()
Big_font = pygame.font.SysFont(None, 80)
Small_font = pygame.font.SysFont(None, 40)

def draw_snake(snake_coords):
    for coord in snake_coords:
        x, y = coord['x'] * CELL_SIZE, coord['y'] * CELL_SIZE
        pygame.draw.rect(SURFACE, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

def draw_apple(coord):
    x, y = coord['x'] * CELL_SIZE, coord['y'] * CELL_SIZE
    pygame.draw.rect(SURFACE, RED, (x, y, CELL_SIZE, CELL_SIZE))

def snake_run():
    start_x = random.randint(5, WINDOW_WIDTH // CELL_SIZE - 6)
    start_y = random.randint(5, WINDOW_HEIGHT // CELL_SIZE - 6)
    snake_coords = [{'x': start_x, 'y': start_y},
                    {'x': start_x - 1, 'y': start_y},
                    {'x': start_x - 2, 'y': start_y}]
    direction = 'right'

    apple_x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1)
    apple_y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1)
    apple = {'x': apple_x, 'y': apple_y}

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP and direction != 'down':
                    direction = 'up'
                elif event.key == K_DOWN and direction != 'up':
                    direction = 'down'
                elif event.key == K_LEFT and direction != 'right':
                    direction = 'left'
                elif event.key == K_RIGHT and direction != 'left':
                    direction = 'right'

        if direction == 'up':
            new_head = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] - 1}
        elif direction == 'down':
            new_head = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] + 1}
        elif direction == 'left':
            new_head = {'x': snake_coords[0]['x'] - 1, 'y': snake_coords[0]['y']}
        elif direction == 'right':
            new_head = {'x': snake_coords[0]['x'] + 1, 'y': snake_coords[0]['y']}

        snake_coords.insert(0, new_head)

        if (new_head['x'] == apple['x'] and new_head['y'] == apple['y']):
            apple_x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1)
            apple_y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1)
            apple = {'x': apple_x, 'y': apple_y}
        else:
            del snake_coords[-1]

        SURFACE.fill(WHITE)
        draw_snake(snake_coords)
        draw_apple(apple)
        pygame.display.update()

        if (new_head['x'] < 0 or new_head['x'] >= WINDOW_WIDTH // CELL_SIZE or
            new_head['y'] < 0 or new_head['y'] >= WINDOW_HEIGHT // CELL_SIZE or
            new_head in snake_coords[1:]):
            return

        fps_clock.tick(FPS)

fps_clock = pygame.time.Clock()

def snake_start():
    while True:
        SURFACE.fill(WHITE)
        
        play_button = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2, 100, 40)
        
        pygame.draw.rect(SURFACE, GREEN, play_button)
        play_text = pygame.font.Font(None, 30).render("Play", True, BLACK)
        
        SURFACE.blit(play_text, play_button.move(20, 10))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                
                if play_button.collidepoint(mouse_x, mouse_y):
                    return
        
        pygame.display.update()
        fps_clock.tick(FPS)


def break_run():
    bricks = [pygame.Rect(50 + 100*i, 50 + 20*j, 80, 10) for i in range(7) for j in range(3)]
    paddle = pygame.Rect(400, 300, 60, 10)
    ball = pygame.Rect(400, 300, 10, 10)
    ball_dx = 1
    ball_dy = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left >0:
            paddle.left-=2
        if keys[pygame.K_RIGHT] and paddle.right >0:
            paddle.right+=2

        ball.left += ball_dx
        ball.top += ball_dy

        if ball.left <= 0 or ball.right>=WINDOW_WIDTH:
            ball_dx*=-1
        if ball.top <=0:
            ball_dy*=-1

        if ball.top >= paddle.bottom:
            return

        if ball.colliderect(paddle):
            ball_dy*=-1

        hit_index = ball.collidelist(bricks)
        if hit_index != -1:
            hit_brick = bricks.pop(hit_index)
            # print(hit_brick)
            ball_dy*=-1

        if len(bricks) == 0:
            return

        SURFACE.fill((0,0,0))
        pygame.draw.rect(SURFACE, WHITE, paddle)
        pygame.draw.rect(SURFACE, WHITE, ball)
        for brick in bricks:
            pygame.draw.rect(SURFACE, RED, brick)

        pygame.display.flip()
        pygame.time.delay(FPS)
# 

def baseball_run():
    text = ""
    ans = ""
    # 
    text_surface = Big_font.render(text, True, WHITE)
    retrun_surface = Small_font.render(ans, True, WHITE)
    num = random.sample(range(1,9),4)
    print(num)
    #임의의 숫자 4개 선언, 중복x
    i = 1       
    n=1                                             
    answers = []
    def strike(e):
        ans = ""
        list_user =[]
        str=0
        ball = 0
        user = e
        for n in range(4):
            list_user.append(int(user[n]))
            n = n + 1
            # print(list_user)
        for a in range(4):
            if num[a] == list_user[a]:
                str = str + 1
            for b in range(4):
                if num[a] == list_user[b]:
                    ball = ball + 1 
        if str == 4:
            return ans
        else:
            ans = f"{str} strike, {ball-str} ball, {4-ball} out"
            return list_user, ans
         
        
        # SURFACE.blit(retrun_surface, (100,100))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                
                if event.key == pygame.K_RETURN:
                    # print(text)
                    a = strike(text) 
                    # print(a[0], a[1])
                    if a!="":
                        if(len(answers)>=5):
                            del answers[0]
                        answers.append(a)
                        print(answers)
                        retrun_surface = Small_font.render(str(a), True, WHITE)
                         
                    else:
                        return
                    i=i+1
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                if i>= 10:
                    return
                text_surface = Big_font.render(text, True, WHITE)
        SURFACE.fill(BLACK)
        SURFACE.blit(text_surface, (100, 100))
        for n in range(len(answers)):
            SURFACE.blit(Small_font.render(str(answers[n]), True, WHITE) , (100, 150+50*(n+1)))
            # pygame.display.update()
        pygame.display.flip()    
import requests
from bs4 import BeautifulSoup
def lol():
    text=""
    def op_gg(e):
        Name = e
        SummonerName = ""
        Ranking = ""
        TierUnranked = ""
        LeagueType = []
        Tier = []
        LP = []
        Wins = []
        Losses = []
        Ratio = []
        url='https://www.op.gg/summoner/userName=' + Name
        hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        
        for i in soup.select('div[class=SummonerName]'):
            SummonerName = i.text

        for i in soup.select('span[class=ranking]'):
            Ranking = i.text

        TierUnranked = soup.select('div.Cell')

        for i in soup.select('div[class=LeagueType]'):
            LeagueType.append(i.text)


        for i in soup.select('div[class=Tier]'):
            Tier.append(i.text)

        for i in soup.select('div[class=LP]'):
            LP.append(i.text)

        for i in soup.select('span[class=Wins]'):
            Wins.append(i.text)

        for i in soup.select('span[class=Losses]'):
            Losses.append(i.text)

        for i in soup.select('span[class=Ratio]'):
            Ratio.append(i.text)

        if SummonerName != "":
            check = input(SummonerName + "님의 솔로랭크 정보가 궁금하시면 '솔랭'을, 자유랭크 정보가 궁금하시면 '자랭'을 입력해주세요: ")
            if check == '솔랭':
                if 'Unranked' in str(TierUnranked[0]):
                    return SummonerName + "님은 솔로랭크 Unranked입니다."
                else:
                    # print("==================================")
                    # print(SummonerName + "님의 솔로랭크 정보입니다.")
                    # print("==================================")
                    # print("티어: " + Tier[0].strip('\n\t'))
                    # print("LP: " + LP[0])
                    # print("승/패: " + Wins[0] + " " + Losses[0])
                    # print("승률: " + Ratio[0])

                    return {SummonerName, Tier[0].strip('\n\t'), LP[0], Wins[0] + " " + Losses[0], Ratio[0]}

            elif check == '자랭':
                if 'Unranked' in str(TierUnranked[1]):
                    # print("==================================")
                    # print(SummonerName + "님은 자유랭크 Unranked입니다.")
                    # print("==================================")
                    return {SummonerName}
                else:
                    # print("=====================================")
                    # print(SummonerName + "님의 자유랭크 정보입니다.")
                    # print("=====================================")
                    # print("티어: " + Tier[1].strip('\n\t'))
                    # print("LP: " + LP[1])
                    # print("승/패: " + Wins[1] + " " + Losses[1])
                    # print("승률: " + Ratio[1])
                    return {SummonerName, Tier[1].strip('\n\t'), LP[1], Wins[1] + " " + Losses[1], Ratio[1]}

            else:
                return "Error! 정확하게 입력해주세요."
        else:
            return "소환사 정보가 없습니다."
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                
                if event.key == pygame.K_RETURN:
                    a= op_gg(text) 
                    print(a)                   
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                # if i>= 10:
                #     return
                # text_surface = Big_font.render(text, True, WHITE)
        SURFACE.fill(BLACK)
        # SURFACE.blit(Big_font.render(a, True, WHITE), (100, 100))
        # for n in range(len(a)):
        #     SURFACE.blit(Small_font.render(str(a[n]), True, WHITE) , (100, 150+50*(n+1)))
        #     pygame.display.update()
        pygame.display.flip()  
          


def main():
    message_Title = Big_font.render("Games", True, WHITE) 
    a = Small_font.render("Break_ball", True, WHITE)
    b = Small_font.render("Snake", True, WHITE)
    c = Small_font.render("Baseball_num", True, WHITE)
    a1 = Small_font.render("1", True, WHITE)
    b2 = Small_font.render("2", True, WHITE)
    c3 = Small_font.render("3", True, WHITE)
    press = Small_font.render("Press the number", True, WHITE)
    while True:
        SURFACE.fill(BLACK)
        for event in pygame.event.get():  
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                        break_run()
                if event.key == pygame.K_2:
                        snake_start()
                        snake_run()
                if event.key == pygame.K_3:
                    baseball_run()
                if event.key == pygame.K_4:
                    lol()
        SURFACE.blit(message_Title, (220, 20))
        SURFACE.blit(a, (30, 300))
        SURFACE.blit(b, (250, 300))
        SURFACE.blit(c, (400, 300))
        SURFACE.blit(a1, (100, 350))
        SURFACE.blit(b2, (280, 350))
        SURFACE.blit(c3, (480, 350))
        SURFACE.blit(press, (200, 400))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
