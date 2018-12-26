# set 集合 fronzenset(不可变集合) 无序, 不重复
s = set('abcdefff')

print(s)
# 不可变的set 可以作为dict的key
b = frozenset('abcde')

# 求差集
result = s.difference(b)
# 这样也可以求差集
result_ = s - b
# 交集
result_j = s & b
# 并集
result_b = s | b

print(result)
print(result_)
print(result_j)
print(result_b)