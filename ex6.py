# -*- coding: utf-8 -*-

x = "세상에는 %d 종류의 사람이 있어요." % 10
binary = "'이진수'"
do_not = "모르는"
y = "%s를 아는 사람과 %s 사람." % (binary, do_not)
z = 'How fun is it!'

print x
print y
print z

print "'%s'라고 했어요." % x
print "'%s'이라고도 했죠." % y
print "So, %r" % z

hilarious = False
joke_evaluation = "웃기는 농담 아니어요?! %r"

print joke_evaluation % hilarious

w = "이 문자열의 왼쪽 ->"
e = "<- 이 문자열의 오른쪽"

print w + e
