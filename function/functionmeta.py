
def decorator2(func):
    def wrapper(*args, **kwargs):
        print 'Decorator 2'
        func(*args, **kwargs)
        print getattr(func, '__name__')
        for arg in args:
            print arg
    return wrapper


@decorator2
def get(para):
    print '{}, welcome'.format(para)


if __name__ == '__main__':
    get('test')

