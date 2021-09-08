from mcpi.minecraft import Minecraft
from House import House
import random

mc = Minecraft.create()
x, y, z = mc.player.getPos()



#this barely works 
brick = 46
air = 0
oak = 5
glass = 20

x = int(x)
y = int(y)
z = int(z)

house_length = 20
house_height = 5
house_width = 20



randX = random.randint(x, x+100)
randZ = random .randint(z, z+100)

mc.postToChat(randX)
mc.postToChat(randZ)


house1 = House(randX, y, randZ, randX + house_length, y + house_height, randZ + house_width, oak)

                    