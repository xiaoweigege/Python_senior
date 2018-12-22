# Python 中国一切皆对象

1. 一切皆对象
    1. 动态语言和静态语言的却别
        1. Python面向对象更彻底
    2. 函数和类也是对象,属于Python的一等公民
        1. 赋值给一个变量
        2. 可以添加到集合对象中
        3. 可以作为参数传递给函数
        4. 可以当做函数的返回值
2. type、object、class 的关系 (重要)
    1. type -> class -> object
    2. type 继承自 object , object 实例化之后是type
    3. Python 中所有对象都是由type 创建出来的

3. Python中的常见内置类型
    1. 对象的3个特征
        1. 身份 (内存地址)
        2. 类型 (int, str, 等等)
        3. 值   (1,'qwe',等等)
    2. None (全局只有一个)
    3. 数值
        1. int
        2. float
        3. complex
        4. bool (1,0)
    4. 迭代类型
    5. 序列类型
        1. list
        2. bytes,bytearray,memoryview(二进制序列)
        3. range
        4. tuple
        5. str
        6. array
    6. 映射(dict)
    7. 集合
        1. set
        2. frozenset
    8. 上下文管理类型(with)
    9. 其他
        1. 模块类型(import)
        2. class和实例
        3. 函数类型
        4. 方法类型
        5. 代码类型
        6. object对象
        7. type类型
        8. ellipsis类型(省略号)
        9. notimplemented类型
