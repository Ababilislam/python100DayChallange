def myFun(**kwargs):
    for key, value in kwargs.items():
        print("{} == {}".format(key, value))


# Driver code
myFun(first='my', mid='name', last='is')
