friends=['김도한', '류은진', '이광우', '한승욱', '김유준']

for name in friends:
    print('오늘 나오신 분은' + name + '입니다.')

출석부 = {'이광우':"출석", "한승욱":"출석", "류은진":"출석", "김도한":"출석", "정유선":"아픔", "김유준":"조퇴", "염재희":"결혼", "박지영":"격무에 시달림", "고유빈":"대학생"}
for element in 출석부.items():
    if element[1] == "출석":
        print(element[0]+'님은 VIP이십니다.')
    else:
        print(element[0]+'님은 아쉬우신 분들입니다. 사유:'+element[1])



