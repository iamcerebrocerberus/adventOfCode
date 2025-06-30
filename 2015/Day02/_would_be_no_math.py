def surface_area_of_box(length: int, width: int, height: int, /) -> int:
    little_extra_paper = min(length*width , width*height, height*length)
    surface_area = 2*length*width + 2*width*height + 2*height*length
    return surface_area + little_extra_paper

with open('input.txt') as dims:
    dimensions = [dim.strip('\n') for dim in dims]
    total_square_feet = 0
    for dim in dimensions:
        length, width, height = map(int, dim.split('x'))
        total_square_feet += surface_area_of_box(length, width, height)
    print(total_square_feet)