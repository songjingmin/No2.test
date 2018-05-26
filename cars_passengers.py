# 汽车数量
cars = 100

#每辆汽车座位
space_in_a_car = 4.0

#司机数量
drivers = 30

#乘客数量
passengers = 90

#没有司机的车的数量
cars_not_driven = cars - drivers

#有司机的车的数量
cars_driven = drivers

#可用车厢容量
carpool_capacity = cars_driven * space_in_a_car
#每辆车上的平均乘客量
average_passengers_per_car = passengers / cars_not_driven

print ("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("We need to put about", average_passengers_per_car, "in each car.")