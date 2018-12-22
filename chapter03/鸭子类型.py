
class Cat(object):
    def say(self):
        print('i am a cat')


class Dog(object):
    def say(self):
        print('i am a dog')


class Duck(object):
    def say(self):
        print('i am a duck')

    def __getitem__(self, item):
        return ['xiaoweigege'][item]


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

duck = Duck()
a = ['wei1', 'wei2']
b = ['wei2', 'wei3']
name_tuple = ('wei4', 'wei5')
name_set = {'wei6', 'wei7'}
# extend 可接受的是一个可迭代的类型， 所以并不仅仅局限于list, 如果自己实现一个类 类中 定义了 __iter__ 也可以传递进去
# 这就是Python的鸭子类型
#     def extend(self, iterable):
a.extend(b)
a.extend(name_tuple)
a.extend(name_set)
a.extend(duck)
print(a)
