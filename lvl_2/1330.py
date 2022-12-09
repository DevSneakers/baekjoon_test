# 두 정수 A B 가 주어졌을 때 A B 비교 프로그램
a, b = map(int, input().split())
if(a == b):
    print('==')
elif(a > b):
    print('>')
else:
    print('<')