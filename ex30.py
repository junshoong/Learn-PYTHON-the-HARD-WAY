# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15


if cars > people:
    print "차를 타야 해요."
elif cars < people:
    print "차를 안 타야 해요."
else:
    print "결정할 수 없어요."

if buses > cars:
    print "버스가 너무 많아요."
elif buses < cars:
    print "버스를 탈 수도 있어요."
else:
    print "아직도 결정할 수 없어요."

if people > buses:
    print "좋아요 버스를 탑시다."
else:
    print "좋아요 그럼 집에 있죠."
