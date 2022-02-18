import sys

data = []
n = 28

size = -1

for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)

    if (b > size):
        print(f'Length {a} Size {b}')
        size = b

    data.append(None)
