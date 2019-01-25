
def sum_type():
    count = 0
    nums = []
    while True:
        x = yield
        if not x:
            break
        count += x
        nums.append(x)

    return count, nums


def midder(key):
    while True:
        final_dict[key] = yield from sum_type()


def main():
    data_dict = {
        '手机': [200, 500, 400, 800],
        '电脑': [150, 200, 178],
        '空调': [845, 654, 102, 784, 520]
    }
    for key, values in data_dict.items():
        m = midder(key)
        m.send(None)
        for v in values:
            m.send(v)
        m.send(None)

    print(final_dict)


if __name__ == '__main__':
    final_dict = dict()
    main()