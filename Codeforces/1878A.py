for _ in range(int(input())):
    _, k = input().split()
    subsegment = list(map(int, input().split()))
    if int(k) in subsegment:
        print("YES")
    else:
        print("NO")