def firstn_gen(n):
    for i in range(0, n):
        yield i

def print_strs(name):
    print(f'Hello, {name}!')
    yield
    print(f'Fuck you, {name}!')
    yield

def infinite():
    i = 0
    while True:
        yield i
        i += 1

def io():
    while True:
        x = yield
        yield x*2

def print_sended():
    x = 'start'
    while True:
        x = yield x
        print('Got value', x)

it = print_sended()
next(it)
for i in range(0, 10):
    it.send(i)
