def get_adjacent(matrix, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adjacent = []
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            adjacent.append((r,c))
    return adjacent