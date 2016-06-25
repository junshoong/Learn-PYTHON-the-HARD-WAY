# -*- coding: utf-8 -*-

numbers = []

def while_checker(end, add):
    i = 0
    while i < end:
        print "꼭대기에서 i는 %d" % i
        numbers.append(i)

        i += add
        print "숫자는 이제: ", numbers
        print "바닥에서 i는 %d" % i

print "마지막 숫자를 입력하세요."
end = int(raw_input(">"))
print "반복해서 더할 숫자를 입력하세요."
add = int(raw_input(">"))
while_checker(end, add)

print "숫자: "

for num in numbers:
    print num
