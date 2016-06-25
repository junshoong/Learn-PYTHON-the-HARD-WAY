# -*- coding: utf-8 -*-

class Other(object):

    def override(self):
        print "다른 override()"

    def implicit(self):
        print "다른 implicit()"

    def altered(self):
        print "다른 altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "자식 override()"

    def altered(self):
        print "자식, 다른 altered() 호출 전"
        self.other.altered()
        print "자식, 다른 altered() 호출 후"

son = Child()

son.implicit()
son.override()
son.altered()
