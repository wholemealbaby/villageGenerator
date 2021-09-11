from mcpi.minecraft import Minecraft
from Road import Road
import random


def main():
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


    r1 = Road('south', player_x, player_y, player_z, 50, 4, 6, cobble)
    print(player_x, player_y, player_z)
    r1.get_coords()

main()



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
