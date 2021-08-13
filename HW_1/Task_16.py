def task_16(w):
    left, right = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'], ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
    if w[0] in left:
        for i in range(len(w)):
            if i % 2 != 0:
                if w[i] not in right:
                    return False
            else:
                if w[i] not in left:
                    return False
        return True
    else:
        for i in range(len(w)):
            if i % 2 != 0:
                if w[i] not in left:
                    return False
            else:
                if w[i] not in right:
                    return False
        return True


assert task_16("yams")
assert not task_16("test")
print(task_16(input("Write a word: ")))
