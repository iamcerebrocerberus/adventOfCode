def find_floor_number(puzzle_input: str) -> int:
    with open(puzzle_input, 'r') as directions:
        floor_number = 0
        for floor_direction in directions.read():
            floor_number += 1 if floor_direction == '(' else -1
    return floor_number
    
print(find_floor_number('puzzle_input.txt'))