
# def get_total_page(m, n):
#     (total_page) = m/n + 1
#     print(int(total_page))

# get_total_page(40,20)


# paging.py
def get_total_page(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))  # 3 출력

# // 이거는 몫을 의미하는 것