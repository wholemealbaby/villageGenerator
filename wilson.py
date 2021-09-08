from mcpi.minecraft import Minecraft
from House import House

mc = Minecraft.create()
x, y, z = mc.player.getPos()

brick = 46
air = 0
oak = 5
glass = 20


def create_house(length=8, width=10, height=5):
    # Makes a rectangle
    for i in range(length):
        for j in range(width):
            for k in range(height):
                if k == 0 or k == height - 1:
                    mc.setBlock(x + i, y + k, z + j, oak)
                elif i == 0 or i == length - 1:
                    mc.setBlock(x + i, y + k, z + j, oak)
                elif j == 0 or j == width - 1:
                    mc.setBlock(x + i, y + k, z + j, oak)
                else:
                    mc.setBlock(x + i, y + k, z + j, air)


house_length = 15
house_height = 5
house_width = 15

mc.postToChat(x)
mc.postToChat(y)
mc.postToChat(z)

house1 = House(x, y, z, x + house_length, y + house_height, z + house_width, oak)

# create_house()
