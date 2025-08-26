f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())


# 문제는 f1을 close 하지 않아서..?
# 근데 close안했는데 왜 안되는거지