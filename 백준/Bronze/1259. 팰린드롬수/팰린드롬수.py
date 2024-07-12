while True:
    pal = input()
    if pal == "0":
        break
    elif pal == pal[::-1]:
        print("yes")
    else:
        print("no")