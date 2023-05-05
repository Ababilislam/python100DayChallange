# Checking number of occurrence of
# geeks in string

# generator to print even numbers
def print_even(checking_data, checker) :
    for i in checking_data:
        if i == checker:
            yield i

# initializing string
test_string = " The are many student around you, \
student are known for teaching other student"

# printing even numbers using yield
count = 0
print ("The number of {checking data} in string is : ", end = "" )
test_string = test_string.split()

for j in print_even(test_string, "student"):
    count = count + 1

print (count)