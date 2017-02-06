

field_names = ['a', 'b', 'c']
names = map(str, field_names)
print names

typename = 'tuple'
print [typename] + field_names



Point = namedtuple('Point', ['x', 'y', 'z'])
point = Point(1, 2, 3)
print point

point.x = 5
print point
