map = []
def Creation(size,choice):
    import random
    size = size.split("x")
    rows = int(size[0])
    cols = int(size[1])
    line = []
    for i in range(cols):
        line.append("️⬜️")
    for i in range(rows):
        map.append(list(line))

    print("Hiding your treasure! X marks the spot.")
    if(choice.lower() == "burry"):
        position = input("Where do you want to put the treasure? (eg A1 or B2) where A is the row and 1 is the column\n")
        position = list(position)
        row = ord(position[0].upper()) - 65
        print(row)
        col = int(position[1]) - 1
        print(col)
        map[row][col] = "X"
    else:
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-1)
        map[row][col] = "X"

    print("Treasure Map Created!")

def print_map(map):
    for i in range(len(map)):
        print(map[i])

if __name__ == "__main__":
    size = input("Enter the Size of Treasure Map (eg 1x1, 3x3, 4x5 or 9x9 ....) \n")
    choice = input("You want to burry the treasure yourself or want the treasure to Spawn itself ?(burry or spawn)\n")
    Creation(size,choice)
    