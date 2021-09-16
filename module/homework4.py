from FuntionsForModule import INTexam
from FuntionsForModule import FunctionsFor4HW
import pathlib

print('Скрипт с кирпичной стеной')

profile_path = pathlib.Path('profile.txt')
profile_path.absolute()
with open(profile_path, 'r') as profile:
        user_name = profile.readline()

print('Привет,' + user_name + '!!!')

Number_of_rows_in_the_wall = (input('Введите количество рядов в стене:'))
Number_of_rows_in_the_wall = INTexam.exam(Number_of_rows_in_the_wall)
Number_of_rows_in_the_wall = list(range(1,Number_of_rows_in_the_wall+1))


wall, wall_print, bricks_length  = [], [], []
for number in Number_of_rows_in_the_wall:
    Number_of_bricks = (input('Введите количество кирпичей в ряду: '))
    Number_of_bricks = INTexam.exam(Number_of_bricks)
    Number_of_bricks_list = list(range(1, Number_of_bricks + 1))
    
    row_of_brick, row_of_brick_print, brick_whole_length =[], [], []
    for bricks in Number_of_bricks_list:
        brick_length = (input('Введите длинну кирпича: '))
        brick_length = INTexam.exam(brick_length)
        brick_whole_length.append(brick_length+2)
        brick = '|' + '_' * (brick_length) + '|'
        row_of_brick.append(brick_length)
        row_of_brick_print.append(brick)
    
    wall.append(row_of_brick)
    wall_print.append(row_of_brick_print)
    brick_whole_length = sum(brick_whole_length)
    bricks_length.append(brick_whole_length)

number_for_cycle = 0  
for row_of_brick in wall:
    print (wall[number_for_cycle],)
    number_for_cycle += 1

distance_matrix = FunctionsFor4HW.get_distance_matrix(wall)
conclusion = FunctionsFor4HW.get_min_joints_distance(distance_matrix)

print(distance_matrix)
print (conclusion, 'Точка(-и), в которой(-рых) линия пересекает наименьшее количество кирпичей')

highest = (max(bricks_length) + 2)
resoult = int((highest - bricks_length[0]) / 2)
up_down_edge = '+' + '-' * (highest) + '+'
roof, down = '|' + ' ' * resoult + '_' * bricks_length[0]  + ' ' * resoult + '|', '|' + ' ' * highest + '|'

print(up_down_edge)
print(roof)

number_for_cycle4 = 0
for row_of_brick in wall_print:
    row1 = ''.join(row_of_brick)
    resoult = int((highest - bricks_length[number_for_cycle4]) / 2)
    left_edge, right_edge  = '|' + ' ' * (resoult - 1) , ' ' * (resoult - 1) + '|'
    print (left_edge, row1, right_edge)
    number_for_cycle4 += 1
print (down)
print (up_down_edge)
