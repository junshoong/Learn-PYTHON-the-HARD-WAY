# -*- coding: utf-8 -*-

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "자동차", cars, "대가 있습니다."
print "운전자는", drivers, "명 뿐입니다."
print "오늘 빈 차가", cars_not_driven, "대일 것입니다."
print "오늘은", carpool_capacity, "명을 태울 수 있습니다."
print "함께 탈 사람은", passengers, "명 있습니다."
print "차마다", average_passengers_per_car, "명 정도씩 타야 합니다."
