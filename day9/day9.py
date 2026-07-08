data = open("./day9/input.txt", "r").read().splitlines()

def data_setup(data):
    cleaned_data = []
    for line in data:
        cleaned_data.append([int(x) for x in line.split(",")])
    return cleaned_data

def get_area(p1, p2):
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height

def create_edge_set(points):
    point_count = len(points)
    horizontal_edges = []
    vertical_edges = []

    for i in range(point_count):
        # create edges between points and store them in a list to represent the edges of the shape formed by the points.
        p1, p2 = points[i], points[(i + 1) % point_count]  # Wrap around to connect last point to first point

        min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
        min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])

        if p1[0] == p2[0]: # Vertical line
            x = min_x # min_x same as max_x  
            vertical_edges.append((x, min_y, max_y)) # Vertical Line (position, lower bound, upper bound, orientation)
        else: # Horizontal line
            y = min_y # min_y same as max_y
            horizontal_edges.append((y, min_x, max_x)) # Horizontal Line (position, lower bound, upper bound, orientation)

    return sorted(horizontal_edges, key=lambda x: x[0]), sorted(vertical_edges, key=lambda x: x[0])

def create_corner_pairs(cleaned_data):
    corner_pairs = []

    for i in range(len(cleaned_data)):
        for j in range(i + 1, len(cleaned_data)):
            current_area = get_area(cleaned_data[i], cleaned_data[j])
            
            corner_pair = (cleaned_data[i], cleaned_data[j], current_area)
            corner_pairs.append(corner_pair)
    
    return sorted(corner_pairs, key=lambda x: x[2], reverse=True)


def get_rect_corners_inside(corner_pair):
    # Create the four corners of the rectangle formed by the corner pair.
    # p1-----p2
    # |xxxxxx|
    # |xxxxxx|
    # p4-----p3
    
    min_x = min(corner_pair[0][0], corner_pair[1][0])
    max_x = max(corner_pair[0][0], corner_pair[1][0])
    min_y = min(corner_pair[0][1], corner_pair[1][1])
    max_y = max(corner_pair[0][1], corner_pair[1][1])
    # To get the inside edges, we need to move the corners inward by 1 unit.
    p1, p2, p3, p4 = (min_x + 1, min_y + 1), (max_x - 1, min_y + 1), (max_x - 1, max_y - 1), (min_x + 1, max_y - 1)
    return p1, p2, p3, p4


def create_rect_edges(corner_pair):
    p1, p2, p3, p4 = get_rect_corners_inside(corner_pair)
    horizontal_edges, vertical_edges = create_edge_set((p1, p2, p3, p4))
    return horizontal_edges, vertical_edges


def check_rectangle_edges(corner_pair, horizontal_edges_polygon, vertical_edges_polygon):
    horizontal_edges_rect, vertical_edges_rect = create_rect_edges(corner_pair)

    # Check if the rectangle edges intersect with the polygon edges.
    # check horizontal edges of the rectangle against vertical edges of the polygon
    for horizontal_edge_rect in horizontal_edges_rect:
        for vertical_edge_polygon in vertical_edges_polygon:
            if horizontal_edge_rect[1] <= vertical_edge_polygon[0] <= horizontal_edge_rect[2] and vertical_edge_polygon[1] <= horizontal_edge_rect[0] <= vertical_edge_polygon[2]:
                return False  # Intersection found, rectangle is not valid


    # check vertical edges of the rectangle against horizontal edges of the polygon
    for vertical_edge_rect in vertical_edges_rect:
        for horizontal_edge_polygon in horizontal_edges_polygon:
            if vertical_edge_rect[1] <= horizontal_edge_polygon[0] <= vertical_edge_rect[2] and horizontal_edge_polygon[1] <= vertical_edge_rect[0] <= horizontal_edge_polygon[2]:
                return False  # Intersection found, rectangle is not valid
            
    return True  # No intersections found, rectangle is valid



def is_inside_shape( x, y, edges):
    # same technique as in raytracing, count the number of intersections with the edges of the shape. If the count is odd, the point is inside; if even, it's outside.
    intersection_count = 0

    for edge_x, min_y, max_y in edges:
        if x <= edge_x and min_y <= y <= max_y:
            intersection_count += 1


    return intersection_count % 2 == 1  # True if inside, False if outside


def part1(data):
    max_area = 0
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            current_area = get_area(data[i], data[j])
            
            if current_area > max_area:
                max_area = current_area
                
    print("Part 1:", max_area)
    return max_area


def part2(data):
    horizontal_edges, vertical_edges = create_edge_set(data)
    corner_pairs = create_corner_pairs(data)

    for pair in corner_pairs:
        checked = check_rectangle_edges(pair, horizontal_edges, vertical_edges)
        if not checked:
            #print(f"Rectangle edges intersect with polygon edges for pair: {pair}")
            continue  # Skip this pair if the rectangle edges intersect with the polygon edges

        corners = get_rect_corners_inside(pair)
        is_inside = is_inside_shape(corners[0][0], corners[0][1],  vertical_edges)
        
        # print("checked pair" + str(pair))
        if is_inside:
            print(f"Is inside: {is_inside}")
            area = get_area(pair[0], pair[1])
            print(f"Area: {area}")
            return area



cleaned_data = data_setup(data)
part1(cleaned_data)
part2(cleaned_data)