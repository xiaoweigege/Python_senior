
class Group(object):
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self.group_name, self.company_name, self.staffs[item])
        elif isinstance(item, int):
            return cls(self.group_name, self.company_name, [self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        # 此魔法函数可以用来被 if  in  这样的操作
        if item in self.staffs:
            return True
        else:
            return False


if __name__ == '__main__':
    group = Group('小伟科技', 'boos', ['xw1', 'xw2'])
    print(group[1].staffs)
    print(len(group))
    if 'xw1' in group:
        print('yes')
    else:
        print('no')

    reversed(group)
    print(group.staffs)