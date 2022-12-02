
import sys


top_calories = [0,0,0]
calories_actual = 0    
min_arg_actual= 0
def argmin (number_list):
    return min ( enumerate(number_list)  , key=lambda x:x[1])[0]

for line in sys.stdin:
    if line != "\n":
        calories_actual += int(line)

    if line == "\n":
        if calories_actual > top_calories[min_arg_actual]:
            print ("top :" , top_calories)
            top_calories[min_arg_actual]= calories_actual
            min_arg_actual=argmin(top_calories) 
        calories_actual = 0


print("--------------------")
print ("top :" , top_calories)

