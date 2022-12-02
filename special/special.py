import sys


arr= []
for line in sys.stdin:
    arr.append(line.split("-")[1])


for s in sorted(arr):
    print(s.strip())