def shownumbers(limit):
    for i in range(0,limit +1):
        if i % 2 == 0:
            print(i , "even")

        else:
            print(i,"odd")

limit = int(input("Enter a number : "))
shownumbers(limit)
