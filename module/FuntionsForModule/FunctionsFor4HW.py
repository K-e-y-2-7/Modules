def get_distance_matrix(w):
    distance_matrix = {}
    for wall_row in w:
        key = 0

        for brick_length in wall_row[:-1]:
            key += brick_length

            if key in distance_matrix:
                distance_matrix[key] += 1     
            else:
                distance_matrix[key] = 1
    
    return distance_matrix


def get_min_joints_distance(d):
    min_joints = min(d.values())
    min_values = []
    for distance, joints_count in d.items():
        if joints_count == min_joints:
            min_values.append(distance)
        else:
            pass
    min_values.sort()
    return min_values
    