from mcpi.minecraft import Minecraft
import numpy as np
import random

mc = Minecraft.create()
x, y, z = mc.player.getPos()

brick = 46
oak = 5


def create_house(length, width, height):
    # Makes a rectangle
    for i in range(length):
        for j in range(width):
            for k in range(height):
                if k == 0 or k == height - 1:
                    mc.setBlock(x + i, y + k, z + j, 5)
                elif i == 0 or i == length - 1:
                    mc.setBlock(x + i, y + k, z + j, 5)
                elif j == 0 or j == width - 1:
                    mc.setBlock(x + i, y + k, z + j, 5)
                else:
                    mc.setBlock(x + i, y + k, z + j, 0)


create_house(8, 10, 5)
