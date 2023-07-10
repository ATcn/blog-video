#!/usr/bin/env python3
# coding=utf-8
"""
@File : 多线程动画.py
@Author  : AT
@Create  : 2023/7/10 13:31
@Desc    : 
"""

import turtle
import threading
import random
import queue
import time

# 全局变量，用于控制主线程终止
terminate = False

def draw_square(pen):
    for _ in range(4):
        pen.forward(100)
        pen.right(90)

def pen_thread(q):
    while not terminate:
        try:
            # 从队列中获取任务
            task = q.get(block=False)
            pen = task['pen']
            num_loops = task['num_loops']

            # 随机生成画笔的起始位置
            pen.penup()
            pen.goto(random.randint(-200, 200), random.randint(-200, 200))
            pen.pendown()

            for _ in range(num_loops):
                # 绘制一个正方形
                draw_square(pen)

                # 更新画布
                turtle.update()

                # 暂停一段时间
                time.sleep(0.1)

                # 清空画布
                pen.clear()

            # 结束绘画，并隐藏画笔
            pen.hideturtle()

        except queue.Empty:
            continue

def main():
    # 创建一个画布
    canvas = turtle.Screen()

    # 创建一个队列用于存储绘图任务
    task_queue = queue.Queue()

    # 创建多个线程并启动
    num_threads = 5
    threads = []

    for _ in range(num_threads):
        pen = turtle.Turtle()
        pen.speed(1)
        num_loops = random.randint(1, 10)

        # 将绘图任务放入队列
        task_queue.put({'pen': pen, 'num_loops': num_loops})

    turtle.tracer(0)  # 禁止自动更新画布

    for _ in range(num_threads):
        thread = threading.Thread(target=pen_thread, args=(task_queue,))
        thread.start()
        threads.append(thread)


    # 等待用户关闭窗口
    turtle.mainloop()

    # 设置终止变量为True，使子线程退出循环
    global terminate
    terminate = True

    turtle.done()

    # 等待所有子线程结束
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()

