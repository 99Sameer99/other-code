width = 80
iters = 30

##class wrappingboolarray:
##    def __init__(self, length, defval=0):
##        self._items = [defval for i in range(length)]
##        self._length = length
##
##    def __getitem__(self, index):
##        return self._items[index % self._length]
##
##    def __setitem__(self, index, value):
##        self._items[index % self._length] = value
##
##    def __str__(self):
##        return ''.join(['|' if item == 1 else '-' for item in self._items])


def print_gen(lst):
    print(''.join([ '|' if i == 1 else ' ' for i in lst ]))


og = [0]*width
og[width//2] = 1

print_gen(og)
print('=================')

for _ in range(iters):
    nex_gen = []
    for i in range(1, len(og)-1):
        if [og[i-1], og[i], og[i+1]] == [1, 1, 1]:
            nex_gen.append(0)
        elif [og[i-1], og[i], og[i+1]] == [1, 1, 0]:
            nex_gen.append(0)
        elif [og[i-1], og[i], og[i+1]] == [1, 0, 1]:
            nex_gen.append(0)
        elif [og[i-1], og[i], og[i+1]] == [1, 0, 0]:
            nex_gen.append(1)
        elif [og[i-1], og[i], og[i+1]] == [0, 1, 1]:
            nex_gen.append(1)
        elif [og[i-1], og[i], og[i+1]] == [0, 1, 0]:
            nex_gen.append(1)
        elif [og[i-1], og[i], og[i+1]] == [0, 0, 1]:
            nex_gen.append(1)
        elif [og[i-1], og[i], og[i+1]] == [0, 0, 0]:
            nex_gen.append(0)

    og = [0] + nex_gen + [0]
    print_gen(og)
