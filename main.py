from mcpi.minecraft import Minecraft
from random import randint
import numpy as np


def buildRoom(l, h, w):
    px, py, pz = player.getPos()

    px, py, pz = int(px), int(py), int(pz)
    px += 2

    # Walls
    mc.setBlocks(px, py, pz, px, py + h, pz + w, 45)
    mc.setBlocks(px, py, pz, px + l, py + h, pz, 45)
    mc.setBlocks(px + l, py, pz, px + l, py + h, pz + w, 45)
    mc.setBlocks(px, py, pz + w, px + l, py + h, pz + w, 45)

    # roof and floor
    mc.setBlocks(px, py - 1, pz, px + l, py - 1, pz + w, 5, 0)
    mc.setBlocks(px, py + h + 1, pz, px + l, py + h + 1, pz + w, 5, 0)


# Pass this function and x and z and it will find the surface of the world at that horizontal location
def find_surface_y(x, z, y=60):
    # default y val is 60 because mc sea level is 63
    while True:
        if mc.getBlock(x, y, z) == 0:
            headRoom = True
            # flag that indicates whether any
            # blocks exist above the y value
            # to ensure the code isn't looking at a cave or something

            for i in range(1, 16, 4):
                if mc.getBlock(x, y + i, z) != 0:
                    headRoom = False
                    y = y + i
                    break

            if headRoom:
                break
        y += 1

    return [x, y, z]


def get_plot():
    # generating random X and Z values relative to the player within a 300block radius
    player_x, player_y, player_z = player.getPos()
    rx = randint(int(player_x) - 300, int(player_x) + 300)
    rz = randint(int(player_z) - 300, int(player_z) + 300)

    plot = [find_surface_y(rx, rz)] # finds the surface of the random horizontal coordinate

    # appends coordinates of every second surface block inside a 20x20 plot
    for x in range(1, 20, 2):
        for z in range(1, 20, 2):
            plot.append(find_surface_y(rx + x, rz + z))
    print(plot)


if __name__ == "__main__":
    mc = Minecraft.create()
    player = mc.player

    WALL_MATERIALS = [5, 17, 24, 98, 155, 159, 172, 179, 215, 251]
    FLOOR_MATERIALS = [5, 24, 35, 100, 155, 159, 162, 179, 201, 251]

    px, py, pz = player.getPos()

    get_plot()
