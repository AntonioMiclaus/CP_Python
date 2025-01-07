for _ in range(int(input())):
    n = int(input())
    s = input()
    if "B" in s:
        print(s.rfind("B")-s.find("B")+1)
    else:
        print(0)
