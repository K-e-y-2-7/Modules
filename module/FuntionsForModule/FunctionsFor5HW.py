def unique_values(dicts, keys):
    unique_elements = []
    
    for name_of_list in keys:
        for dict_to_the_first_cell in dicts:
            for dict_to_the_second_cell in dicts:
                if dict_to_the_first_cell[name_of_list] == dict_to_the_second_cell[name_of_list]:
                    pass
                else:
                    unique_elements.append(dict_to_the_first_cell[name_of_list])

    unique_elements = list(set(unique_elements))
    _range = range(0, len(unique_elements))

    list_of_categories = []

    for name_of_list in keys:
        name_of_list = []
        list_of_categories.append(name_of_list)

    for num in _range:
        print(_range, ' _range')
        print(num, ' num')
        break_check = 0
        for _dict in dicts:
            print(_dict, ' _dict')
            print(dicts, ' dicts')
            increasing_number = 0
            for key in keys:
                print(unique_elements, ' unique_elements')
                print(unique_elements[num], ' unique_elements[num]')
                print(_dict[key], ' _dict[key]')
                if unique_elements[num] == _dict[key]:
                    a = list_of_categories[increasing_number]
                    a.append(_dict)
                    break_check = 1
                    break
                else:
                    pass

                increasing_number += 1

            if break_check == 1:
                break
            else:
                pass

    for _list in list_of_categories:
        i = 0
        if _list == []:
            k = keys[i]
            unique_elements.append(dicts[0][k])
            _list.append(dicts[i])
        else:
            i += 1

    print(unique_elements)
    result = list_of_categories
    return result
