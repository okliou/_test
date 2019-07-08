# 装饰器
# def singleton(cls):
#     instances = {}
#
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper
#
#
# @singleton
# class Foo(object):
#     pass


# new方法
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class Foo(Singleton):
#     pass


# 元类，类对象创建实例对象时一定要调用call方法
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton):
    __metaclass__ = Singleton


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()
    print(foo1 is foo2)
