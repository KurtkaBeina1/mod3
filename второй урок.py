a = 'ABCAACCBBAA44456'


# множество - строка состоящая из уникальных\ неповторяющихся объектов

def strcount(a):  # O(N**2)
    for char in a:
        counter = 0
        for sub_char in a:
            if char == sub_char:
                counter += 1
        print(char, counter)


def strcount(a):  # O(N*M)
    for char in set(a):  # set - переделывает во множество строку
        counter = 0
        for sub_char in a:
            if char == sub_char:
                counter += 1
        print(char, counter)

        

def strcount_2(a):  # O(N)
    syms_counter = {}
    for char in a:
        syms_counter[char] = syms_counter.get(char, 0) + 1
    print(syms_counter)

strcount(a)
