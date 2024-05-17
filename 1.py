def _hash(s: str, x=256, prime=101) -> int:
    return sum([ord(v)*x**(len(s)-c-1) for c, v in enumerate(s)]) % prime

def search(sub: str, string: str) -> int:
    h = _hash(sub)
    for i in range(0, len(string)):
        current = _hash(string[i:i+len(sub)])
        if current == h and string[i:i+len(sub)] == sub:
            return i
    return -1

s = 'hello, world!'
sub = 'world'
print(search(sub, s))
