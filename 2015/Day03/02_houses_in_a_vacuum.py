from typing import Tuple

def find_new_location(x_coordinate: int, y_coordinate: int, direction: str) -> Tuple[int, int]:
    if direction == '>':
        x_coordinate += 1
    elif direction == '<':
        x_coordinate -= 1
    elif direction == '^':
        y_coordinate += 1
    elif direction == 'v':
        y_coordinate -= 1
    return (x_coordinate, y_coordinate)


# x and y cordinates for santa and robo santa
santa_x ,santa_y = 0, 0
robosanta_x ,robosanta_y = 0, 0

# both santa and robosanta start at same point
houses = {(0, 0)}

with open('input.txt') as moves:
    for pos, direction in enumerate(moves.read(), 1):
        if pos % 2 != 0:
            santa_x, santa_y = find_new_location(santa_x, santa_y, direction)
            houses.add((santa_x, santa_y))
        else:
            robosanta_x, robosanta_y = find_new_location(robosanta_x, robosanta_y, direction)
            houses.add((robosanta_x, robosanta_y))
    print(len(houses))
        