# -*- coding: utf-8 -*-

people = 20
cats = 30
dogs = 15


if people < cats:
    print "고양이가 너무 많아요! 세상은 멸망합니다!"

if people > cats:
    print "고양이가 많이 않아요! 세상은 지속됩니다!"

if people < dogs:
    print "세상은 침에 젖습니다!"

if people > dogs:
    print "세상은 말랐습니다!"


dogs += 5

if people >= dogs:
    print "사람은 개보다 많거나 같습니다"

if people <= dogs:
    print "사람은 개보다 적거나 같습니다."


if people == dogs:
    print "사람은 개입니다."
