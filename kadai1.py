for x in range(1,101):
    if (x % 3 == 0 and x % 5 == 0):
        print("だいがく爆破したい")
    elif(x % 3 == 0):
        print("勉強したい")
    elif(x % 5 == 0):
        print("就活したい")
    else:
        print(f"{x}")

        