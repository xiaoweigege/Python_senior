# array deque
# 数组, 是一组连续的内存空间
import array
# arrapy 和 list 的一个重要区别, array 只能存放指定的数据类型
my_array = array.array('i')
my_array.append(1)
my_array.append(2)
print(my_array)