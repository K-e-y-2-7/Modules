from FuntionsForModule import FunctionsFor5HW
import pathlib

profile_path = pathlib.Path('profile.txt')
profile_path.absolute()

with open(profile_path, 'r') as profile:
        user_name = profile.readline()

print('Привет,' + user_name + '!!!')

Number_of_dicts = int(input('Введите количество словарей на проверку уникальности: '))
Number_of_keys = int(input('Введите количество ключей: '))

List_of_dicts, Key_of_dicts = [], []

for number in range(0, Number_of_keys):
    key = input('Введите название ключа: ').title()
    Key_of_dicts.append(key)

print(Key_of_dicts)

for number in range(1, Number_of_dicts + 1):
    def get_user_data(Keys = Key_of_dicts):
        user_data = {}
        for key in Keys:
            user_data[key] = ''
        return user_data


    User_data = get_user_data()

    for key in User_data:
        User_data[key] = input('Введите значение ключа ' + key + ' : ')

    List_of_dicts.append(User_data)

print(FunctionsFor5HW.unique_values(List_of_dicts, Key_of_dicts))
