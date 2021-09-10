from mcpi.minecraft import Minecraft
import random


def relative_movement(bearing, coords, instructions):
    x, y, z = coords[0], coords[1], coords[2]
    for i in instructions:
        direction = i[0]
        length = i[1]
        if direction == 'up':
            y += length
        elif direction == 'down':
            y -= length
        elif direction == 'left' or direction == 'right':
            if direction == 'right':
                length *= -1
            if bearing == 'north':
                x -= length
            elif bearing == 'east':
                z -= length
            elif bearing == 'south':
                x += length
            elif bearing == 'west':
                z += length
        elif direction == 'forward' or direction == 'back':
            if direction == 'back':
                length *= -1
            if bearing == 'north':
                z -= length
            elif bearing == 'east':
                x += length
            elif bearing == 'south':
                z += length
            elif bearing == 'west':
                x -= length
    return x, y, z

# Spawn road under x, y, z
class Road:
    def __init__(self, bearing, x, y, z, length, width, winding_dist, block):
        self.bearing = bearing
        self.x, self.y, self.z = x, y, z
        self.length, self.width = length, width - 1
        self.winding_dist = winding_dist
        self.block = block

        self.road_section = []
        # Init road_section with starting coords
        starting_coords = relative_movement(bearing, (self.x, self.y, self.z),
                                            [('down', 1)])
        self.road_section.append(starting_coords)

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
                    if curve == -1:
                        road_left = relative_movement(self.bearing, self.road_section[-1], [('forward', 1), ('left', 1)])
                        self.road_section.append(road_left)
                    elif curve == 0:
                        road_left = relative_movement(self.bearing, self.road_section[-1], [('forward', 1)])
                        self.road_section.append(road_left)
                    elif curve == 1:
                        road_left = relative_movement(self.bearing, self.road_section[-1], [('forward', 1), ('right', 1)])
                        self.road_section.append(road_left)

        for coords in self.road_section:
            road_left = coords
            road_right = relative_movement(self.bearing, road_left, [('right', self.width)])
            self.mc.setBlocks(road_left, road_right, block)

    def get_coords(self):
        for i in self.road_section:
            print(i)
        return self.road_section
