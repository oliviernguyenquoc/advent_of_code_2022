with open("./day4/input.txt") as f:
    instruction_list = f.read().splitlines()

result = 0

for instruction in instruction_list:
    # print(instruction)
    (pair1_str, pair2_str) = instruction.split(",")
    tuple1 = pair1_str.split("-")
    tuple2 = pair2_str.split("-")

    # Cast str to int
    tuple1 = (int(tuple1[0]), int(tuple1[1]))
    tuple2 = (int(tuple2[0]), int(tuple2[1]))

    if (tuple1[0] <= tuple2[0] and tuple1[1] >= tuple2[1]) or (
        tuple1[0] >= tuple2[0] and tuple1[1] <= tuple2[1]
    ):
        result += 1

print(result)