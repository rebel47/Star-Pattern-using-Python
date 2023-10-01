def christmas(rows):
    for i in range(rows//2):
        print(" "*(rows-i-1) + "*"*(2*i+1))
    for i in range(rows//2, rows):
        print(" "*(rows-1) + "*")
    print(" "*(rows-1) + "|")

christmas(15)
