def task_14(letter):
    if len(letter) > 1:
        return "Letter is not a char"
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if letter.lower() in vowels:
        return "vowel"
    return "consonant"


assert task_14("a") == "vowel"
assert task_14("b") == "consonant"
assert task_14("ab") == "Letter is not a char"
print(task_14(input("Write letter: ")))
