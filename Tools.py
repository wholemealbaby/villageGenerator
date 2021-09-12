from mcpi.minecraft import Minecraft
import numpy as np
import random

mc = Minecraft.create()
player = mc.player


def find_surface_y(x, z, y=60):
    # default y val is 60 because mc sea level is 63
    while True:
        if mc.getBlock(x, y, z) == 0:
            headRoom = True
            # flag that indicates whether any
            # blocks exist above the y value
            # to ensure the code isn't looking at a cave or something

            for i in range(1, 32, 4):
                if mc.getBlock(x, y + i, z) != 0:
                    headRoom = False
                    y = y + i
                    break

            if headRoom:
                break
        y += 1

    return [x, y, z]


# performs mc.getBlocks with coordinates in arrays for ease
def getBlocks_from_tuple(tup1, tup2):
    mc.getBlocks(tup1[0], tup1[1], tup1[2], tup2[0], tup2[1], tup2[2])


# performs
def setBlocks_from_tuple(tup1, tup2, id, dataid=0):
    mc.setBlocks(tup1[0], tup1[1], tup1[2], tup2[0], tup2[1], tup2[2], id, dataid)


# returns lowest of 2 variables
def get_lo(a, b):
    if a < b:
        return a
    else:
        return b


# returns highest of 2 variables
def get_hi(a, b):
    if a > b:
        return a
    else:
        return b


def get_blocks_info(x0, y0, z0, x1, y1, z1):
    blocks = mc.getBlocks(x0, y0, z0, x1, y1, z1)
    blocks = list(blocks)
    blocks = np.array(blocks)

    blocks_coords = []

    # saving decimal component of coordinates to allow them to be added back
    # onto the iterator value
    x_decimal = x0 - int(x0)
    y_decimal = y0 - int(y0)
    z_decimal = z0 - int(z0)

    for y in range(int(get_lo(y0, y1)), int(get_hi(y0, y1) + 1)):
        for x in range(int(get_lo(x0, x1)), int(get_hi(x0, x1)) + 1):
            for z in range(int(get_lo(z0, z1)), int(get_hi(z0, z1)) + 1):
                blocks_coords.append([x + x_decimal, y + y_decimal, z + z_decimal])

    x_dist = int(fabs(x0 - x1) + 1)
    y_dist = int(fabs(y0 - y1) + 1)
    z_dist = int(fabs(z0 - z1) + 1)

    blocks_coords = np.array(blocks_coords)

    blocks.reshape(x_dist * y_dist, z_dist)

    blocks_info = []

    for i in range(blocks.size):
        blocks_info.append([blocks[i], blocks_coords[i]])

    return np.array(blocks_info, dtype=object)
