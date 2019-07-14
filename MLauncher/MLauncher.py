#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, os, urllib

pygame.init()

screen = pygame.display.set_mode((610, 500))

pygame.display.set_icon(pygame.image.load('image/ico2.ico'))
pygame.display.set_caption("MLauncher")

def game():
    pass

def server():
    pass

def update():
    pass

def vk():
    os.system("explorer https://vk.com/club_g_games")

MLauncher = True
while MLauncher:
    font1 = pygame.font.Font(None, 30)
    text1 = font1.render(u"Версия: 0.0.1 Alpha", True, (0,0,0))

    font2 = pygame.font.Font(None, 30)
    text2 = font2.render(u"Играть", True, (0,0,0))

    font3 = pygame.font.Font(None, 30)
    text3 = font3.render(u"Сервер", True, (0,0,0))

    font4 = pygame.font.Font(None, 30)
    text4 = font4.render(u"Обновление MLaunchera", True, (0,0,0))

    font5 = pygame.font.Font(None, 30)
    text5 = font5.render(u"Группа VK", True, (0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MLauncher = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                MLauncher = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 320 and pygame.mouse.get_pos()[1] >= 170:
                if pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1] <= 270:
                    vk()

    bg = pygame.draw.rect(screen,(114,114,114),(0,0,800,640));

    screen.blit(text1, [400, 470])

    button1 = pygame.draw.rect(screen,(0,0,0),(30,35,260,100));
    button11 = pygame.draw.rect(screen,(255,255,255),(32,37,256,96));
    screen.blit(text2, [117, 75])

    button2 = pygame.draw.rect(screen,(0,0,0),(320,35,260,100));
    button22 = pygame.draw.rect(screen,(255,255,255),(322,37,256,96));
    screen.blit(text3, [410, 75])

    button3 = pygame.draw.rect(screen,(0,0,0),(30,170,260,100));
    button33 = pygame.draw.rect(screen,(255,255,255),(32,172,256,96));
    screen.blit(text4, [36, 210])

    button4 = pygame.draw.rect(screen,(0,0,0),(320,170,260,100));
    button44 = pygame.draw.rect(screen,(255,255,255),(322,172,256,96));
    screen.blit(text5, [410, 210])

    pygame.display.update()

pygame.quit()
exit()
