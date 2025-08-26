import sys

args = sys.argv[1:]
a = 0
for i in args:
    a += int(i)


average = a / len(args)
print(average)


#모르겠네....