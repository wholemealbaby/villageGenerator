from mcpi.minecraft import Minecraft

mc = Minecraft.create()
player = mc.player


def buildHouse(l,h,w):
    px, py, pz = player.getPos()

    px, py, pz = int(px), int(py), int(pz)
    px+=2

    # Walls
    mc.setBlocks(px, py, pz, px, py+h, pz+w, 45)
    mc.setBlocks(px, py, pz, px+l, py+h, pz, 45)
    mc.setBlocks(px+l, py, pz, px+l, py+h, pz+w, 45)
    mc.setBlocks(px, py, pz+w, px+l, py+h, pz+w, 45)

    #roof and floor


buildHouse(8,5,8)




