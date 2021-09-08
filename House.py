from mcpi.minecraft import Minecraft

class House:
    def __init__(self, x_lower, y_lower, z_lower, x_upper, y_upper, z_upper, block_id):
        self.x_lower = x_lower
        self.y_lower = y_lower
        self.z_lower = z_lower

        self.x_upper = x_upper
        self.y_upper = y_upper
        self.z_upper = z_upper

        self.block_id = block_id

        mc = Minecraft.create()

        mc.setBlocks(x_lower, y_lower, z_lower, x_upper, y_upper, z_upper, block_id)
        mc.setBlocks(x_lower+1, y_lower+1, z_lower+1, x_upper-1, y_upper-1, z_upper-1, 0)

        rooms = []




