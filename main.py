def solve_rovers(input_text):
    lines = input_text.strip().split("\n")
    max_x, max_y = map(int, lines[0].split())

    directions = ["N", "E", "S", "W"]

    moves = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0)
    }

    results = []
    i = 1

    while i < len(lines):
        x, y, facing = lines[i].split()
        x = int(x)
        y = int(y)

        instructions = lines[i + 1]
        i += 2

        for command in instructions:
            if command == "L":
                current_index = directions.index(facing)
                facing = directions[(current_index - 1) % 4]

            elif command == "R":
                current_index = directions.index(facing)
                facing = directions[(current_index + 1) % 4]

            elif command == "M":
                dx, dy = moves[facing]
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x <= max_x:
                    x = new_x
                if 0 <= new_y <= max_y:
                    y = new_y

        results.append(f"{x} {y} {facing}")

    return "\n".join(results)


input_data = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""

print(solve_rovers(input_data))