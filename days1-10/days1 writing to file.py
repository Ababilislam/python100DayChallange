# file1 = open("data.txt","w")
l= ["this is dhaka \n", "this is paris \n", "this is tangail\n"]
# s = "Hello world\n"
#
# file1.write(s)
#
# file1.writelines(l)
#
# file1.close()
#
# file1 = open("data.txt",'r')
# print(file1.read())
# file1.close()

###############################
# with open():
##############################
with open("data.txt",'w') as file:   #writing into file
    file.write("hello this is UDOY\n")
    file.writelines(l)

with open('data.txt','r') as file:
    print(file.read())
