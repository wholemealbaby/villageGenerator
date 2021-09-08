from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()
player = mc.player

WALL_MATERIALS = [5, 17, 24, 98, 155, 159, 172, 179, 215, 251]
FLOOR_MATERIALS = [5, 24, 35, 100, 155, 159, 162, 179, 201, 251]

class Room:
    def __init__(self, x, y, z):
        # PROPERTIES
        width = random.randint(5, 12)       # x axis
        height = 5                          # y axis
        length = random.randint(5, 12)      # z axis
        wallMaterial = WALL_MATERIALS[random.randint(0, len(WALL_MATERIALS)-1)]
        floorMaterial = FLOOR_MATERIALS[random.randint(0, len(WALL_MATERIALS) - 1)]

        # LOCATION
        x0 = x - int(width/2)
        y0 = y
        z0 = z - int

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
    mc.setBlocks(px, py-1, pz, px+l, py-1, pz+w, 5, 0)
    mc.setBlocks(px, py +h+1, pz, px + l, py + h + 1, pz + w, 5, 0)

buildRoom(8, 5, 8)


