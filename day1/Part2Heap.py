
import sys
import heapq

calories = []
calories_actual= 0
for line in sys.stdin:
    if line != "\n":
        calories_actual += int(line)

    if line == "\n":
        calories.append(calories_actual)
        calories_actual =0
    

print("--------------------")
print ("top :" , heapq.nlargest(3, calories))

print ("top :" ,sum( heapq.nlargest(3, calories)))
