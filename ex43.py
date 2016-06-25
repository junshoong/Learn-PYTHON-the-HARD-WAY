# -*- coding: utf-8 -*-

from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "아직 만들지 않은 장면입니다. 상속해 enter()를 구현하세요."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        print "엔진 __init__의 scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "play의 첫 장면", current_scene

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            print "다음 장면", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "지도에서 받은 새 장면", current_scene

class Death(Scene):
    
    quips = [
            "사망. 이거 진짜 못하네요.",
            "어머니가 자랑스러워 하시겠어요... 좀 더 똑똑하셨다면요.",
            "패배자 같으니.",
            "제가 기르는 강아지도 이거보단 잘 해요."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        print "페르칼 25번 행성의 고던족은 여러분의 .."
        action = raw_input(">")

        if action == "발사!":
            print "당신은 광선총을 빼들기가 무섭게 .."
            return 'death'
        
        elif action == "회피!":
            print "세계적인 권투 선수처럼 달리고 피하고 .."
            return 'death'

        elif action == "농담하기" or action == "1":
            print "운 좋게도 당신은 학교에서 고던어 .."
            return 'laser_weapon_armory'
        
        else:
            print "처리할 수 없습니다!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    
    def enter(self):
        print "당신은 무기고로 뛰어 굴러 들어가 .."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[번호판]>")
        guesses = 0

        while guess != code and guesses < 9:
            print "삐비비빅!"
            guesses += 1
            guess = raw_input("[번호판]>")

        if guess == code or guess == "1":
            print "철컥하며 컨테이너가 열리고 틈새로 .."
            return 'the_bridge'
        else:
            print "마지막 순간에 자물쇠가 웅웅거리고 .."
            return 'death'


class TheBridge(Scene):
    
    def enter(self):
        print "당신은 팔에 중성자탄을 끼고 다리로 .."
        action = raw_input(">")

        if action == "폭탄 던지기":
            print "당신은 당황해서 고던인 무리에 폭탄을 .."
            return 'death'

        elif action == "천천히 폭탄 설치하기" or action == "1":
            print "팔에 낀 폭탄을 광선총으로 겨누자 .."
            return 'escape_pod'
        else:
            print "처리할 수 없습니다!"
            return 'the_bridge'

class EscapePod(Scene):
    
    def enter(self):
        print "우주선이 통째로 폭발하기 전에 .."
        good_pod = randint(1,5)
        guess = raw_input("[구명정 번호]>")

        if int(guess) != good_pod:
            print "%s번 구명정으로 뛰어들어 .." % guess
            return 'death'
        elif int(guess) == 1:
            print "%s번 구명정으로 뛰어들어 .." % guess
            return 'finished'
        else:
            print "%s번 구명정으로 뛰어들어 .." % guess
            return 'finished'


class Map(object):

    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "__init__의 start_scene", self.start_scene

    def next_scene(self, scene_name):
        print "next_scene의 start_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene 결과는 ", val
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
