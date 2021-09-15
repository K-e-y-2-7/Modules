import os
import tkinter
from tkinter.constants import N
from PIL import Image, ImageTk
from random import choice
import pathlib
from FuntionsForModule import INTexam

profile_path = pathlib.Path('profile.txt')
profile_path.absolute()
with open(profile_path, 'r') as profile:
        user_name = profile.readline()
        
print('Привет,' + user_name + '!!!')
print(''''Инструкция по управлению:
    Q -- выход;
    UP -- белая клетка опустится вниз на один ярус;
    DOWN -- белая клетка поднимется вверх на один ярус;
    RIGHT -- белая клетка уйдет влево на один ярус;
    LEFT -- белая клетка уйдет вправо на один ярус;
    ''')

print ('Х = сложность мозаики. Поле игры Х * Х По умолчанию Х = 4. Если хотите изменить сложность, напишите: 1, если хотите оставить стандартную сложность напишите: 0')
user_choice = int(input('Ваш ввод: '))

while True:
    if user_choice == 1: 
        user_input1 = (input('Х = сложность мозаики. Поле игры Х * Х По умолчанию Х = 4. Если хотите изменить сложность, введите значение Х (желательно не больше 15, потому что, будет сильно лагать, и скорее всего игра крашнется): '))
        user_input1 = INTexam.exam(user_input1)
        size = user_input1
        break
    elif user_choice == 0:
        size = 4
        break
    else:
        user_choice = int(input('Вы ввели неверное значение, пожалуйста, повторите попытку: '))


way_to_module = str(pathlib.Path(__file__).parent.absolute())
print (way_to_module)
way_to_nums = way_to_module+'/nums/'
way_to_img = way_to_module+'/img/'

user_image = str(input('Введите название картинки из папки module/img: '))
dirs = os.listdir(way_to_nums)


num_files = [os.path.join(way_to_nums, file_) for file_ in dirs]

main_window = tkinter.Tk()
main_window.title('Мозаика')

frame = tkinter.Frame(main_window)
frame.grid()


def get_regions(image):
    ''' Функция разбиения изображения на квадратики.
        На входе ожидает объект PIL.Image
        Возвращает список картинок-квадратиков ImageTk.PhotoImage
    '''
    regions = []
    pixels = image.width // size
    for i in range(size):
        for j in range(size):
            x1 = j * pixels
            y1 = i * pixels
            x2 = j * pixels + pixels
            y2 = i * pixels + pixels
            box = (x1, y1, x2, y2)
            region = image.crop(box)
            region.load()
            region = ImageTk.PhotoImage(region)
            regions.append(region)
    
    return regions 



def make_mosaik_from_filename(file_name):
    ''' Создание мозаики на основе имени файла с картинкой
        Возвращает список картинок-квадратиков ImageTk.PhotoImage
    '''
    image = Image.open(file_name)
    return get_regions(image)

nums = [tkinter.PhotoImage(file=f) for f in num_files]
images = make_mosaik_from_filename(way_to_img + user_image +".jpg")
images[-1] = nums[-1]
labels = []
for i in range(size):
    for j in range(size):
        label = tkinter.Label(main_window, image=images[i*size + j])
        label.grid(row=i, column=j)
        label.x = i * size + j
        label.row = i
        label.column = j
        labels.append(label)

empty_cage = labels[-1]

labels_before = list(labels)
print(empty_cage, ' < empty_cage') 
print(labels_before, ' < labels_before') 
def grid_x(empty_cage, near):
    ''' Отрисовка расположения двух клеток
    '''
    if near is not None:
        empty_cage.grid(row=empty_cage.row, column=empty_cage.column)
        near.grid(row=near.row, column=near.column)


def exchange(empty_cage, near):
    ''' Обмен местами клеток в общем списке
    '''
    if near is not None:
        ci = empty_cage.row * size + empty_cage.column
        ni = near.row * size + near.column
        labels[ci], labels[ni] = labels[ni], labels[ci]


def label_above(empty_cage):
    '''Вернуть клетку сверху'''
    pass
    return labels[(empty_cage.row-1)*size + empty_cage.column]


def label_under(empty_cage):
    '''Вернуть клетку снизу''' 
    pass
    return labels[(empty_cage.row+1)*size + empty_cage.column]


def label_left(empty_cage):
    '''Вернуть клетку слева'''
    pass
    return labels[empty_cage.row*size + empty_cage.column - 1]


def label_right(empty_cage):
    '''Вернуть клетку справа'''
    pass
    return labels[empty_cage.row*size + empty_cage.column + 1]


def end_game(function_launch_key):
     
    if function_launch_key == 1:
        print(labels)
        if labels_before == labels:
            print('Мозайка сложена!')
            
            key_press('q', 1)

        else:
            print('Ходите еще')


def key_press(btn, launch_key ):
    '''Основная логика перемещения на игровом поле. 
       Основной элемент логики - пустая клетка - от неё определяем соседа.
       Далее меняем координаты пустой клетки и соседа.
    '''
    near = None

    if btn == 'r' and empty_cage.column > 0:
        near = label_left(empty_cage)
        end_game(launch_key)
        empty_cage.column -= 1
        near.column += 1
    elif btn == 'l' and empty_cage.column < size - 1:
        near = label_right(empty_cage)
        end_game(launch_key)
        empty_cage.column += 1
        near.column -= 1
    elif btn == 'u' and empty_cage.row < size - 1:
        near = label_under(empty_cage)
        end_game(launch_key)
        empty_cage.row += 1
        near.row -= 1
    elif btn == 'd' and empty_cage.row > 0:
        near = label_above(empty_cage)
        end_game(launch_key)
        empty_cage.row -= 1
        near.row += 1
    elif btn == 'q':
        exit() 
    exchange(empty_cage, near)
    grid_x(empty_cage, near)
 


def mix_up(launch_key):
    '''Перемешивание клеток
       SIDE ** 4 - взято для лучшего перемешивания,
       т.к. не все вызовы функции нажатия кнопок
       будут приводить к движению клеток на поле
    '''
    buttons = ['d', 'u', 'l', 'r']
    for i in range (size ** 4):
        x = choice(buttons)
        key_press(x, launch_key)
    launch_key += 1
    return end_game(launch_key)

num_key = 0
main_window.bind('<Right>', lambda e: key_press('r', 1))
main_window.bind('<Left>', lambda e: key_press('l', 1))
main_window.bind('<Up>', lambda e: key_press('u', 1))
main_window.bind('<Down>', lambda e: key_press('d', 1))
main_window.bind('<q>', lambda e: key_press('q', 1))

main_window.after(5000, mix_up(num_key)) 
main_window.mainloop()


    