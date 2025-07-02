from typing import List
from math import prod

def feet_of_ribbon(*sides: List[int]) -> int:
    shortest_distance_sides = sorted(sides)
    perimeter_of_one_face = 2 * (shortest_distance_sides[0]+shortest_distance_sides[1])
    ribbon_for_bow = prod(shortest_distance_sides)
    return perimeter_of_one_face + ribbon_for_bow


with open('input.txt') as dims:
    dimensions = [dim.strip('\n') for dim in dims]
    total_feet_of_ribbon = 0
    for dim in dimensions:
        length, width, height = map(int, dim.split('x'))
        total_feet_of_ribbon += feet_of_ribbon(length, width, height)
    print(total_feet_of_ribbon)
    