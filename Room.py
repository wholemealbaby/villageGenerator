
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

 
mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()

FLOOR_MATERIALS = [block.STONE, block.COBBLESTONE, block.WOOD]
WALL_MATERIALS = [block.BRICK_BLOCK, block.SANDSTONE, block.WOOD_PLANKS]
STAIR_MATERIALS = [block.STAIRS_STONE_BRICK, block.STAIRS_WOOD]



houseFloor = FLOOR_MATERIALS[random.randint(0, len(FLOOR_MATERIALS)-1)]
houseWall = WALL_MATERIALS[random.randint(0, len(WALL_MATERIALS)-1)]

#makes sure stairs semi matches the floor
if houseFloor == block.STONE or houseFloor == block.COBBLESTONE:
    houseStairs = STAIR_MATERIALS[0]
else:
    houseStairs = STAIR_MATERIALS[1]


class House:
    def __init__(self) -> None:
        pass
    def createHouse(x, y, z):
        #hallway
        mc.setBlocks(x+2, y, z-2, x+8, y+4, z+2, houseWall) #solid cube
        mc.setBlocks(x+3, y+1, z-1, x+7, y+3, z+1, block.AIR) #empty inside
        mc.setBlocks(x+2, y+1, z, x+2, y+2, z, block.AIR) #doorway
        mc.setBlocks(x+2, y, z-2, x+8, y, z+2, houseFloor) #make floor dif mat
        mc.setBlocks(x+1, y, z-1, x+1, y, z+1, houseFloor) #front door porch
        mc.setBlocks(x, y, z-1, x, y, z+1, houseStairs, 3) #front door stairs

        numRooms = random.randint(1, 4)

        House.createRoom()
    

    def createRoom():

        possiblePos = ["TopL","TopR","BottomL","BottomR"]
        y1 = y
        
        #for 5 x 5 rooms (inside space of 3x3)
        ROOM_SIDE = 4
        ROOM_HEIGHT = 4
        numRooms = random.randint(1,4)

        for i in range(numRooms):
            roomPos = possiblePos[(random.randint(0, len(possiblePos) - 1))]
  
            if roomPos == "TopL":
                x1 = x + 5
                z1 = z - 6
            elif roomPos == "TopR":
                x1 = x + 5
                z1 = z + 2
            elif roomPos == "BottomL":
                x1 = x + 1
                z1 = z - 6
            elif roomPos == "BottomR":
                x1 = x + 1
                z1 = z + 2
            else:
                break

            #just flips doorway position to ensure connects to hallway. Probably better way to do this

            if roomPos == "TopL" or roomPos ==  "BottomL":
                mc.setBlocks(x1,y1,z1, x1+ROOM_SIDE, y1+ROOM_HEIGHT, z1 + ROOM_SIDE, houseWall)
                mc.setBlocks(x1 + 1,y1 + 1,z1 + 1, x1+ROOM_SIDE -1, y1+ROOM_HEIGHT -1, z1 + ROOM_SIDE - 1, block.AIR)
                mc.setBlocks(x1+ (ROOM_SIDE / 2), y1+1, z1+ROOM_SIDE,x1+ (ROOM_SIDE / 2), y1+2, z1+ROOM_SIDE, block.AIR )
                mc.setBlocks(x1,y1,z1, x1+ROOM_SIDE, y1, z1 + ROOM_SIDE, houseFloor)
            else:
                mc.setBlocks(x1,y1,z1, x1+ROOM_SIDE, y1+ROOM_HEIGHT, z1 + ROOM_SIDE, houseWall)
                mc.setBlocks(x1 + 1,y1 + 1,z1 + 1, x1+ROOM_SIDE -1, y1+ROOM_HEIGHT -1, z1 + ROOM_SIDE - 1, block.AIR)
                mc.setBlocks(x1+ (ROOM_SIDE / 2), y1+1, z1,x1+ (ROOM_SIDE / 2), y1+2, z1, block.AIR )
                mc.setBlocks(x1,y1,z1, x1+ROOM_SIDE, y1, z1 + ROOM_SIDE, houseFloor)


House.createHouse(x,y,z)


