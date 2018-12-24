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


class User(object):
    def __init__(self, birthady):
        self.__birthady = birthady

    def get_age(self):
        return 2018 - self.__birthady.year


if __name__ == '__main__':
    user = User(Date.from_string('1996-09-02'))
    print(user.get_age())
    print(user._User__birthady)