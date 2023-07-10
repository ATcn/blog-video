#!/usr/bin/env python3
# coding=utf-8
"""
@File : 01精灵.py
@Author  : AT
@Create  : 2023/7/10 13:54
@Desc    :
"""

import pygame
from pygame.locals import *
import moviepy.editor as mpy
import random

# 初始化Pygame
pygame.init()

# 创建窗口
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

# 加载背景图像并缩放
background_image = pygame.image.load('01screen.jpg')
background_image = pygame.transform.scale(background_image, (window_width, window_height))

# 加载精灵图像并缩小尺寸
sprite_image = pygame.image.load('01sprite.jpg')
sprite_image = pygame.transform.scale(sprite_image, (100, 100))

# 设置精灵1的初始位置和速度
sprite1_x, sprite1_y = 100, 100
sprite1_vx, sprite1_vy = 100, 80

# 设置精灵2的初始位置和速度
sprite2_x, sprite2_y = 600, 400
sprite2_vx, sprite2_vy = -120, -90

# 设置精灵3的初始位置和速度
sprite3_x, sprite3_y = window_width // 2, window_height // 2
sprite3_speed = 150

# 场景标识：0表示场景1，1表示场景2
scene = 0

# 更新精灵的位置
def update(dt):
    global sprite1_x, sprite1_y, sprite2_x, sprite2_y, sprite3_x, sprite3_y, scene

    if scene == 0:
        sprite1_x += sprite1_vx * dt
        sprite1_y += sprite1_vy * dt

        sprite2_x += sprite2_vx * dt
        sprite2_y += sprite2_vy * dt

        # 判断精灵1和精灵2是否离开画面
        if sprite1_x < -sprite_image.get_width() or sprite1_x > window_width or \
                sprite1_y < -sprite_image.get_height() or sprite1_y > window_height or \
                sprite2_x < -sprite_image.get_width() or sprite2_x > window_width or \
                sprite2_y < -sprite_image.get_height() or sprite2_y > window_height:
            scene = 1

    elif scene == 1:
        sprite3_x += random.randint(-1, 1) * sprite3_speed * dt
        sprite3_y += random.randint(-1, 1) * sprite3_speed * dt

    # 绘制背景图像
    window.blit(background_image, (0, 0))

    # 绘制精灵1、精灵2和精灵3到窗口
    window.blit(sprite_image, (sprite1_x, sprite1_y))
    window.blit(sprite_image, (sprite2_x, sprite2_y))
    window.blit(sprite_image, (sprite3_x, sprite3_y))

    pygame.display.flip()

# 主循环
running = True
while running:
    dt = clock.tick(60) / 1000.0

    # 处理事件
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    update(dt)

# 退出Pygame
pygame.quit()

