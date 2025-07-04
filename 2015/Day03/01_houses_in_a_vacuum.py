from typing import Tuple

def santas_new_location(x_cordinate: int, y_cordinate: int, direction: str) -> Tuple[int, int]:
    if direction == '>':
        x_cordinate += 1
    elif direction == '<':
        x_cordinate -= 1
    elif direction == '^':
        y_cordinate += 1
    elif direction == 'v':
        y_cordinate -= 1
    return (x_cordinate, y_cordinate)


# since we are using a 2D dimenstion, we have x and y cordination
# and this means santas starting point is x = 0, y = 0 which maps to (0, 0)
x = 0
y = 0
santas_location = (x, y)
houses = {santas_location}
with open('input.txt') as moves:
    for direction in moves.read():
        x, y = santas_new_location(x, y, direction)
        houses.add((x, y))        
    print(len(houses))
        


