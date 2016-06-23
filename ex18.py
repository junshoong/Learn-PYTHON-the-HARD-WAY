# -*- coding: utf-8 -*-

# argv를 쓴 스크립트와 비슷한 함수
def print_two(*args):
    arg1, arg2 = args
    print "실행인자1: %r, 실행인자2: %r" % (arg1, arg2)

# 좋아요. 사실 *args는 필요가 없습니다. 그냥 이렇게 하죠.
def print_two_again(arg1, arg2):
    print "실행인자1: %r, 실행인자2: %r" % (arg1, arg2)

# 이 함수는 실행인자를 하나만 받습니다.
def print_one(arg1):
    print "실행인자1: %r" % arg1

# 이 함수는 실행인자를 하나도 받지 않습니다.
def print_none():
    print "아무것도 받지 않음."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
