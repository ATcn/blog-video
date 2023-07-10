#!/usr/bin/env python3
# coding=utf-8
"""
@File : 移动圆球.py.py
@Author  : AT
@Create  : 2023/7/10 10:38
@Desc    : 
"""

import turtle
from time import sleep


class Ball:

    def __init__(self):
        self

# function for movement of an object
def draw_ball(obj):
    # to fill the color in ball
    obj.fillcolor('orange')

    # start color filling
    obj.begin_fill()

    # draw circle
    obj.circle(20)

    # end color filling
    obj.end_fill()


# Driver Code
if __name__ == "__main__":

    # create a screen object
    screen = turtle.Screen()

    # set screen size
    screen.setup(600, 600)

    # screen background color
    screen.bgcolor('green')

    # screen updaion
    screen.tracer(0)

    # create a turtle object object
    ball_pen = turtle.Turtle()

    # set a turtle object color
    ball_pen.color('orange')

    # set turtle object speed
    ball_pen.speed(10)

    # set turtle object width
    ball_pen.width(2)

    # hide turtle object
    ball_pen.hideturtle()

    # turtle object in air
    ball_pen.penup()

    # set initial position
    ball_pen.goto(0, 0)

    # move turtle object to surface
    ball_pen.pendown()

    # infinite loop
    for i in range(10):
        # clear turtle work
        ball_pen.clear()

        # forward motion by turtle object
        ball_pen.left(20)  # 角度，轨迹转圈完整性
        # print(f'ball_pen.left -> {ball_pen.position()}')

        ball_pen.forward(50)  # 圆大小
        print(f'ball_pen.forward -> {ball_pen.position()}')

        # call function to draw ball
        draw_ball(ball_pen)

        # update screen
        screen.update()

        sleep(0.005)
        # 保存结局

    # 结束绘画并保存
    turtle.done()
