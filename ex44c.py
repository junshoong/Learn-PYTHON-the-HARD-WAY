# -*- coding: utf-8 -*-

class Parent(object):

    def altered(self):
        print "부모 altered()"

class Child(Parent):

    def altered(self):
        print "자식, 부모 altered() 호출 전"
        super(Child, self).altered()
        print "자식, 부모 altered() 호출 후"

dad = Parent()
son = Child()

dad.altered()
son.altered()
