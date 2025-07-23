'''
Leftover Blocks
You have a number of building blocks that can be used to 
build a valid structure. There are certain rules about 
what determines a valid structure:

1. The building blocks are cubes.
2. The structure is built in layers.
3. The top layer is a single block.
4. A block in an upper layer must be supported by four blocks in a lower layer.
5. A block in a lower layer can support more than one block in an upper layer.
6. You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, 
calculates the number of blocks left over after building 
the tallest possible valid structure.

'''

############ PEDAC ##############

# Task 1 --> rules

# Input: number of blocks (integer)
# Output: number of leftover blocks after building tallest possible valid structure (integer)

# Explicit rules
# 1. The building blocks are cubes.
# 2. The structure is built in layers.
# 3. The top layer is a single block.
# 4. A block in an upper layer must be supported by four blocks in a lower layer.
# 5. A block in a lower layer can support more than one block in an upper layer.
# 6. You cannot leave gaps between blocks.


# Implicit rules
# 1. Starting with top block as layer 1, with layer numbers increasing moving
#    down toward bottom, number of blocks in each layer is the layer number squared:
# 
#    - top layer (layer 1) - 1 block
#    - layer 2 - 4 blocks
#    - layer 3 - 9 blocks
#.   - layer 4 - 16 blocks
#    - and so on

# Questions:
# 1. Will there always be leftover blocks?
# 2. Can more blocks be used per layer than the minimum of 4 per block in upper layer?


# Task 2 --> test cases

# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True

# Task 3 --> data structure

# Integers

# Task 4 --> algorithm

# 1. Initialize variables for keeping track of current layer and # of remaining available blocks after
#    building current layer.
#.     - current_layer = 1
#.     - available_blocks = starting number of blocks passed as argument to function
# 2. Starting with layer 1, calculate # blocks to construct current layer by 
#    squaring the layer number. Examples:
#       - layer 1:  blocks_for_layer = 1 ** 2 --> 1
#       - layer 2:  blocks_for_layer = 2 ** 2 --> 4
#       - layer 3:  blocks_for_layer = 3 ** 2 --> 9
# 3. Determine if there are enough available blocks to construct current layer by
#    subtracting number of blocks needed for current layer from total remaining available blocks.
#       - available_blocks - blocks_for_layer
# 4. If step 3 is >= 0, there are enough blocks to construct layer. Update available_blocks by subtracting
#    blocks_for_layer. If step 3 < 0, return available_blocks.
# 5. If a layer was constructed, increment current_layer by 1 and repeat steps for next layer.

# Task 5 --> code

def calculate_leftover_blocks(starting_blocks):

    current_layer = 1
    available_blocks = starting_blocks

    while True:
        blocks_for_layer = current_layer ** 2

        if available_blocks - blocks_for_layer >= 0:
            available_blocks -= blocks_for_layer
            current_layer += 1
        else:
            return available_blocks


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True