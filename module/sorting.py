from FuntionsForModule import SortFunc
import pathlib

print('Сортировка')

profile_path = pathlib.Path('profile.txt')
profile_path.absolute()
with open(profile_path, 'r') as profile:
        user_name = profile.readline()

print('Привет,' + user_name + '!!!')

user_input = input('Введите любую числовую последовательность, отделяя елементы в ней, пробелом: ').split()
user_input = list(set(map(int, user_input)))
list_sorted = SortFunc.sort_function(user_input)
print(list_sorted)

