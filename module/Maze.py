'''Maze

===========================
'''

maze = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 1, 0],
]

for elem in maze:
    print(elem)

zip_maze = list(zip(*maze))

for elem in zip_maze:
    print(elem)

print(zip_maze)
print(maze)




right_way = 1
under_way = 1

for raw in maze:
    if (0, 1) in raw:
        print('1 if')
        right_way = 0
        for col in zip_maze:
            print('2cycle')
            if (0, 1) in col:
                print('2if')
                under_way = 0
            else:
                continue

            if right_way == 0 and under_way == 0:
                print('У лабиринта нет решения')
                break

    else:
        continue


