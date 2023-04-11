# import fileinput
import fileinput

# Using fileinput.input() method
for line in fileinput.input(files='data.txt'):
	print(line)
