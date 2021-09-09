from mcpi.minecraft import Minecraft
import random


def relative_movement(bearing, coords, direction, length):
    x, y, z = int(coords[0]), int(coords[1]), int(coords[2])
    if direction == 'up':
        return x, y + length, z
    elif direction == 'down':
        return x, y - length, z
    elif direction == 'left' or direction == 'right':
        if direction == 'right':
            length *= -1
        if bearing == 'north':
            return x - length, y, z
        elif bearing == 'east':
            return x, y, z - length
        elif bearing == 'south':
            return x + length, y, z
        elif bearing == 'west':
            return x, y, z + length
    elif direction == 'forward' or direction == 'back':
        if direction == 'back':
            length *= -1
        if bearing == 'north':
            return x, y, z - length
        elif bearing == 'east':
            return x + length, y, z
        elif bearing == 'south':
            return x, y, z + length
        elif bearing == 'west':
            return x - length, y, z


class Road:
    def __init__(self, bearing, x, y, z, length, width, winding_dist, block):
        x, y, z = int(x), int(y), int(z)
        self.bearing = bearing
        self.x, self.y, self.z = x, y, z
        self.length, self.width = length, width - 1
        self.winding_dist = winding_dist
        self.block = block

        self.road_section = []
        # Init road_section with starting coords
        self.road_section.append(
            [(x, y, z), (relative_movement(bearing, (self.x, self.y, self.z), 'right', self.width))])

        self.mc = Minecraft.create()

        cur_curve = 0
        for i in range(length - 1):
            valid_bounds = False
            while not valid_bounds:
                # Pick if path curves left or right randomly (with heavy weighting -> 80% towards straight path (0),
                # 10% to left (-1) and 10% to right (1)
                curve = random.choice([-1] * 1 + [0] * 8 + [1] * 1)
                if -self.winding_dist <= cur_curve + curve <= self.winding_dist:
                    valid_bounds = True
                    new_base_coord = relative_movement(self.bearing, self.road_section[-1][0], 'forward', 1)
                    if curve == -1:
                        new_base_coord = relative_movement(self.bearing, new_base_coord, 'left', 1)
                    elif curve == 1:
                        new_base_coord = relative_movement(self.bearing, new_base_coord, 'right', 1)
                    self.road_section.append(
                        [new_base_coord, (relative_movement(bearing, new_base_coord, 'right', self.width))])

        for coords in self.road_section:
            print(coords[0], coords[1])
            self.mc.setBlocks(coords[0], coords[1], block)

    def get_coords(self):
        return self.road_section
