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

        # Create a box of block material 'block_id'
        mc.setBlocks(x_lower, y_lower, z_lower, x_upper, y_upper, z_upper, block_id)
        # Hollow out the inside
        mc.setBlocks(x_lower + 1, y_lower + 1, z_lower + 1, x_upper - 1, y_upper - 1, z_upper - 1, 0)

        # Add front door of house (with coordinate selection)
        door_width = 4
        door_height = 4
        door_offset = 3
        mc.setBlocks(x_lower + door_offset - 1, y_lower + 1, z_lower,
                     x_lower + door_offset + door_width - 2, y_lower + door_height, z_lower, 0)
        # mc.postToChat(x_lower+door_offset)
        # mc.postToChat(y_lower+1)
        # mc.postToChat(z_lower)
        # mc.postToChat(x_lower+door_offset+door_width)
        # mc.postToChat(y_lower+1+door_height)
        # mc.postToChat(z_lower)




        # Add windows to house
        window_width = 2
        window_height = 2



        rooms = []
