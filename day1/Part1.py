
import sys


max_calories = 0 
calories_actual = 0    

for line in sys.stdin:
    if line != "\n":
        calories_actual += int(line)

    if line == "\n":
        if calories_actual > max_calories:
            max_calories= calories_actual
            print ("max :" , max_calories)
        calories_actual = 0


print("--------------------")
print ("max :" , max_calories)

