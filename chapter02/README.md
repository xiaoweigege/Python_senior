# 魔法函数

1. 什么是魔法函数
2. Python的数据模型以及数据模型对Python的影响
3. 魔法函数一览
    1. 非数学运算
        1. 字符串表示
            1. `__repr__`
            2. `__str__`
        2. 集合序列相关
            1. `__len__`
            2. `__getitem__`
            3. `__setitem__`
            4. `__delitem__`
            5. `__contains__`
        3. 迭代相关
            1. `__iter__`
            2. `__next__`
        4. 可调用
            1. `__call__`
        5. with 上下文管理器
            1. `__enter__`
            2. `__exit__`
        6. 数值转换
            1. `__abs__`
            2. `__bool__`
            3. `__int__`
            4. `__float__`
            5. `__hash__`
            6. `__index__`
        7. 元类相关
            1. `__new__`
            2. `__init__`
        8. 属性相关
            1. `__getattr__`
            2. `__setattr__`
            3. `__getattribute__`
            4. `__setattribure__`
            5. `__dir__`
        9. 属性描述符
            1. `__get__`
            2. `__set__`
            3. `__delete__`
        10. 协程
            1. `__await__`
            2. `__aiter__`
            3. `__anext__`
            4. `__aenter__`
            5. `__aexit__`


    2. 数学运算
        1. 一元运算
            1. `__neg__`( - ), `__pos__`( + ), `__abs__`
        2. 二元运算
            1. `__lt__` ( < ), `__le__` ( <= ), `__eq__`(==), `__ne__`(!=)
            2. `_gt__`( > ), `__ge__` ( >= )
        3. 算术运算符
            1. `__add__` ( + ), `__sub__` ( - ), `__mul__` ( * ), `__truediv__` ( / ), `__floordiv__` ( // )
            2. `__mod__` ( % ), `__divmod__` ( divmod() ), `__pow__` ( ** 或 pow() ), `__round__` ( round() )
        4. 反向算术运算符
            1. `__radd__`, `__rsub__`, `__rmul__`, `__rtruediv__`
            2. `__rfloordiv__`, `__rmod__`, `__rdivmod__`, `__rpow__`
        5. 增量赋值算术运算符
            1. `__iadd__` ( += ), `__isub__`, `__imul__`, `__itruediv__`
            2. `i_floordiv__`, `__imod__`, `__ipow__`
        6. 位运算符
            1. `__invert__` ( ~ ), `__lshift__` ( << ), `__rshift__` ( >> ), `__and__` ( & )
            2. `__or__` ( | ), `__xor__` ( ^ )
        7. 反向位运算符
            1. `__rlshift__`, `__rrshift__`, `__rand__`, `__rxor__`
            2. `__ror__`
        8. 增量赋值位运算符
            1. `__ilshift__`, `__irshift__`, `__iand__`, `__ixor__`, `__ior__`

            
4. 随便举个例子说明魔法函数的重要性(len函数)
