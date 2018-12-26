import bisect

# 用来处理已排序的序列, 用来维持已排序的序列, 升序, 主要利用二分查找法来实现的

# 二分查找, 插入是有序的
inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)

print(bisect.bisect(inter_list, 4))
print(inter_list)
