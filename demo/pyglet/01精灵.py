#!/usr/bin/env python3
# coding=utf-8
"""
@File : 01精灵.py
@Author  : AT
@Create  : 2023/7/10 13:54
@Desc    : 
"""

import pyglet
import random

# 创建一个窗口
window = pyglet.window.Window(width=800, height=600)

# 加载背景图像
background_image = pyglet.image.load('01screen.jpg')

# 缩放背景图像
background_sprite = pyglet.sprite.Sprite(background_image)
background_sprite.scale_x = window.width / background_sprite.width
background_sprite.scale_y = window.height / background_sprite.height

# 加载精灵图像并缩小尺寸
sprite_image = pyglet.image.load('01sprite.jpg')
scaled_image = sprite_image.get_region(0, 0, sprite_image.width, sprite_image.height).get_texture()
scaled_image.width = 100  # 指定缩小后的宽度
scaled_image.height = 100  # 指定缩小后的高度

# 创建两个精灵
sprite1 = pyglet.sprite.Sprite(scaled_image)
sprite2 = pyglet.sprite.Sprite(scaled_image)

# 设置精灵的初始位置和速度
sprite1.x = 100
sprite1.y = 100
sprite1.vx = random.randint(50, 150)  # 水平速度
sprite1.vy = random.randint(50, 150)  # 垂直速度

sprite2.x = 500
sprite2.y = 400
sprite2.vx = random.randint(-150, -50)  # 水平速度
sprite2.vy = random.randint(-150, -50)  # 垂直速度

# 创建第三个精灵
sprite3 = pyglet.sprite.Sprite(scaled_image)

# 设置第三个精灵的初始位置和速度
sprite3.x = window.width / 2
sprite3.y = window.height / 2
sprite3.vx = random.choice([-50, 50])  # 水平速度
sprite3.vy = 0

# 设置场景切换的标志
scene = 1
movement_count = 0

# 更新精灵的位置
def update(dt):
    global scene, movement_count

    if scene == 1:
        sprite1.x += sprite1.vx * dt
        sprite1.y += sprite1.vy * dt

        sprite2.x += sprite2.vx * dt
        sprite2.y += sprite2.vy * dt

        if sprite1.x < 0 or sprite1.x > window.width or sprite1.y < 0 or sprite1.y > window.height:
            scene = 2
            sprite3.x = window.width / 2
            sprite3.y = window.height / 2
            sprite3.vx = random.choice([-50, 50])  # 水平速度
            sprite3.vy = 0
            movement_count = 0

    elif scene == 2:
        sprite3.x += sprite3.vx * dt

        if sprite3.x < 100 or sprite3.x > window.width - 100:
            sprite3.vx *= -1
            movement_count += 1

            if movement_count >= 4:
                sprite3.vx = 0

# 绘制背景和精灵
@window.event
def on_draw():
    window.clear()
    background_sprite.draw()

    if scene == 1:
        sprite1.draw()
        sprite2.draw()

    elif scene == 2:
        sprite3.draw()

# 设置更新函数的定时器
pyglet.clock.schedule_interval(update, 1/60.0)

# 运行程序
pyglet.app.run()


