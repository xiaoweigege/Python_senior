from copy import deepcopy
a = {
    'xw': {'company': 'pf'},
    'xw1': {'company': 'pf1'}
}

# clear 清空字典
# a.clear()
# print(a)

# copy, 返回浅拷贝
new_dict = a.copy()
new_dict['xw1']['company'] = 'xwkj'
# 修改了new_dict 也修改了 a
# 浅拷贝 只 copy 第一层
print(new_dict)
print(a)
print('--------------')
# 深拷贝
deep_dict = deepcopy(a)
deep_dict['xw']['company'] = 'qwer'
print(deep_dict)
print(a)

print('------------')
# 列表转字典
new_list = ['xw', 'pf']
new_dict = dict.fromkeys(new_list, [1, 2])
print(new_dict)

for k, v in new_dict.items():
    print(k, v)

