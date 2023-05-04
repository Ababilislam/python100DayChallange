def eveOdd(x):
    """Function to check if the number is even or odd"""
    if (x % 2 == 0):
        print("'{}' this number is even".format(x))
    else:
        print("'{}' this number is odd".format(x))


eveOdd(2)
eveOdd(3)
print(eveOdd.__doc__)
