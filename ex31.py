# -*- coding: utf-8 -*-

print "문이 두 개 있는 어두운 방에 들어왔습니다. 1번과 2번 중 어느 방으로 들어갈까요?"

door = raw_input(">")

if door == "1":
    print "거대 곰이 치즈 케이크를 먹고 있습니다. 무엇을 할까요?"
    print "1. 케이크를 뺏는다."
    print "2. 곰에게 소리를 지른다."

    bear = raw_input(">")

    if bear == "1":
        print "곰이 당신의 머리를 먹어치웁니다. 잘했어요!"
    elif bear == "2":
        print "곰이 당신의 머리를 먹어치웁니다. 잘했어요!"
    else:
        print "음, %s 행동을 하는 것이 더 나았나 보네요. 곰이 도망갑니다." % bear

elif door == "2":
    print "당신은 크툴루 눈동자의 끝없는 심연을 쳐다봅니다."
    print "1. 블루베리."
    print "2. 노란 재킷 빨래집게."
    print "3. 권총이 울부짖는 가락 이해하기."

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "당신의 육체는 젤리푸딩의 마음의 힘으로 살아남았습니다. 잘했어요!"
    else:
        print "광기가 당신의 눈을 썩어 문드러진 시궁창으로 만듭니다. 잘했어요!"

else:
    print "비틀거리다 발을 헛디뎌 칼날로 떨어져 죽습니다. 잘했어요!"
