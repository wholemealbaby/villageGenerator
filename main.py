from mcpi.minecraft import Minecraft
from random import randint
import numpy as np

mc = Minecraft.create()
player = mc.player

WALL_MATERIALS = [5, 17, 24, 98, 155, 159, 172, 179, 215, 251]
FLOOR_MATERIALS = [5, 24, 35, 100, 155, 159, 162, 179, 201, 251]
INVALID_REFERENCE_BLOCKS = [0, 1, 5, 7, 8, 9, 17, 18, ]


class Room:
    def __init__(self, x, y, z):
        # PROPERTIES
        width = random.randint(5, 12)  # x axis
        height = 5  # y axis
        length = random.randint(5, 12)  # z axis
        wallMaterial = WALL_MATERIALS[random.randint(0, len(WALL_MATERIALS) - 1)]
        floorMaterial = FLOOR_MATERIALS[random.randint(0, len(WALL_MATERIALS) - 1)]

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

def find_plot_reference_block():
    # List of blocks that aren't acceptable to build a village on
    block_coords = get_random_surface_block()
    block = mc.getBlock(block_coords[0], block_coords[1], block_coords[2])

    while block not in INVALID_REFERENCE_BLOCKS:
        block_coords = get_random_surface_block()
        block = mc.getBlock(block_coords[0], block_coords[1], block_coords[2])

    return block_coords


# Pass this function and x and z and it will find the surface of the world at that horizontal location
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


# returns the coordinates of a random surface block
def get_random_surface_block():
    player_x, player_y, player_z = player.getPos()
    rx = randint(int(player_x) - 3000, int(player_x) + 3000)
    rz = randint(int(player_z) - 3000, int(player_z) + 3000)
    return find_surface_y(rx, rz)


def count_blocks(blocks):
    block_counts = {}
    for block in blocks:
        if block in block_counts:
            block_counts[block] += 1
        else:
            block_counts[block] = 1
    return block_counts


# performs mc.getBlocks with coordinates in arrays for ease
def getBlocks_from_tuple(mc, tup1, tup2):
    mc.getBlocks(tup1[0], tup1[1], tup1[2], tup2[0], tup2[1], tup2[2])

# performs
def setBlocks_from_tuple(mc, tup1, tup2, id, dataid=0):
    mc.setBlocks(tup1[0], tup1[1], tup1[2], tup2[0], tup2[1], tup2[2], id, dataid)


def get_blocks_info(x0, y0, z0, x1, y1, z1):
    block_map = mc.getBlocks(x0, y0, z0, )


def cut_plot():
    # generating random X and Z values relative to the player within a 300block radius

    # randomly generated coordinates of a surface block
    # that will be the reference and start point of the plot
    ref_block = find_plot_reference_block()
    ref_x = ref_block[0]
    ref_y = ref_block[1]
    ref_z = ref_block[2]

    # checks a 100x100 block base plot for any air blocks
    # if there are any air blocks in the base plot then the base plot is unsuitable
    # this loops offsetting the y by -1 each loop until an acceptable base plot is found
    y_offset = 0
    found_valid_plot = False
    while found_valid_plot is False:

        # if the offset brings the y coordinate below 63 a new reference block is found
        if ref_y - y_offset < 60:
            print("Hit depth limit, finding new reference block")
            ref_block = find_plot_reference_block()
            ref_x = ref_block[0]
            ref_y = ref_block[1]
            ref_z = ref_block[2]
            continue

        blocks = mc.getBlocks(ref_x, ref_y - y_offset, ref_z, ref_x + 100, ref_y - y_offset, ref_z + 100)
        for block in blocks:
            found_valid_plot = True

            # base plot is invalid if it contains air or water blocks
            if block == 0 or block == 8 or block == 9:
                found_valid_plot = False
                print("Not a valid base, invalid plot")
                break
        y_offset += 1

    mc.setBlocks(ref_x, ref_y - y_offset, ref_z, ref_x + 100, ref_y, ref_z + 100, 2)
    mc.setBlocks(ref_x, (ref_y + 1 - y_offset), ref_z, ref_x + 100, ref_y + 20, ref_z + 100, 0)
    player.setPos(ref_x, ref_y + 1 - y_offset, ref_z)


# not functional
def stop_waterfalls(ref_block):
    boundary_ref_block = [(ref_block[0] - 1), ref_block[1] + 1, (ref_block[2] - 1)]
    boundary_ref_x = boundary_ref_block[0]
    boundary_ref_y = boundary_ref_block[1]
    boundary_ref_z = boundary_ref_block[2]

    boundary_blocks = get_boundary_blocks(boundary_ref_x, boundary_ref_y, boundary_ref_z)
    boundary_blocks_array = []

    for i in boundary_blocks:
        boundary_blocks_array = []

    blocks = np.array(boundary_blocks_array)
    blocks.reshape(102, 102)
    print(blocks)


# Returns map of block id's from 1 outside and 1 block above plot surface
def get_boundary_blocks(boundary_ref_x, boundary_ref_y, boundary_ref_z):
    return mc.getBlocks(boundary_ref_x, boundary_ref_y, boundary_ref_z, boundary_ref_x + 102, boundary_ref_y,
                        boundary_ref_z + 102)


if __name__ == "__main__":
    mc = Minecraft.create()
    player = mc.player

    WALL_MATERIALS = [5, 17, 24, 98, 155, 159, 172, 179, 215, 251]
    FLOOR_MATERIALS = [5, 24, 35, 100, 155, 159, 162, 179, 201, 251]

    px, py, pz = player.getPos()

    cut_plot()
