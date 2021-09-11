from mcpi.minecraft import Minecraft


class House:
    def __init__(self, bearing, x, y, z, width, height, length, walls, roof):
        self.bearing = bearing
        self.x, self.y, self.z = x, y, z
        self.x_end, self.y_end, self.z_end = x, y, z
        self.width = width
        self.height = height
        self.length = length
        self.walls, self.roof = walls, roof

        oak = 5
        glass = 20
        brick = 45

        self.mc = Minecraft.create()
        # Generate walls
        self.generate_block(bearing, x, y, z, width, height, length, walls)
        # Hollow out inside
        self.hollow_block(bearing, x, y, z, width, height, length)
        # Generate roof
        self.generate_block(bearing, x, y + height - 1, z, width, 1, length, roof)
        # Generate door
        self.add_door(bearing, x, y, z)
        # Generate window
        self.add_window(bearing, x, y, z)

    def generate_block(self, bearing, x, y, z, width, height, length, block):
        if bearing == 'north' or bearing == 'west':
            length = -length + 1
        if bearing == 'south' or bearing == 'west':
            width = -width + 1
        if bearing == 'north' or bearing == 'east':
            width -= 1
        if bearing == 'east' or bearing == 'south':
            length -= 1

        # Make a rectangular cuboid of block
        if bearing == 'north' or bearing == 'south':
            x_end, y_end, z_end = x + width, y + height - 1, z + length
            self.mc.setBlocks(x, y, z, x_end, y_end, z_end, block)
        elif bearing == 'east' or bearing == 'west':
            x_end, y_end, z_end = x + length, y + height - 1, z + width
            self.mc.setBlocks(x, y, z, x_end, y_end, z_end, block)

    def hollow_block(self, bearing, x, y, z, width, height, length):
        y += 1
        width -= 2
        height -= 2
        length -= 2
        if bearing == 'north' or bearing == 'east':
            x += 1
        if bearing == 'south' or bearing == 'west':
            x -= 1
        if bearing == 'north' or bearing == 'west':
            z -= 1
        if bearing == 'east' or bearing == 'south':
            z += 1

        self.generate_block(bearing, x, y, z, width, height, length, 0)

    # Will be utilising fixed positions for now (4 wide 3 high)
    def add_door(self, bearing, x, y, z):
        y += 1
        if bearing == 'north':
            x += 3
        elif bearing == 'south':
            x -= 3
        elif bearing == 'east':
            z += 3
        elif bearing == 'west':
            z -= 3
        self.generate_block(bearing, x, y, z, 4, 3, 1, 0)

    # Will be utilising fixed positions for now (2 wide 2 high)
    def add_window(self, bearing, x, y, z):
        y += 2
        if bearing == 'north':
            x += 10
        elif bearing == 'south':
            x -= 10
        elif bearing == 'east':
            z += 10
        elif bearing == 'west':
            z -= 10
        self.generate_block(bearing, x, y, z, 2, 2, 1, 20)

