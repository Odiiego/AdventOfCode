import hashlib


def getKey():
    n = 1
    while True:
        input = f"iwrupvqb{n}"
        result = hashlib.md5(input.encode())
        if result.hexdigest()[:6] == "000000":
            print(n)
            return n
        else:
            n += 1
