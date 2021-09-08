from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getPos()




mc.setBlocks((x-100), 3, (z-100), (x + 100), (y + 50), (z + 100), 0)

        