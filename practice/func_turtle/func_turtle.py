import turtle

"""
turtle.forward(distance): 현재 방향으로 distance만큼 이동
turtle.backward(distance): 현재 반대방향으로 distance만큼 이동
turtle.right(angle): 진행방향 오른쪽으로 angle만큼 회전
turtle.left(angle): 진행방향 왼쪽으로 angle만큼 회전
turtle.circle(radius, angle): 현재 지점을 기준으로 +r면 반시계방향으로 반지름 r인 원 그림
turtle.goto(x, y): x, y 좌표로 이동
turtle.dot(d): 현재 위치를 중심으로 지름 d만큼의 원을 그리고 채움
turtle.home(): 0,0 으로 이동
turtle.clear(): 그림 다 지움

turtle.color(color): 펜색 지정
turtle.penup(): 펜을 올림(이동해도 그림이 안그려짐)
turtle.pendown(): 펜을 내림(이동하면 그림이 그려짐)
"""

turtle.setup(width = 500, height = 500)

# 원점에 빨간색 점 찍기
turtle.color('red')
turtle.dot(15)
turtle.color('black')
turtle.shape('turtle')
turtle.penup()

# org_x, org_y에 n층의 피라미드를 그리는 함수
# dot의 간격은 20으로 설정, dot 크기는 10
def draw_pyramid(org_x, org_y, n):
    w = n*2-1 

    for i in range(n):
        y = i * 20
        for j in range(w-(i*2)):
            x = j * 20

            if i == 0 and j == 0:
                turtle.color('green')
            else:
                turtle.color('black')

            turtle.goto(org_x + x+20*i, org_y + y)
            turtle.dot(10)
    turtle.home()

# (x, y) 위치에 n 층의 피라미드를 그리기위해 사용자로부터 받는 입력을 저장할
# 변수를 초기화
x = None
y = None
n = None

# 메뉴를 구성하고 사용자로부터 x, y, n이 모두 입력되면 피라미드를 그리고
# x, y, n을 다시 초기화 시키고 입력 대기하는 루프
while True:
    pass 

    # x, y, n에 모든 값이 다 채워졌으면 
    # draw_pyramid()함수를 호출하여 (x,y)위치에 n층 피라미드를 그린다.
    if None:
        # 그림을 그리고
        draw_pyramid(x, y, n)
        
        # x, y, n을 다시 초기화 한다.
        pass

    # 메뉴가 완성되면 이 break를 주석 처리해서 while 루프가 제대로
    # 작동하도록 할 것
    break
