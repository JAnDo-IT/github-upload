# Day 1: Data Types
i = 4
d = 4.0
s = "HackerRank "
# Declare second integer, double, and String variables.
ii = int (5)
dd = float(5.0)
ss = str(" HR2 ")

# Read and save an integer, double, and String to your variables.
#ii = int(input(" int value: "))
#dd = float(input(" double value: "))
#ss = str(input(" string value: "))
#In the Test output is printed should
ii = int(input())
dd = float(input())
ss = str(input())

#print()

#print (ii)
#print("{0:.1f}".format(dd))
#print(ss)

# Print the sum of both integer variables on a new line.
sumi = i + ii
print(sumi)

# Print the sum of the double variables on a new line.
sumd = d + dd
print("{0:.1f}".format(sumd))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+ss)

#optional
#sums = s + ss
#print(sums)