import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    # f = open('memo.txt', 'a')
    # f.write(memo)
    # f.write('\n')
    # f.close
    with open('memo.txt', 'a') as f:
        f.write(memo)
        f.write('\n')
elif option == '-v':
    with open('memo.txt', 'r') as f:
        memo = f.read()
        print(memo)




#print(sys.argv)
# 입력받은것을 리스트로 만들어서 출력

