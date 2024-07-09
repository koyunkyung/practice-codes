while True:
    tri = map(int, input().split())
    sort = sorted(tri)
    if sort == [0,0,0]:
        break
    elif sort[2]**2 == sort[0]**2 + sort[1]**2:
        print("right")
    else:
        print("wrong")