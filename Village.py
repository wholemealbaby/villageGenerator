from mcpi.minecraft import Minecraft
from Road import Road
import random
import randGenHouse


class Village():
    # Block IDs
    air = 0
    cobble = 4
    oak = 5
    gravel = 14
    glass = 20
    brick = 45
    tnt = 46

    # Create instance on minecraft
    mc = Minecraft.create()

    # Find current coords of player
    player_x, player_y, player_z = mc.player.getPos()
    # Decide which direction the village will be facing

    # Set params for how much the road will wind
    ROAD_WIDTH = 4
    ROAD_LENGTH = 50  # TODO: Change this later according to how many houses spawn
    ROAD_WINDING_DIST = 6

    # Set params for how big the houses will be
    house_length = random.randint(15, 20)  # Adjacent to road
    house_width = random.randint(15, 20)  # Parallel to road
    house_height = 7  # TODO: We can make this random later
    # Define an array to store all House(s)
    houses = []

    # r1 = Road('south', player_x, player_y, player_z, 50, 4, 6, cobble)
    # print(player_x, player_y, player_z)
    # r1.get_coords()

    def __int__(self):
        # Direction village is facing - @wilson not sure why we need this but ill keep it here
        self.face = random.choice(['north', 'east', 'south', 'west'])

        # House generation
        self.num_houses = random.randint(3, 13)
        self.houses = []
        for i in range(self.num_houses):
            self.houses.append(randGenHouse)






# clear_area('west', player_x, player_y, player_z, 5, 7, 3, 10)


# First we generate a direction the village is facing randomly (e.g., north, east, south, west) and cut out a chunk


# We make the assumption


# Then generate houses carefully with an offset based on direction the road is expected to travel


# Then we generate rooms


# Then we generate roads


# And then we connect these roads


# Generate a road
# left and right 6 blocks

# house_length = 20
# house_height = 7
# house_width = 20
#
# house1 = House('east', x, y, z, house_width, house_height, house_length, oak, brick)
