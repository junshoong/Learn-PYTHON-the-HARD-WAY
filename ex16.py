# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "%r 파일을 지우려 합니다." % filename
print "취소하려면 CTRL-C(^C)를 누르세요.",
print "진행하려면 리턴을 누르세요."

raw_input("?")

print "파일 여는 중..."
target = open(filename, 'w')

print "파일 내용을 지웁니다. 안녕히!"
target.truncate()

print "이제 세 줄에 들어갈 내용을 묻겠습니다."

line1 = raw_input("1줄: ")
line2 = raw_input("2줄: ")
line3 = raw_input("3줄: ")

print "이 내용을 파일에 씁니다."

target.write(line1+"\n"+line2+"\n"+line3+"\n")

print "마지막으로 닫습니다."
target.close()
