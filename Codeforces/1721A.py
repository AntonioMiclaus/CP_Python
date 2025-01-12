for _ in range(int(input())):
    letters = list(input())
    letters.extend(list(input()))
    letters = set(letters)
    if len(letters) == 1:
        print(0)
    elif len(letters) == 2:
        print(1)
    elif len(letters) == 3:
        print(2)
    else:
        print(3)
