
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def parser_from_string(date_str):
        year, month, day = tuple(date_str.split('-'))
        # 静态方法 的一个缺点的 是这里用了硬编码
        # 当类名改变了, 这里必须改, 所有产生了 类方法
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        if int(year) > 0 and (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    def add_one_day(self):
        self.day += 1

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':

    newDate = Date(2018, 12, 23)
    newDate.add_one_day()
    print(newDate)

    # 静态方法完成实例化
    new_date = Date.parser_from_string('2018-12-31')
    print(new_date)

    # 类方法实现实例化
    class_date = Date.from_string('2018-12-18')
    print(class_date)

    print(Date.valid_str('2018-12-15'))