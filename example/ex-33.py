#####################################################################        
# 실습문제33: 리스트 홀수번째 합   02. 리스트 18번 슬라이드
# lab 33
nums = [5, 15, 2, -8, -12, -29, 43, 1]

# 홀수번째 원소의 합
# print( sum(nums[::2]) )

j = 0
for i in nums[::2]:
    j += i
    
print(j)
##################################################################### 