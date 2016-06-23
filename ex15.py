# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename)

print "파일 %r의 내용:" % filename
print txt.read()

print "파일 이름을 다시 입력해 주세요."
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
