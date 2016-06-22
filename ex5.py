# -*- coding: utf-8 -*-

name = "Zed A. Shaw"
age = 35 # not a lie
height = 188/2.54 # inch
weight = 82/0.4536 # pound
eyes = '파랑'
teeth = '하양'
hair = '갈색'

print "%s에 대해 이야기해 보죠." % name
print "키는 %d 센티미터고요." % height
print "몸무게는 %r 킬로그램이에요." % weight
# %r은 '이게 뭐든 표현해!'
print "사실 아주 많이 나가는건 아니죠."
print "눈은 %s이고 머리는 %s이에요." % (eyes, hair)
print "이는 보통 %s이고 커피를 먹으면 달라져요." % teeth

# 이 줄은 까다롭지만 정확히 따라 하세요
print "%d, %d, %d를 모두 더하면 %d 랍니다." % (
        age, height, weight, age + height + weight)
