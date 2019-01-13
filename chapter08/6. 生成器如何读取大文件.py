
def my_read_lines(f, newline):
    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(1024)
        if not chunk:
            yield buf
            break
        buf += chunk


with open('input.txt', 'r') as f:
    string = my_read_lines(f, '{ | }')
    for s in string:
        print(s)