for _ in range(int(input())):
    a, b = map(int, input().split())
    print(max(0, min(a, 2*a - b)))