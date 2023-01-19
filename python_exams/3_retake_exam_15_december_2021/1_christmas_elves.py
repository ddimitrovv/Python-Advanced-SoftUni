# Everything in the Santa Claus' workshop was going well until, on one freezing Sunday,
# a dangerous storm destroyed almost all toys. Now Santa's elves fear they won't be able
# to meet their December deadline. It could be a disaster, and some children around the world
# may not get their Christmas toys. Luckily, you've come up with an idea,
# and you just need to write a program that manages your plan.
# The Christmas elves have special toy-making skills - each elf can make a toy from a given number of materials.
# First, you will receive a sequence of integers representing each elf's energy.
# On the following line, you will be given another sequence of integers,
# each representing a number of materials in a box.
# Your task is to calculate the total elves' energy used for making toys and the total number
# of successfully made toys.
# You are very clever and have immediately recognized the pros and cons of the work process -
# the first elf takes the last box of materials and tries to create the toy:
#     • Usually, the elf needs energy equal to the number of materials.
#       If he has enough energy, he makes the toy. His energy decreases by the used energy,
#       and the toy goes straight to Santa's bag. Then, the elf eats a cookie reward
#       which increases his energy by 1, and goes to the end of the line, preparing for the upcoming boxes.
#     • Every third time one of the elves takes a box, he tries his best to be creative,
#       and he will need twice as much energy as usual. If he has enough, he manages to create 2 toys.
#       Then, his energy decreases; he eats a cookie reward and goes to the end of the line,
#       similar to the first bullet.
#     • Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages
#       to break the toy when he just made it (if he made it). The toy is thrown away,
#       and the elf doesn't get a cookie reward. However, his energy is already spent,
#       and it needs to be added to the total elves' energy.
#         ◦ If an elf creates 2 toys, but he is clumsy, he breaks them.
#     • If an elf does not have enough energy, he leaves the box of materials to the next elf.
#       Instead of making the toy, the elf drinks a hot chocolate which doubles his energy,
#       and goes to the end of the line, preparing for the upcoming boxes.
# Note: North Pole's social policy is very tolerant of the elves.
#       If the current elf's energy is less than 5 units, he does NOT TAKE a box, but he takes a day off.
#       Remove the elf from the collection.
#       Stop crafting toys when you are out of materials or elves.
# Input
#     • The first line of input will represent each elf's energy - integers, separated by a single space
#     • On the second line, you will be given the number of materials in each box -
#       integers, separated by a single space
# Output
#     • On the first line, print the number of created toys: "Toys: {total_number_of_toys}"
#     • On the second line, print the total used energy: "Energy: {total_used_energy}"
#     • On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:
#         ◦ "Elves left: {elf1}, {elf2}, … {elfN}"
#         ◦ "Boxes left: {box1}, {box2}, … {boxN}"
# Constraints
#     • All the elves' values will be integers in the range [1, 100]
#     • All the boxes' values will be integers in the range [1, 100]

from collections import deque

elves_energy = deque(int(x) for x in input().split())
materials_box = [int(x) for x in input().split()]
crafted_gifts = 0
elf_turns = 0
used_energy = 0
while elves_energy and materials_box:

    elf = elves_energy.popleft()

    if elf < 5:
        continue

    elf_turns += 1
    current_toys = 0

    materials = materials_box.pop()

    if elf < materials:
        materials_box.append(materials)
        elves_energy.append(elf * 2)
        continue
    if elf_turns % 3 == 0 and elf < materials * 2:
        materials_box.append(materials)
        elves_energy.append(elf * 2)
        continue

    if elf_turns % 3 == 0 and elf >= materials * 2:
        current_toys += 2
        if elf_turns % 5 == 0:
            elf -= 1
        elf -= materials * 2 - 1
        used_energy += materials * 2

    if elf_turns % 3 != 0:
        current_toys += 1
        if elf_turns % 5 == 0:
            elf -= 1
        elf -= materials - 1
        used_energy += materials

    if elf_turns % 5 != 0:
        crafted_gifts += current_toys

    elves_energy.append(elf)


print(f'Toys: {crafted_gifts}')
print(f'Energy: {used_energy}')
if elves_energy:
    print(f'Elves left: {", ".join(str(x) for x in elves_energy)}')
if materials_box:
    print(f'Boxes left: {", ".join(str(x) for x in materials_box)}')
