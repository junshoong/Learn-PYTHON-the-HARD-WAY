# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['사과', '귤', '배', '살구']
change = [1, '십원', 2, '백원', 3, '오백원']

# 첫 번째 for문은 list를 따라 돕니다.
for number in the_count:
    print "이 수는 %d" % number

# 위와 같아요.
for fruit in fruits:
    print "과일 종류: %s" % fruit

# 섞어 만든 list도 돌 수 있어요.
for i in change:
    print "받은 잔돈 %s" % i

elements = range(0, 6)

# 이것도 출력할 수 있습니다.
for i in elements:
    print "원소는 %d" % i
