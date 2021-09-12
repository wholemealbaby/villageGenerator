from mcpi.minecraft import Minecraft
from random import randint
import numpy as np
from math import fabs
import Plot as plot


mc = Minecraft.create()
player = mc.player


if __name__ == "__main__":
    mc = Minecraft.create()
    player = mc.player

    WALL_MATERIALS = [5, 17, 24, 98, 155, 159, 172, 179, 215, 251]
    FLOOR_MATERIALS = [5, 24, 35, 100, 155, 159, 162, 179, 201, 251]

    px, py, pz = player.getPos()

    py -= 1

    p.cut_plot(20)
