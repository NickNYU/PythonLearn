def define_list_dict():
    list = [dict()]
    list[0]['admin'] = 'administrator'
    list[0]['password'] = 'password'
    print list


def update_dict_with_empty():
    dict1 = dict(x='ssfd',
                 y='')
    dict2 = dict(y=dict1.get('y', 'nick'))
    print dict2


if __name__ == '__main__':
    update_dict_with_empty()