# 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
# （初学者不一定可以完整实现，但请务必先自己动手，你会从中学习到很多知识的^_^）
#
# 假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
# 游戏生成1只乌龟和10条鱼
# 它们的移动方向均随机
# 乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
# 当移动到场景边缘，自动向反方向移动
# 乌龟初始化体力为100（上限）
# 乌龟每移动一次，体力消耗1
# 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
# 鱼暂不计算体力
# 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束

import random


class World:
    def __init__(self):
        self.x = 10
        self.y = 10

    def set_world(self):
        world_map = self.x * self.y


class Fish:
    def __init__(self):
        self.x = random.randint(10)
        self.y = random.randint(10)

    def default_location(self):
        location = self.x * self.y

    def move(self):
        move_speed = 1
