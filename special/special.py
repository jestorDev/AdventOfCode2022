import sys


arr= []
for line in sys.stdin:
    arr.append(line.split("-")[1])


for s in sorted(arr):
    print(s.strip())


'''


L 1

2329
L 2

3546
R 3

5288
L 4

6166
L 5

6597
L 6

6677
R 7

6711
R 8

L 9
RLRLRRLRRRRL 10
'''

