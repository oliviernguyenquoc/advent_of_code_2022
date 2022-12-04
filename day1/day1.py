with open("./day1/input.txt") as f:
    instruction_list = f.read().splitlines()

max_weight: int = 0
current_elf_weight: int = 0
for instruction in instruction_list:
    if instruction != "":
        current_elf_weight += int(instruction)
    else:
        if max_weight < current_elf_weight:
            max_weight = current_elf_weight
        current_elf_weight = 0

print(max_weight)
