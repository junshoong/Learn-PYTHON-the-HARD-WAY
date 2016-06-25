# -*- coding: utf-8 -*-

class Parent(object):

    def override(self):
        print "부모 override()"

    def implicit(self):
        print "부모 implicit()"

    def altered(self):
        print "부모 altered()"

class Child(Parent):

    def override(self):
        print "자식 override()"

    def altered(self):
        print "자식, 부모 altered() 호출 전"
        super(Child, self).altered()
        print "자식, 부모 altered() 호출 후"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
