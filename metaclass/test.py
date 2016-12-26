from get_xxx_by_name import Apple


def test():
    apple = Apple()
    print apple.name


def get_function_by_name(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)


def get_class_by_name(module_name, class_name):
    module = __import__(module_name)
    return getattr(module, class_name)


if __name__ == '__main__':
    cls = get_class_by_name('keywork_class_', 'Orange')
    fruit = cls()
    print fruit.name
