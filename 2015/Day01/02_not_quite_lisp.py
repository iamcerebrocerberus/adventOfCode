def find_first_char_to_basement(puzzle_input: str) -> int:
    with open(puzzle_input, 'r') as directions:
        floor_number = 0
        for position, floor_direction in enumerate(directions.read(), 1):
            floor_number += 1 if floor_direction == '(' else -1
            if floor_number == -1:
                return position

    
print(find_first_char_to_basement('puzzle_input.txt'))