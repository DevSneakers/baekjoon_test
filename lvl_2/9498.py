# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D
# #나머지 점수는 F를 출력하는 프로그램
# a = int(input())
# if(a >= 90):
#     print('A')
# elif(a >= 80):
#     print('B')
# elif(a >= 70):
#     print('C')
# elif(a >= 60):
#     print('D')
# else:
#     print('F')

a = int(input())
score_db = [90, 80, 70, 60]
score = ['A', 'B', 'C', 'D']

if(a >= 60):
    for i in range(len(score_db)):
        if(a >= score_db[i]):
            print(score[i])
            break
else:
    print('F')