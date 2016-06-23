# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "치즈가 %d개 있어요!" % cheese_count
    print "크래커가 %d상자 있어요!" % boxes_of_crackers
    print "파티 벌이기에 충분하네요!"
    print "담요 한 장 가져 오세요.\n"


print "함수에 그냥 숫자를 직접 줄 수 있습니다."
cheese_and_crackers(20, 30)

print "스크립트의 변수를 쓸 수도 있고요."
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "안에서 계산을 해도 됩니다."
cheese_and_crackers(10 + 20, 5 + 6)


print "합쳐서 변수도 쓰고 계산도 할 수도 있습니다."
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
