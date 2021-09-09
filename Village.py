from mcpi.minecraft import Minecraft
import random
from Road import Road

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
village_facing = random.choice(['north', 'east', 'south', 'west'])

# Set params for how much the road will wind
road_width = 4
road_length = 50  # TODO: Change this later according to how many houses spawn
road_winding_dist = 6

# Set params for how big the houses will be
house_length = random.randint(15, 20)  # Adjacent to road
house_width = random.randint(15, 20)  # Parallel to road
house_height = 7  # TODO: We can make this random later
# Define an array to store all House(s)
houses = []


# Clear area in front of player
def clear_area(facing, x, y, z, width_l, width_r, height, length):
    start_x, end_x, start_y, end_y, start_z, end_z = x, x, y, y + height - 1, z, z
    if facing == 'north':
        z -= 1
        start_x, start_z = x - width_l, z
        end_x, end_z = x + width_r, z - length + 1
    elif facing == 'east':
        x += 1
        start_x, start_z = x, z - width_l
        end_x, end_z = x + length - 1, z + width_r
    elif facing == 'south':
        z += 1
        start_x, start_z = x + width_l, z
        end_x, end_z = x-width_r, z + length - 1
    elif facing == 'west':
        x -= 1
        start_x, start_z = x, z + width_l
        end_x, end_z = x - length + 1, z - width_r

    mc.setBlocks(start_x, start_y, start_z, end_x, end_y, end_z, oak)

r1 = Road('north', player_x, player_y, player_z, 50, 4, 6, cobble)
r1.get_coords()

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
