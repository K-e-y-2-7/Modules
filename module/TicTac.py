print('Крестики-Нолики')
import pathlib
from FuntionsForModule import INTexam
import random
from FuntionsForModule import wincombinations
from FuntionsForModule import profile1
print('Привет,' + profile1.user_name + '!!!')

player1 = input('Игрок № 1. Введите ваше имя: ')
player2 = input('Игрок № 2. Введите ваше имя: ')

way_to_directory = str(pathlib.Path(__file__).parent.absolute())

last_games_results = [] 
with open(way_to_directory + '\Results.txt', 'r') as file:
    for line in file:
        last_games_results.append(line)

for elem in last_games_results:
    print(elem)

while True:
    

    team_O, team_X = 1, 2

    random_number_list = [random.randint(1, 2) for r in range(1,2)]
    random_number = random_number_list[0]

    print(random_number_list)
    print('''
        +===========+
        | 1 | 2 | 3 |
        |---+---+---|
        | 4 | 5 | 6 |
        |---+---+---|
        | 7 | 8 | 9 |
        +===========+
    ''')

   
    if random_number == 1:
        team_O, team_X = player1, player2
    else:
        team_X, team_O = player1, player2

    print(team_O, ' играет ноликами.')
    print(team_X, ' играет крестиками.')

    box_team_O, box_team_X  = [], []
    cells = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',

    } 

    cell_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def examination(user_input: int):
        n = 0
        while n < 1:
            if user_input in cell_number:
                cell_number.remove(user_input)
                n += 1
            else:
                user_input = int(input('Эта ячейка уже занята. Выберите другую:'))
    
        return user_input
    
    i, o, x = 0, 0, 0
    while i < 9:  
        if i % 2 == 0:
            team_O_choice = input(team_O + ', запишите номер ячейки для записи "О": ')
            team_O_choice = INTexam.exam(team_O_choice)
            team_O_choice = examination(team_O_choice)
            box_team_O.append(team_O_choice)
            box_team_O = list(map(str, box_team_O))
            box_team_O.sort()

        else:
            team_X_choice = input(team_X + ', запишите номер ячейки для записи "Х": ')
            team_X_choice = INTexam.exam(team_X_choice)
            team_X_choice = examination(team_X_choice)
            box_team_X.append(team_X_choice)
            box_team_X = list(map(str, box_team_X))
            box_team_X.sort()
          
        for num in cells: 
            if cells[num] in box_team_O:
                cells[num] = 'o'
                box_team_O = list(map(int, box_team_O))
            elif cells[num] in box_team_X:
                cells[num] = 'x'
                box_team_X = list(map(int, box_team_X))           
            else:
                pass
    
        drawing = ' +===========+ \n | ' + cells[1] + ' | ' + cells[2] + ' | ' + cells[3] + ' | \n |---+---+---| \n | '+ cells[4] + ' | ' + cells[5] + ' | ' + cells[6] + ' | \n |---+---+---| \n | ' + cells[7] + ' | ' + cells[8] + ' | ' + cells[9] + ' | \n +===========+'
        print(drawing)
   
        for combinations in wincombinations.wins:
            if combinations[0] in box_team_O and combinations[1] in box_team_O and combinations[2] in box_team_O:
                print('Выиграл игрок ', team_O,'!')
                o = 1
                break
            elif combinations[0] in box_team_X and combinations[1] in box_team_X and combinations[2] in box_team_X:
                print('Выиграл игрок ', team_X,'!')
                x = 1
                break
            else:
                pass
   
        i += 1
        if o == 1 or x == 1:
            break
        elif i == 9:
            print('Ничья!')
        else:
            pass


    if o == 1:
        result = 'выиграл игрок ' + team_O + '!'
    elif x == 1:
        result = 'ыиграл игрок ' + team_X +'!'
    else:
        result = 'Ничья!'

    
    result_of_last_games = drawing + '\n' + 'В последней игре ' + result
    
    with open(way_to_directory + '\Results.txt', 'w') as file:
        file.write(result_of_last_games)

    last_games = result_of_last_games
    user_choice = (input('Если хотите сыграть еще одну партию, введите: 0, если хотите закончить партию введите: 1 '))
    user_choice = INTexam.exam(user_choice)
    cell_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if user_choice == 1:
        break
    





