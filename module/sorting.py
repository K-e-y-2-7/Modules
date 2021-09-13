from FuntionsForModule import SortFunc
from FuntionsForModule import profile1
print('Привет,' + profile1.user_name + '!!!')

user_input = input('Введите любую числовую последовательность, отделяя елементы в ней, пробелом: ').split()
user_input = list(set(map(int, user_input)))
list_sorted = SortFunc.sort_function(user_input)
print(list_sorted)

