from mcpi.minecraft import Minecraft
import random


def find_surface(player_x, player_z):
    player_x = int(player_x)
    player_z = int(player_z)
    randx = random.randint((player_x - 150), (player_x + 150))
    randz = random.randint((player_z - 150), (player_z + 150))

    y = 60
    while True:
        if mc.getBlock(randx, y, randz) == 0:
            headRoom = True # flag that indicates whether any
                            # blocks exist above the y value
            for i in range(1,16):
                if mc.getBlock(randx, y+i, randz) != 0:
                    headRoom = False
                    y = y+i
                    break

            if headRoom == True:
                break
        y += 1


    return randx, y, randz


if __name__ == "__main__":
    mc = Minecraft.create()
    player = mc.player

    WALL_MATERIALS = [5, 17, 24, 98, 155, 159, 172, 179, 215, 251]
    FLOOR_MATERIALS = [5, 24, 35, 100, 155, 159, 162, 179, 201, 251]


    class Room:
        def __init__(self, x, y, z):
            # PROPERTIES
            width = random.randint(5, 12)  # x axis
            height = 5  # y axis
            length = random.randint(5, 12)  # z axis
            wallMaterial = WALL_MATERIALS[random.randint(0, len(WALL_MATERIALS) - 1)]
            floorMaterial = FLOOR_MATERIALS[random.randint(0, len(WA_MATERIALS) - 1)]

            # LOCATION
            x0 = x - int(width / 2)
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
        mc.setBlocks(px, py - 1, pz, px + l, py - 1, pz + w, 5, 0)
        mc.setBlocks(px, py + h + 1, pz, px + l, py + h + 1, pz + w, 5, 0)

    px, py, pz = player.getPos()

    randx, randy, randz = find_surface(px, pz)
    print(randx, randy, randz)
    player.setPos(randx, randy + 1, randz)
