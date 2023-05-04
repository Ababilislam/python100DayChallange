
def swap(x,y):
    x,y=y,x
    print(x, y)

x=2
y=5
print("initial value")
print(x,y)
print("this is function swap value")
swap(x,y)
print("this is local value")
print(x,y)