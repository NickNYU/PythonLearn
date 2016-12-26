import sys

'''
Examples:
1. Get Function by module and function name
2. Get Class by module and function name
'''


def get_function_by_name(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)


def get_class_by_name(module_name, class_name):
    module = __import__(module_name)
    return getattr(module, class_name)


class Apple(object):
    def __init__(self):
        self.name = "apple"


class Orange(object):
    def __init__(self):
        self.name = "orange"


class FruitController(object):

    def __init__(self, cls_type):
        self.type = cls_type
        print sys.modules['metaclass']['get_xxx_by_name']
        self.fruit = getattr(sys.modules['get_xxx_by_name'], self.type)

    def show_type(self):
        print self.fruit


def main():

    controller = FruitController("Apple")
    controller.show_type()

if __name__ == '__main__':
    cls = get_class_by_name('get_xxx_by_name', 'Apple')
    print cls
    apple = cls()
    print apple.name

