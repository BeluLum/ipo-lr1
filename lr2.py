
import math
var_int = 70
var_float = 8.4
var_str = "No"
big_int35 = var_int*3.5
var_float +=1
var_str = "No" * 3 + "Yes" * 2
print(f"{big_int35}\n{var_float}\n{var_str}")


n=int(input("Введите количество школьников: "))
k=int(input("Введите количество яблок: "))
remainder=k % n
result= k // n
print("яблок досталось каждому", result)
print("яблок в корзинке", remainder)


volume=int(input("Введите обьем "))
pi=3.14
radius=3*(volume**1/3)/4*pi
print("радиус равен",radius)

firstClass = int(input("Введите количество учеников в первом классе: "))
secondClass = int(input("Введите количество учеников во втором классе: "))
thirdClass = int(input("Введите количество учеников в третьем классе: "))
firstDesks = firstClass // 2 + firstClass % 2
secondDesks = secondClass // 2 + secondClass % 2
thirdDesks = thirdClass // 2 + thirdClass % 2
allDesks = thirdDesks + secondDesks + firstDesks
print("всего нужно парт", allDesks )


x=float(input("введите х "))
y=float(input("введите y "))
result=( 8 + (abs (x - y)) ** 2 + 1) ** (1/3) / (x**2 + y**2 + 2) - math.exp(abs(x - y))
print(result)
