#####################################################################
# 실습문제37: 평균 구하기
# lab 37
L = [1,2,3,4,5,6,7,8,9,10]

def mean1(L):
    S = 0.0
    for xi in L:
        S += xi

    m = S / len(L)

    return m 

def mean2(L):
    return sum(L) / len(L)

print(mean1(L))
print(mean2(L))
##################################################################### 