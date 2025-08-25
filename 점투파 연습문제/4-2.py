def avg_number(*args):
    result = 0
    for i in args:
        result += i
    return print(result/len(args))

avg_number(1, 2)
avg_number(1,2,3,4,5)