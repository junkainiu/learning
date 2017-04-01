#coding=utf-8
class Integer(object):#Integer就是一个描述器,因为定义了__set__()方法.
    def __init__(self, name):
        self.name = name
    def __set__(self, instance, value):#因为我们只需要对"修改属性"这个行为进行hook,所以我们只定义__set__()方法就够了,不用__get__()和__delete__().
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

class Point(object):
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
p.x = 9
p.x = 9.9#这句会抛出TypeError: Expected an int错误.这就是描述器的作用.
