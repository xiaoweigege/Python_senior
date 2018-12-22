
class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    # 可以迭代 或者 company[0]
    def __getitem__(self, item):
        return self.employee_list[item]


company = Company(['tom', 'xiaowei', 'jane'])
for em in company:
    print(em)

print(company[0])
